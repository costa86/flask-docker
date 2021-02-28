import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #DATABASE_NAME="sample.sqlite3"
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{os.path.join(basedir, DATABASE_NAME)}" 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    #DATABASE_URL=postgresql://costa:12345@db:5432/sample

    SQLALCHEMY_TRACK_MODIFICATIONS = False
