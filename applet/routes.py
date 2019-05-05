# -*- coding: utf-8 -*-
import time
import urllib.request
from flask import render_template, flash, redirect
from applet import app
from applet.forms import MyForm

@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def index():
    form = MyForm()
    if form.validate_on_submit(): 
        path = '/static/download/' 
        name = "photo"+str(int(time.time()))+".jpg"
        try:
        	urllib.request.urlretrieve(form.url.data, "applet"+path+name)
        except:
        	return render_template('index.html', form=form, exception=True)
        return render_template("index.html", archive=path+name)
    return render_template('index.html', form=form)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title="Contacts")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/success')
def success():
    return render_template('success.html', title="Success")