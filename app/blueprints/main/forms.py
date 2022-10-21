from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Gift(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    description = StringField('Description', validators = [DataRequired()])
    submit_button = SubmitField('Gift')

class Save(FlaskForm):
    save = StringField('save', validators = [DataRequired()])
    submit_button = SubmitField('Save')

class Comment(FlaskForm):
    comment = StringField('comment', validators = [DataRequired()])
    submit_button = SubmitField('Comment')