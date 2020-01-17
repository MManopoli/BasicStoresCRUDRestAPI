from db import db


# "Models" are the internal representation of some thing
# Also, because we're using SQLAlchemy, these objects are extending db.Model
class StoreModel(db.Model):
    # SQLAlchemy Setup
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # Setting lazy to dynamic turns items into a query builder that only executes when we run items.all()
    items = db.relationship("ItemModel", lazy="dynamic")

    def __init__(self, name):
        # self.id = _id  # No need to do this - SQLAlchemy does this for us because it's a primary_key in the database
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

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
