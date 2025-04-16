from flask import render_template, url_for, flash, redirect, jsonify
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
posts = [
    {
        'authur': 'Hamid Shah',
        'title': 'Blog Post 1',
        'contents': 'First post contents',
        'date_posted': 'April 20, 2018'
    },
        {
        'authur': 'Hassan Shah',
        'title': 'Blog Post 2',
        'contents': 'Second post contents',
        'date_posted': 'April 25, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'Success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # return jsonify({'status':'loged in'})
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have logged in!', 'Success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and passowrd', 'danger')
    return render_template('login.html', title='Login', form=form)

