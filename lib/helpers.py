from db.models import Rider, MatatuRide
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///../matatu_diary.db")
Session = sessionmaker(bind=engine)
session = Session()

def create_rider(name, usual_stop):
    new_rider = Rider(name=name, usual_stop=usual_stop)
    session.add(new_rider)
    session.commit()
    return new_rider

def log_ride(rider_id, route, fare, date, notes):
    new_ride = MatatuRide(rider_id=rider_id, route=route, fare=fare, date=datetime.strptime(date, "%Y-%m-%d"), notes=notes)
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