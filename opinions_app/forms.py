from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import MultipleFileField, FileAllowed


class OpinionForm(FlaskForm):
    title = StringField(
        'Введите название фильма',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 128)]
    )
    text = TextAreaField(
        'Напишите мнение', 
        validators=[DataRequired(message='Обязательное поле')]
    )
    images = MultipleFileField(
        validators=[
            FileAllowed(
                ['jpg', 'jpeg', 'png', 'gif', 'bmp'], 
                message=(
                    'Выберите файлы с расширением '
                    '.jpg, .jpeg, .png, .gif или .bmp'
                )
            )
        ]
    )
    submit = SubmitField('Добавить')
