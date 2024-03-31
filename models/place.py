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
        from models import storage
        rev = []
        for x in storage.all(Review).values():
            if x.place_id == self.id:
                rev.append(x)
        return rev
    @property
    def amenities(self):
        from models import storage
        from models.amenity import Amenity
        ame = []
        moby = storage.all(Amenity)
        for amenity_inst in moby.values():
            if amenity_inst.id == self.amenity_id:
                ame.append(amenity_inst)
        return ame
    @amenities.setter
    def amenities(self, amenity_list):
        from models.amenity import Amenity
        for x in amenity_list:
            if type(x) == Amenity:
                self.amenity_ids.append(x)
    @reviews.setter
    def reviews(self, review_obj):
        if review_obj and review_obj not in self.review_ids:
            self.review_ids.append(review_obj.id)