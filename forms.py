from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
    author = StringField('Author', validators=[DataRequired(), Length(min=1, max=50)])
    pages = IntegerField('Pages', validators=[DataRequired()])
    submit = SubmitField('Submit')
