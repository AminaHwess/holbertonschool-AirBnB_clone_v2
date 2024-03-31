#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, String, Column, Integer, Float, Table
import models
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review


if models.is_type == "db":
    place_amemity = Table("place_amenity", Base.metadata,
                            Column("place_id", String(60),
                                    ForeignKey("places.id"),
                                    primary_key=True, nullable=False),
                            Column("amenity_id", String(60),
                                    ForeignKey("amenities.id"),
                                    primary_key=True, nullable=False))
class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship('Amenity', secondary=place_amemity,
                             viewonly=False)

    @property
    def reviews(self):
        """Getter attribute reviews that returns the list of Review instances
        with place_id equals to the current Place.id
        """
        from models import storage
        my_list = []
        extracted_reviews = storage.all('Review').values()
        for review in extracted_reviews:
            if self.id == review.place_id:
                my_list.append(review)
        return my_list

    @property
    def amenities(self):
        """ Place amenities """
        ob = models.storage.all(Amenity).values()
        return [obj for obj in ob if obj.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, value):
        """ Amenities setter """
        if type(value) is Amenity:
            self.amenity_ids.append(value.id)