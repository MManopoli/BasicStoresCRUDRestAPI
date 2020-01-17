from db import db


# "Models" are the internal representation of some thing
# Also, because we're using SQLAlchemy, these objects are extending db.Model
#
# Also - this is an API in and of itself
# This is an interface between the REST API and the "User" thing
# When we changed the find_by_username implementation -> Nothing changed for security.py
class UserModel(db.Model):
    # SQLAlchemy Setup
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))  # 80 character maximum
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # self.id = _id  # No need to do this - SQLAlchemy does this for us because it's a primary_key in the database
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        # The session is a collection of objects to write to the database
        # We can add multiple objects to the session and write them all at once, which is more efficient
        # In this case, we're just writing the one
        db.session.add(self)
        db.session.commit()
