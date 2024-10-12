from app import app
from models import Episode, Appearance, Guest, db
from faker import Faker
from random import randint, sample 
fake = Faker()

with app.app_context():
    # Clear existing data
    Guest.query.delete()  
    Appearance.query.delete()  
    Episode.query.delete()  

    # Create 10 guests
    guests = []
    for _ in range(10):
        guest = Guest(
            name=fake.name(),
            occupation=fake.job()
        )
        guests.append(guest)
    db.session.add_all(guests)
    db.session.commit()
    print("Creating guests...")

    # Create 5 episodes
    episodes = []
    for _ in range(5):  
        episode = Episode(
            date=fake.date(),
            number=randint(1, 100)
        )
        episodes.append(episode)
    db.session.add_all(episodes)
    db.session.commit()
    print("Creating episodes...")

    # Create appearances 
    appearances = []
    for episode in episodes:
        # Randomly assign 1 to 3 guests to each episode
        assigned_guests = sample(guests, randint(1, 3))
        for guest in assigned_guests:
            appearance = Appearance(
                rating=randint(1, 10),  # Random rating between 1 and 10
                episode_id=episode.id,
                guest_id=guest.id
            )
            appearances.append(appearance)
    db.session.add_all(appearances)
    db.session.commit()
    print("Creating appearances...")
   
    print("Seeding complete.")
