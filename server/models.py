from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    price = Column(Numeric)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': str(self.price)  # Convert to string to ensure JSON serializability
        }

