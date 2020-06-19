import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess!'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:yht19980803@localhost/course_select_system"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
