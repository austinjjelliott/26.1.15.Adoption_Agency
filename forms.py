from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange



animals = ["Dog", "Cat", "Porcupine"]

class AddPetForm(FlaskForm):

    name = StringField("Name?", validators = [InputRequired()])
    species = SelectField("Species?", choices = [(animal, animal) for animal in animals])
    photo_url = StringField("Photo URL", validators = [URL(), Optional()])
    age = IntegerField("Age?", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes about the animal", validators=[Optional()])

class EditPetForm(FlaskForm):

    photo_url = StringField("Photo URL", validators = [URL(), Optional()])
    notes = StringField("Notes about the animal", validators=[Optional()])
    available = BooleanField("Available for adoption?")