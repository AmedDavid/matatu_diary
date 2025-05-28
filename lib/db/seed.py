from faker import Faker
from models import Rider, MatatuRide
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

fake = Faker()
engine = create_engine("sqlite:///matatu_diary.db")
Session = sessionmaker(bind=engine)
session = Session()

# Sample riders
riders = [
    Rider(name="Amina", usual_stop="Kibera"),
    Rider(name="Kiptoo", usual_stop="Ngong"),
    Rider(name="Fatuma", usual_stop="Mombasa Old Town")
]
session.add_all(riders)

# Sample rides
rides = [
    MatatuRide(rider=riders[0], route="Route 46", fare=60, date=fake.date_this_year(), notes="Loud reggae, fast ride"),
    MatatuRide(rider=riders[0], route="Route 111", fare=50, date=fake.date_this_year(), notes="Rainy, slow traffic"),
    MatatuRide(rider=riders[1], route="Ngong Road", fare=40, date=fake.date_this_year(), notes="Quiet driver"),
    MatatuRide(rider=riders[2], route="Route 33", fare=70, date=fake.date_this_year(), notes="Benga tunes, crowded")
]
session.add_all(rides)

session.commit()