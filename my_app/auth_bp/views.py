from . import auth
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from my_app.forms import LoginForm, RegisterForm
from my_app.models.users import User as users
from my_app.models.db import db


@auth.route('/register', methods=('POST', 'GET'))
def register():
    form = RegisterForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # handle form submission
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            
            if not users.user_exists(username=username, email=email):
                users.register_user(username=username, email=email, password=password)
                flash('Wellcome to the club...', 'text-bg-success')
                return redirect(url_for('auth.login'))
            else:
                flash('User is already registered...', 'text-bg-warning')

    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=('POST', 'GET'))
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # handle form submission
            username = request.form.get('username')
            password = request.form.get('password')
            
            user = users.find_user(username)
            if user:
                if check_password_hash(user.password, password):
                    login_user(user, remember=True)
                    flash('Successfully logged in...', 'text-bg-success')
                    return redirect(url_for('blog.index'))
                else:
                    flash('Password is incorrect...', 'text-bg-warning')
            else:
                flash(f'<{username}> is not registered yet...', 'text-bg-warning')

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
