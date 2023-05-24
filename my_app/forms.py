from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField(
        'Username', 
        validators=(DataRequired(), Length(min=3, max=50)), 
        render_kw={'class': 'form-control', 'placeholder': 'Johnny Walker'}
    )
        
    password = PasswordField(
        'Password', 
        validators=(DataRequired(), Length(min=4, max=16)), 
        render_kw={'class': 'form-control', 'placeholder': '4-16 characters'}
    )
        


class RegisterForm(FlaskForm):
    email = StringField(
        'Email', 
        validators=(DataRequired(), Email()), 
        render_kw={'class': 'form-control', 'placeholder': 'johnny.walker@gmail.com'}
        )
    username = StringField(
        'Username', 
        validators=( DataRequired(), Length(min=3, max=50)), 
        render_kw={'class': 'form-control', 'placeholder': 'Johnny Walker'}
        )
    password = PasswordField(
        'Password', 
        validators=(
        DataRequired(), Length(min=4, max=16)), 
        render_kw={'class': 'form-control', 'placeholder': '4-16 characters'}
        )
    password_r = PasswordField(
        validators=(DataRequired(), EqualTo('password', message='Passwords must match...')), 
        render_kw={'class': 'form-control', 'placeholder': 'Repeat password'}
        )


class PostForm(FlaskForm):
    title = StringField(
        'Title',
        validators=(DataRequired(), Length(min=4, max=50)),
        render_kw={'class': 'form-control', 'placeholder': 'Name your article'}
    )
    content = TextAreaField(
        'Content',
        validators=(DataRequired(),),
        render_kw={'class': 'form-control', 'placeholder': 'Write your story hear...', 'rows': '15'}
    )


class UsernameEmailEditForm(FlaskForm):
    email = StringField(
        'Change email', 
        validators=(DataRequired(), Email()), 
        render_kw={'class': 'form-control', 'placeholder': 'johnny.walker@gmail.com'}
        )
    username = StringField(
        'Change username', 
        validators=( DataRequired(), Length(min=3, max=50)), 
        render_kw={'class': 'form-control', 'placeholder': 'Johnny Walker'}
        ) 
    

class PasswordEditForm(FlaskForm):
    old_password = PasswordField(
        'Old password', 
        validators=(DataRequired(), Length(min=4, max=16)), 
        render_kw={'class': 'form-control', 'placeholder': 'Confirm old password*'}
        )
    new_password = PasswordField(
        'New password',
        validators= (DataRequired(), Length(min=4, max=16)), 
        render_kw={'class': 'form-control', 'placeholder': '4-16 characters'}
        )
    new_password_r = PasswordField(
        validators=(DataRequired(), EqualTo('new_password', message='Passwords must match...')), 
        render_kw={'class': 'form-control', 'placeholder': 'Repeat password'}
        )






