import os 
basedir = os.path.abspath(os.path.dirname(__file__))


class Config: 
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'datebese.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS=True
    SECRET_KEY = "Cristian"
    