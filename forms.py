from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional, Email, DataRequired


class AddPetForm(FlaskForm):
    name = StringField(
        "Pet's Name",
        validators=[InputRequired(message="Please enter the pet's name.")]
    )

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL(message="Please enter a valid URL.")]
    )

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)]
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)]
    )

    color = StringField("Color")
    size = SelectField("Size", choices=[("small", "Small"), ("medium", "Medium"), ("large", "Large")])
    special_requirements = TextAreaField("Special Requirements")


class EditPetForm(FlaskForm):
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL(message="Please enter a valid URL.")]
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)]
    )

    is_available = BooleanField("Is Available?")


