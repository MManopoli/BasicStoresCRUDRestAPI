from db import db
from models.store import StoreModel


# "Models" are the internal representation of some thing
# Also, because we're using SQLAlchemy, these objects are extending db.Model
class ItemModel(db.Model):
    # SQLAlchemy Setup
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship("StoreModel")

    def __init__(self, name, price, store_name):
        # self.id = _id  # No need to do this - SQLAlchemy does this for us because it's a primary_key in the database
        self.name = name
        self.price = price
        self.store_id = StoreModel.find_by_name(store_name).id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        # The session is a collection of objects to write to the database
        # We can add multiple objects to the session and write them all at once, which is more efficient
        # In this case, we're just writing the one
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
