from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from . import blog
from my_app.forms import PostForm, UsernameEmailEditForm, PasswordEditForm
from my_app.models.posts import Post as posts
from my_app.models.users import User as users


@blog.route('/')
def index():
    all_posts = posts.query.all()
    return render_template('blog/index.html', all_posts=all_posts)


@blog.route('/post/<int:id>')
def post_info(id):
    post = posts.query.get_or_404(id)
    return render_template('blog/post_info.html', post=post)


@blog.route('/create', methods=('POST', 'GET'))
@login_required
def create_post():
    form = PostForm()

    if request.method == 'POST':
        if form.validate_on_submit:
            title = request.form.get('title')
            content = request.form.get('content')
            posts.add_post(title=title, content=content,
                           user_id=current_user.id)
            flash('Successfully created...', 'text-bg-success')
            return redirect(url_for('blog.index'))

    return render_template('blog/create_post.html', form=form)


@blog.route('/update/<int:id>', methods=('POST', 'GET'))
@login_required
def update_post(id):
    post = posts.query.get_or_404(id)
    form = PostForm()
    form.title.data, form.content.data = post.title, post.content

    if request.method == 'POST' and form.validate_on_submit:
        title = request.form.get('title')
        content = request.form.get('content')
        posts.update_post(title=title, content=content, id=id)
        flash('Successfully updated...', category='text-bg-success')
        return redirect(url_for('blog.index'))

    return render_template('blog/update_post.html', form=form)


@blog.route('/delete/<int:id>')
@login_required
def delete_post(id):
    posts.delete_post(id)
    flash('Post was deleted...', 'text-bg-success')
    return redirect(url_for('blog.index'))


@blog.route('/profile/<int:id>')
@login_required
def profile(id):
    username_email_form = UsernameEmailEditForm()
    username_email_form.username.data = current_user.username
    username_email_form.email.data = current_user.email
    password_form = PasswordEditForm()
    user_posts = current_user.posts
    posts_count = len(user_posts)
    data = {'username_email_form': username_email_form, 'password_form': password_form, 
            'user_posts': user_posts, 'posts_count': posts_count}
    return render_template('blog/profile.html', data=data)


@blog.route('/profile/update_username_email/<int:id>', methods=('POST',))
@login_required
def update_username_email(id):
    form = UsernameEmailEditForm(request.form)

    if form.validate_on_submit():
        username = request.form.get('username')
        email = request.form.get('email')
        users.update_username_email(id=id, username=username, email=email)
        flash('Data updated successfully...', 'text-bg-success')

    return redirect(url_for('blog.profile', id=id))


@blog.route('/profile/update_password/<int:id>', methods=('POST',))
@login_required
def update_password(id):
    form = PasswordEditForm(request.form)
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')

    if check_password_hash(current_user.password, old_password):

        if form.validate_on_submit():
            users.update_password(id=id, password=new_password)
            flash('Password successfully changed...', 'text-bg-success')
        else:
            flash('Passwords must match...')
    else:
        flash('Wrong old password...', 'text-bg-warning')

    return redirect(url_for('blog.profile', id=id))



@blog.route('/delete_profile/<int:id>')
def delete_profile(id):
    posts.delete_all_user_posts(id)
    users.delete_user(id)
    flash('Account and all posts were deleted successfylly...')
    return redirect(url_for('auth.login'))
