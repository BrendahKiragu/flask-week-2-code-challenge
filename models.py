from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import AssociationProxy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Episode(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    #relationships
    appearances = db.relationship('Appearance', back_populates='episode')
    guests = AssociationProxy('appearances', 'guest', creator=lambda guestObj: Appearance(guest=guestObj))

class Appearance(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True) 
    rating = db.Column(db.Integer) 
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))  # Foreign key reference to Episode
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'))  # Foreign key reference to Guest

    # relationships
    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')


class Guest(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String) 
    occupation = db.Column(db.String) 

    #relationships
    appearances = db.relationship('Appearance', back_populates='guest')
    episodes = AssociationProxy('appearances', 'episode', creator=lambda episodeObj: Appearance(episode=episodeObj))

