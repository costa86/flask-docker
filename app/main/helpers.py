
from flask import flash
from app.models import Post
from app import db

def create_post(body):
    post = Post(body=body)
    db.session.add(post)
    db.session.commit()
    flash("A new post has been created")