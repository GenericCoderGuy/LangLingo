from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main.models import User, Post, Phrase, Comment
from app import db
from flask_login import current_user, login_required
from googletrans import Translator
from app.blueprints.main.forms import Save

@app.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        posts = Post.query.all()
        users = User.query.all()

        if request.method == 'GET':
            return render_template('home.html', current=current, posts=posts, users=users, currentCall=currentCall)

        if request.method == 'POST':
            post_title = request.form['title']
            post_body = request.form['body']
            new_post = Post(title=post_title, body=post_body, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()

            flash('Post added successfully', 'success')
            return redirect(url_for('main.home', title=post_title, body=post_body, new_post=new_post))

    else:
        return redirect(url_for('auth.landing'))

@app.route('/explore')
def explore():
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        posts = Post.query.all()
        users = User.query.all()

        if request.method == 'GET':
            return render_template('explore.html', current=current, posts=posts, users=users, currentCall=currentCall)

    else:
        return redirect(url_for('auth.landing'))

@app.route('/about')
def about():
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        posts = Post.query.all()
        users = User.query.all()

        if request.method == 'GET':
            return render_template('about.html', current=current, posts=posts, users=users, currentCall=currentCall)

    else:
        return redirect(url_for('auth.landing'))

@app.route('/contact')
def contact():
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        posts = Post.query.all()
        users = User.query.all()

        if request.method == 'GET':
            return render_template('contact.html', current=current, posts=posts, users=users, currentCall=currentCall)

    else:
        return redirect(url_for('auth.landing'))

@app.route('/translate_lang', methods=['GET', 'POST'])
def translate_lang():
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        form = Save()
        phrases = Phrase.query.all()
        lang = [{"name":'afrikaans',"code":"af"},{"name":'albanian',"code":"sq"},{"name":'amharic',"code":"am"},
        {"name":'arabic',"code":"ar"},{"name":'armenian',"code":"hy"},{"name":'azerbaijani',"code":"az"},
        {"name":'basque',"code":"eu"},{"name":'belarusian',"code":"be"},{"name":'bengali',"code":"bn"},
        {"name":'bosnian',"code":"bs"},{"name":'bulgarian',"code":"bg"},{"name":'catalan',"code":"ca"},
        {"name":'cebuano',"code":"ceb"},{"name":'chichewa',"code":"ny"},{"name":'chinese (simplified)',"code":"zh-cn"},
        {"name":'chinese (traditional)',"code":"zh-tw"},{"name":'corsican',"code":"co"},{"name":'croatian',"code":"hr"},
        {"name":'czech',"code":"cs"},{"name":'danish',"code":"da"},{"name":'dutch',"code":"nl"},
        {"name":'english',"code":"en"},{"name":'esperanto',"code":"eo"},{"name":'estonian',"code":"et"},
        {"name":'filipino',"code":"tl"},{"name":'finnish',"code":"fi"},{"name":'french',"code":"fr"},
        {"name":'frisian',"code":"fy"},{"name":'galician',"code":"gl"},{"name":'georgian',"code":"ka"},
        {"name":'german',"code":"de"},{"name":'greek',"code":"el"},{"name":'gujarati',"code":"gu"},
        {"name":'haitian creole',"code":"ht"},{"name":'hausa',"code":"ha"},{"name":'hawaiian',"code":"haw"},
        {"name":'hebrew',"code":"iw"},{"name":'hindi',"code":"hi"},{"name":'hmong',"code":"hmn"},
        {"name":'hungarian',"code":"hu"},{"name":'icelandic',"code":"is"},{"name":'igbo',"code":"ig"},
        {"name":'indonesian',"code":"id"},{"name":'irish',"code":"ga"},{"name":'italian',"code":"it"},
        {"name":'japanese',"code":"ja"},{"name":'javanese',"code":"jw"},{"name":'kannada',"code":"kn"},
        {"name":'kazakh',"code":"kk"},{"name":'khmer',"code":"km"},{"name":'korean',"code":"ko"},
        {"name":'kurdish (kurmanji)',"code":"ku"},{"name":'kyrgyz',"code":"ky"},{"name":'lao',"code":"lo"},
        {"name":'latin',"code":"la"},{"name":'latvian',"code":"lv"},{"name":'lithuanian',"code":"lt"},
        {"name":'luxembourgish',"code":"lb"},{"name":'macedonian',"code":"mk"},{"name":'malagasy',"code":"mg"},
        {"name":'malay',"code":"ms"},{"name":'malayalam',"code":"ml"},{"name":'maltese',"code":"mt"},
        {"name":'maori',"code":"mi"},{"name":'marathi',"code":"mr"},{"name":'mongolian',"code":"mn"},
        {"name":'myanmar (burmese)',"code":"my"},{"name":'nepali',"code":"ne"},{"name":'norwegian',"code":"no"},
        {"name":'pashto',"code":"ps"},{"name":'persian',"code":"fa"},{"name":'polish',"code":"pl"},
        {"name":'portuguese',"code":"pt"},{"name":'punjabi',"code":"pa"},{"name":'romanian',"code":"ro"},
        {"name":'russian',"code":"ru"},{"name":'samoan',"code":"sm"},{"name":'scots gaelic',"code":"gd"},
        {"name":'serbian',"code":"sr"},{"name":'sesotho',"code":"st"},{"name":'shona',"code":"sn"},
        {"name":'sindhi',"code":"sd"},{"name":'sinhala',"code":"si"},{"name":'slovak',"code":"sk"},
        {"name":'slovenian',"code":"sl"},{"name":'somali',"code":"so"},{"name":'spanish',"code":"es"},
        {"name":'sundanese',"code":"su"},{"name":'swahili',"code":"sw"},{"name":'swedish',"code":"sv"},
        {"name":'tajik',"code":"tg"},{"name":'tamil',"code":"ta"},{"name":'telugu',"code":"te"},
        {"name":'thai',"code":"th"},{"name":'turkish',"code":"tr"},{"name":'ukrainian',"code":"uk"},
        {"name":'urdu',"code":"ur"},{"name":'uzbek',"code":"uz"},{"name":'vietnamese',"code":"vi"},
        {"name":'welsh',"code":"cy"},{"name":'xhosa',"code":"xh"},{"name":'yiddish',"code":"yi"},
        {"name":'yoruba',"code":"yo"},{"name":'zulu',"code":"zu"},{"name":'Filipino',"code":"fil"},
        {"name":'Hebrew',"code":"he"}]

        if request.method == 'GET':
            return render_template('translator.html', phrases=phrases, current=current, currentCall=currentCall, languages=lang, form=form)

        if request.method == 'POST':
            sentence = str(request.form["sentence"])
            code = str(request.form["code"])
            # src = str(request.form["src"])
            src = 'en'

            print(sentence)
            translator = Translator()

            translated_sentence = translator.translate(text=sentence, src='en', dest=code)
            translated = translated_sentence.text
            translatedString = str(translated)

            newPhrase = Phrase(textOriginal=sentence, textTranslated=translatedString, languageOriginal=src, languageTranslated=code, user_id=current_user.id)

            db.session.add(newPhrase)
            db.session.commit()

            flash('This phrase has been saved to your profile', 'success')

            return redirect(url_for('main.translate_lang'))
        
    else:
        return redirect(url_for('auth.landing'))

@app.route('/learn', methods=['GET', 'POST'])
def learn():
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)

        if request.method == 'GET':
            return render_template('learn.html', current=current, currentCall=currentCall)

        if request.method == 'POST':
            answer = request.form['body']
            # new_post = Post(title=post_title, body=post_body, user_id=current_user.id)
            # db.session.add(new_post)
            # db.session.commit()

            if answer.lower() == "hola":
                flash('Correct', 'success')
                return render_template('learn.html', current=current, currentCall=currentCall)

            else:
                flash('Incorrect', 'danger')
                return render_template('learn.html', current=current, currentCall=currentCall)

    else:
        return redirect(url_for('auth.landing'))

@app.route('/post', methods=['POST'])
@login_required
def create_post():
    post_title = request.form['title']
    post_body = request.form['body']
    
    new_post = Post(title=post_title, body=post_body, user_id=current_user.id)

    db.session.add(new_post)
    db.session.commit()

    flash('Post added successfully', 'success')
    return redirect(url_for('main.home'))

@app.route('/profile')
@login_required
def profile():
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        posts = Post.query.all()
        users = User.query.all()
        phrases = Phrase.query.all()

        if request.method == 'GET':
            return render_template('profile.html', current=current, posts=posts, users=users, phrases=phrases, currentCall=currentCall)

        else:
            return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('auth.login'))

@app.route('/profile/<id>', methods=['GET', 'POST'])
def user(id):
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        posts = Post.query.all()
        users = User.query.all()
        phrases = Phrase.query.all()
        
        user = User.query.get(id)
        # stringedUser = user.id

        if request.method == 'GET':
            return render_template('profile-other.html', user=user, current=current, posts=posts, users=users, phrases=phrases, currentCall=currentCall)

        else:
            return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('auth.login'))


@app.route('/post/<id>', methods=['GET', 'POST'])
def post(id):
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        posts = Post.query.all()
        users = User.query.all()
        comments = Comment.query.all()
        userComment = User.query.get(id)
        
        single_post = Post.query.get(id)
        stringedPost = single_post.id
        user = User.query.get(single_post.user_id)

        if request.method == 'GET':
            return render_template('single-post.html', userComment=userComment, comments=comments, post=single_post, user=user, current=current, posts=posts, users=users)
        
        if request.method == 'POST':
            comment = str(request.form["comment"])

            newComment = Comment(body=comment, post_id=stringedPost, user_id=current_user.id)

            db.session.add(newComment)
            db.session.commit()

            flash('Comment successfully posted!', 'success')

            return redirect(url_for('main.post', id=stringedPost))

    else:
        return redirect(url_for('auth.login'))

