from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    '''Form to add a pet'''

    name = StringField('Pet Name', validators=[
                       InputRequired(message='Pet Name cannot be blank')])

    species = SelectField(
        'Species',
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    age = IntegerField('Age', validators=[
                       Optional(), NumberRange(min=0, max=30)])

    notes = TextAreaField('Notes about the Pet', validators=[Optional()])


class EditPetForm(FlaskForm):
    '''Form to edit a pet'''

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    notes = TextAreaField('Notes about the Pet', validators=[Optional()])

    available = BooleanField('Available?')
