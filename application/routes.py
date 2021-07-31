from flask import render_template, flash, redirect, json
from application import app, db
from application.forms import LoginForm
from application.models import User
import os

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    filename = os.path.join(app.static_folder, 'data', 'menu.json')
    with open(filename) as file:
        data = json.load(file)
    return render_template("index.html", data=data)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data
        
        user        = User.objects(email=email).first()
        if user and user.password == password:
            flash(f"Welcome {user.username} to Our Restaurant !", "success")
            return redirect("/index")
        else:
            flash("Sorry...Please double check your email and password!", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/order", methods=['POST', 'GET'])
def order():
    return render_template("order.html", title="Order History")

@app.route("/menu", methods=['POST', 'GET'])
def menu():
    return render_template("menu.html", title="menu")

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    return render_template("contact.html", title="contact")