from db.models import Rider, MatatuRide
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import random

# engine = create_engine("sqlite:///../matatu_diary.db")
engine = create_engine("sqlite:///matatu_diary.db")
print("helpers.py database path:", engine.url)  # Debug output
Session = sessionmaker(bind=engine)
session = Session()

# List of Kenyan matatu nicknames
MATATU_NICKNAMES = [
    "Nganya za Ronga",
    "KBS Flyer",
    "Mtaa Blaster",
    "Super Metro King",
    "City Shuttle Beast",
    "Rasta Roadman",
    "Nairobi Drift"
]

# Simple route suggestions for traffic-heavy routes
TRAFFIC_ALTERNATIVES = {
    "Route 46": "Route 111",
    "Route 111": "Route 23",
    "Ngong Road": "Route 24"
}

def create_rider(name, usual_stop):
    new_rider = Rider(name=name, usual_stop=usual_stop)
    session.add(new_rider)
    session.commit()
    return new_rider

def log_ride(rider_id, route, fare, date, notes, driver_vibe):
    matatu_nickname = random.choice(MATATU_NICKNAMES)
    new_ride = MatatuRide(
        rider_id=rider_id,
        route=route,
        fare=fare,
        date=datetime.strptime(date, "%Y-%m-%d"),
        notes=notes,
        driver_vibe=driver_vibe,
        matatu_nickname=matatu_nickname
    )
    session.add(new_ride)
    session.commit()
    return new_ride

def display_rides(rider_id):
    rides = session.query(MatatuRide).filter_by(rider_id=rider_id).all()
    return rides

def find_rides_by_route(rider_id, route):
    rides = session.query(MatatuRide).filter_by(rider_id=rider_id, route=route).all()
    return rides

def analyze_fares(rider_id):
    rides = session.query(MatatuRide).filter_by(rider_id=rider_id).all()
    if rides:
        avg_fare = sum(ride.fare for ride in rides) / len(rides)
        return avg_fare
    return 0

def check_traffic_alerts(rider_id):
    rides = session.query(MatatuRide).filter_by(rider_id=rider_id).all()
    traffic_routes = [ride.route for ride in rides if "traffic" in (ride.notes or "").lower()]
    if traffic_routes:
        suggestions = {route: TRAFFIC_ALTERNATIVES.get(route, "No alternative") for route in traffic_routes}
        return traffic_routes, suggestions
    return None, None

def delete_rider(rider_id):
    rider = session.query(Rider).get(rider_id)
    if rider:
        session.delete(rider)
        session.commit()

def delete_ride(ride_id):
    ride = session.query(MatatuRide).get(ride_id)
    if ride:
        session.delete(ride)
        session.commit()