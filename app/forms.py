from flask_wtf import FlaskForm
from wtforms import PasswordField, DateField, SubmitField, StringField, RadioField
from wtforms.validators import DataRequired, EqualTo, InputRequired, Length, Regexp, Email, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    firstName= StringField('Firstname', validators=[DataRequired()])
    surName= StringField('Surname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        InputRequired(message="Password is required"),
        Length(min=8, message="Password must be at least 8 characters long"),
        Regexp(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', 
               message="Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        InputRequired(message="Please confirm your password"),
        EqualTo('password', message="Passwords must match")
    ])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different username.')

    def validate_confirm_password(self, confirm_password):
        if self.password.data != confirm_password.data:
            raise ValidationError('Passwords do not match.')
        
    submit = SubmitField('Register')

class CSRFProtectForm(FlaskForm):
    """A simple form just for CSRF protection."""
    pass 