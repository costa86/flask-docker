from app.auth import bp
from flask import render_template,redirect,url_for,flash
from app.models import User
from flask_login import login_user,logout_user,current_user,login_required
from app.auth.forms import RegistrationForm,LoginForm
from app import db


templates = {
    "auth":"auth/auth.html"
}

@bp.route("/login",methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for("main.index"))

    data = {
        "form":form,
        "title":"Login",
        "new_user":False
    }

    return render_template(templates["auth"],data=data)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))


def create_user(username,password):
    user = User(username=username)
    user.set_password(password=password)
    db.session.add(user)
    db.session.commit()
    flash("new user")

@bp.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        create_user(form.username.data,form.password.data)
        return redirect(url_for("auth.login"))

    data = {
        "title":"Register a new user",
        "form":form,
        "new_user":True
    }
    return render_template(templates["auth"],data=data)
