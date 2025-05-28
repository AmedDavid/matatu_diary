from faker import Faker
from models import Rider, MatatuRide
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

fake = Faker()
engine = create_engine("sqlite:///../../matatu_diary.db")
print("Seed database path:", engine.url)  # Debug path
Session = sessionmaker(bind=engine)
session = Session()

# Matatu nicknames
MATATU_NICKNAMES = [
    "Nganya za Ronga",
    "KBS Flyer",
    "Mtaa Blaster",
    "Super Metro King",
    "City Shuttle Beast",
    "Rasta Roadman",
    "Nairobi Drift"
]

# Clear existing data
session.query(MatatuRide).delete()
session.query(Rider).delete()
session.commit()
print(f"Deleted MatatuRide rows: {session.query(MatatuRide).count()}")
print(f"Deleted Rider rows: {session.query(Rider).count()}")

# Sample riders
riders = [
    Rider(name="Amina", usual_stop="Kibera"),
    Rider(name="Kiptoo", usual_stop="Ngong"),
    Rider(name="Fatuma", usual_stop="Mombasa Old Town")
]
session.add_all(riders)
session.commit()
print(f"Inserted Rider rows: {session.query(Rider).count()}")

# Print inserted riders
print("\nInserted Riders:")
for rider in session.query(Rider).all():
    print(f"ID: {rider.id}, Name: {rider.name}, Usual Stop: {rider.usual_stop}")

# Sample rides with driver vibes and nicknames
rides = [
    MatatuRide(rider=riders[0], route="Route 46", fare=60, date=fake.date_this_year(), notes="Loud reggae, fast ride", driver_vibe="Hustler", matatu_nickname="Nganya za Ronga"),
    MatatuRide(rider=riders[0], route="Route 111", fare=50, date=fake.date_this_year(), notes="Rainy, slow traffic", driver_vibe="Chill", matatu_nickname="KBS Flyer"),
    MatatuRide(rider=riders[1], route="Ngong Road", fare=40, date=fake.date_this_year(), notes="Quiet driver", driver_vibe="Laidback", matatu_nickname="Super Metro King"),
    MatatuRide(rider=riders[2], route="Route 33", fare=70, date=fake.date_this_year(), notes="Benga tunes, crowded", driver_vibe="Loud", matatu_nickname="Rasta Roadman")
]
session.add_all(rides)
session.commit()
print(f"Inserted MatatuRide rows: {session.query(MatatuRide).count()}")

# Print inserted rides
print("\nInserted Matatu Rides:")
for ride in session.query(MatatuRide).all():
    print(f"ID: {ride.id}, Rider ID: {ride.rider_id}, Route: {ride.route}, Fare: {ride.fare}, Date: {ride.date}, Notes: {ride.notes}, Driver Vibe: {ride.driver_vibe}, Matatu Nickname: {ride.matatu_nickname}")

print("Seeding completed successfully!")