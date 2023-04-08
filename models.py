from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = 'https://images.unsplash.com/photo-1415369629372-26f2fe60c467?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80'

db = SQLAlchemy()


def connect_db(app):
    '''Conncet database to Flask app'''
    with app.app_context():
        db.app = app
        db.init_app(app)


class Pet(db.Model):
    '''Pet for adoption'''

    __tablename_ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True, nullable=False)

    def image_url(self):
        '''Display default or presented image'''

        return self.photo_url or DEFAULT_IMAGE
