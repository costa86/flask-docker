from flask import render_template
from app import db
from app.errors import bp

@bp.app_errorhandler(404)
def not_found(e):
    return render_template("errors/404.html")

@bp.app_errorhandler(401)
def not_authorized(e):
    return render_template("errors/401.html")

@bp.app_errorhandler(500)
def internal_error(e):
    db.session.rollback()
    return render_template("errors/500.html")