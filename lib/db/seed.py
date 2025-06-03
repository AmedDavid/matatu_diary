from faker import Faker
from models import Rider, MatatuRide
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from datetime import datetime

# database seed script for Matatu Diary
# This script populates the database with sample data for testing purposes.

fake = Faker()
# engine = create_engine("sqlite:///../../matatu_diary.db")
engine = create_engine("sqlite:///matatu_diary.db")
print("seed.py database path:", engine.url)
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
    Rider(name="Fatuma", usual_stop="Mombasa Old Town"),
    Rider(name="David", usual_stop="Nairobi CBD"),
    Rider(name="Wanjiku", usual_stop="Kawangware"),
    Rider(name="Otieno", usual_stop="Dandora"),
    Rider(name="Njeri", usual_stop="Rongai"),
    Rider(name="Kamau", usual_stop="Embakasi")
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
    # Amina's rides
    MatatuRide(rider=riders[0], route="Route 46", fare=60, date=datetime.strptime("2025-05-27", "%Y-%m-%d").date(), notes="Loud reggae, fast ride", driver_vibe="Hustler", matatu_nickname="Nganya za Ronga"),
    MatatuRide(rider=riders[0], route="Route 111", fare=50, date=datetime.strptime("2025-02-18", "%Y-%m-%d").date(), notes="Rainy, slow traffic", driver_vibe="Chill", matatu_nickname="KBS Flyer"),
    MatatuRide(rider=riders[0], route="Route 46", fare=70, date=datetime.strptime("2025-05-28", "%Y-%m-%d").date(), notes="Heavy traffic, late", driver_vibe="Loud", matatu_nickname="Mtaa Blaster"),
    
    # Kiptoo's rides
    MatatuRide(rider=riders[1], route="Ngong Road", fare=40, date=datetime.strptime("2025-05-12", "%Y-%m-%d").date(), notes="Quiet driver", driver_vibe="Laidback", matatu_nickname="Super Metro King"),
    MatatuRide(rider=riders[1], route="Ngong Road", fare=45, date=datetime.strptime("2025-05-25", "%Y-%m-%d").date(), notes="Traffic jam, hot day", driver_vibe="Hustler", matatu_nickname="City Shuttle Beast"),
    
    # Fatuma's rides
    MatatuRide(rider=riders[2], route="Route 33", fare=70, date=datetime.strptime("2025-04-20", "%Y-%m-%d").date(), notes="Benga tunes, crowded", driver_vibe="Loud", matatu_nickname="Rasta Roadman"),
    MatatuRide(rider=riders[2], route="Route 33", fare=65, date=datetime.strptime("2025-05-15", "%Y-%m-%d").date(), notes="Smooth ride", driver_vibe="Chill", matatu_nickname="Nairobi Drift"),
    
    # David's rides
    MatatuRide(rider=riders[3], route="Route 39", fare=40, date=datetime.strptime("2025-05-29", "%Y-%m-%d").date(), notes="Very calm ride", driver_vibe="Chill", matatu_nickname="KBS Flyer"),
    MatatuRide(rider=riders[3], route="Route 111", fare=55, date=datetime.strptime("2025-05-20", "%Y-%m-%d").date(), notes="Traffic, noisy", driver_vibe="Hustler", matatu_nickname="Super Metro King"),
    
    # Wanjiku's rides
    MatatuRide(rider=riders[4], route="Route 46", fare=60, date=datetime.strptime("2025-05-26", "%Y-%m-%d").date(), notes="Traffic, reggae music", driver_vibe="Loud", matatu_nickname="Nganya za Ronga"),
    MatatuRide(rider=riders[4], route="Route 23", fare=30, date=datetime.strptime("2025-05-10", "%Y-%m-%d").date(), notes="Fast and smooth", driver_vibe="Laidback", matatu_nickname="Mtaa Blaster"),
    
    # Otieno's rides
    MatatuRide(rider=riders[5], route="Route 111", fare=50, date=datetime.strptime("2025-05-22", "%Y-%m-%d").date(), notes="Heavy traffic", driver_vibe="Hustler", matatu_nickname="Rasta Roadman"),
    
    # Njeri's rides
    MatatuRide(rider=riders[6], route="Ngong Road", fare=35, date=datetime.strptime("2025-05-18", "%Y-%m-%d").date(), notes="Cool driver", driver_vibe="Chill", matatu_nickname="Nairobi Drift"),
    
    # Kamau's rides
    MatatuRide(rider=riders[7], route="Route 33", fare=80, date=datetime.strptime("2025-05-29", "%Y-%m-%d").date(), notes="Crowded, slow traffic", driver_vibe="Loud", matatu_nickname="City Shuttle Beast")
]
session.add_all(rides)
session.commit()
print(f"Inserted MatatuRide rows: {session.query(MatatuRide).count()}")

# Print inserted rides
print("\nInserted Matatu Rides:")
for ride in session.query(MatatuRide).all():
    print(f"ID: {ride.id}, Rider ID: {ride.rider_id}, Route: {ride.route}, Fare: {ride.fare}, Date: {ride.date}, Notes: {ride.notes}, Driver Vibe: {ride.driver_vibe}, Matatu Nickname: {ride.matatu_nickname}")

print("Seeding completed successfully!")