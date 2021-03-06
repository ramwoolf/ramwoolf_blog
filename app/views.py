from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = { 'nickname': 'Ramwoolf' }
    posts = [
    	{
    		'author': {'nickname': 'John'},
    		'body': 'OLOLOLO'
    	},
    	{
    		'author': {'nickname': 'Vasya'},
    		'body': 'BREKEKE'
    	}
    ]
    return render_template("index.html", title = 'Home', user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember me=' + str(form.remember_me.data))
        return redirect('/index')

    return render_template('login.html', title = 'Sign In', form = form)