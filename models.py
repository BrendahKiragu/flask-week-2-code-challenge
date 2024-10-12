from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import AssociationProxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    serialize_rules = ("-appearances.episode")

    #relationships
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')
    guests = AssociationProxy('appearances', 'guest', creator=lambda guestObj: Appearance(guest=guestObj))

class Appearance(db.Model, SerializerMixin):
    __tablename__ = "appearances"

    id = db.Column(db.Integer, primary_key=True) 
    rating = db.Column(db.Integer) 
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))  # Foreign key reference to Episode
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))  # Foreign key reference to Guest

    serialize_rules = ("-episode.appearances", "-guest.apearances")

    # relationships
    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')

    @validates('rating')
    def validate_rating(self, key, rating):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating

class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String) 
    occupation = db.Column(db.String) 

    serialize_rules = ("-appearances.guest")

    #relationships
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')
    episodes = AssociationProxy('appearances', 'episode', creator=lambda episodeObj: Appearance(episode=episodeObj))

