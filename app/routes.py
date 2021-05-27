from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from app import app

@app.route("/")
@app.route("/index")
def index():
    page = "Index"
    items = [
        "Cavalier King Charles Spaniel",
        "German Shepherd",
        "Alaskan Malamute",
    ]
    return render_template("index.html", page=page, items=items)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', page='Sign In', form=form)