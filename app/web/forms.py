from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


from app import User


class NewUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 128)])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 128),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    email = StringField('Email', validators=[DataRequired(), Length(1, 128),
                                             Email()])
    street = StringField('Street', validators=[DataRequired(), Length(1, 128)])
    suite = StringField('Suite', validators=[DataRequired(), Length(1, 128)])
    city = StringField('City', validators=[DataRequired(), Length(1, 128)])
    zipcode = StringField('Zipcode', validators=[DataRequired(), Length(1, 128)])
    lat = StringField('Latitude', validators=[DataRequired(), Length(1, 128)])
    lng = StringField('Longitude', validators=[DataRequired(), Length(1, 128)])
    phone = StringField('Phone', validators=[DataRequired(), Length(1, 128)])
    website = StringField('Website', validators=[DataRequired(), Length(1, 128)])
    company_name = StringField('Company Name', validators=[DataRequired(), Length(1, 128)])
    company_catchPhrase = StringField('CatchPhrase', validators=[DataRequired(), Length(1, 128)])
    company_bs = StringField('Company Description', validators=[DataRequired(), Length(1, 128)])

    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password_confirm', message='Passwords must match.')])
    password_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
