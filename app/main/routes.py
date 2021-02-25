from app.main import bp
from flask import render_template,redirect,url_for,flash
from app.models import Post,User
from flask_login import current_user,login_required
from app import db
from app.main.forms import PostForm
from .helpers import create_post

@bp.route('/')
def index():
    data = {
        "home":True,
        "title":"home"
    }
    return render_template("index.html",data=data)

@bp.route("/posts/add",methods=["GET","POST"])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        create_post(form.post.data)
        return redirect(url_for("main.posts"))
    data = {
        "form":form,
        "title":"New Post"
    }
    return render_template("index.html",data=data)


@bp.route("/posts")
@login_required
def posts():
    data ={
        "posts":Post.query.all(),
        "title":"Posts"
    }
    return render_template("posts.html",data=data)

@bp.route("/users")
@login_required
def users():
    data = {
        "users":User.query.all(),
        "title":"Users"
    }

    return render_template("users.html",data=data)


@bp.route("/user/<id>")
@login_required
def get_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    data = {
        "user":user,
        "title":f"User {user.username}"
    }

    return render_template("user.html",data=data)

@bp.route("/users/<username>")
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    data = {
        "user":user,
        "title":f"User {user.username}"
    }

    return render_template("profile.html",data=data)


@bp.route("/post/<id>")
@login_required
def get_post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    data = {
        "post":post,
        "title":f"Post ID {post.id}"
    }

    return render_template("post.html",data=data)