from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired, Length, EqualTo , Email, ValidationError
from Pack.models import Student
class RegisterUser(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Student.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("User already Exist")


    def validate_email(self, email):
        useremail = Student.query.filter_by(email=email.data).first()
        if useremail:
            raise ValidationError("E-mail already Exist")


class LoginUser(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('Log in')

class AddSubject(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    # student_id = SelectField('Student ID',validators=[DataRequired()])
    submit = SubmitField('Add Subject')