# Matatu Route Diary

## Overview
Karibu to the Matatu Route Diary, a jua kali CLI app for Kenyan commuters! Whether you’re dodging traffic on Route 46 from Kibera to CBD or vibing to benga tunes on a Mombasa matatu, this tool logs your rides. Track fares, routes, and driver vibes (e.g., “loud reggae, 60 KES”), then check trends like which route saves you cash. Built with Python, SQLAlchemy, and Alembic—pure hustle!

## Installation
1. Clone this repo: `git clone https://github.com/AmedDavid/matatu_diary.git`.
2. CD into the folder and run `pipenv install` for SQLAlchemy, Alembic, and Faker.
3. Fire up the env with `pipenv shell`.
4. Set the database with `alembic upgrade head` from `lib/db`.
5. (Optional) Seed data with `python lib/db/seed.py` for test rides.

## Usage
Run it with `python lib/cli.py`. Pick from:
- Create your rider profile (name, usual stop).
- Log a ride (route, fare, date, notes).
- See all your rides.
- Search by route (e.g., “Route 111”).
- Check fare trends (e.g., average for Ngong Road).
- Delete a ride or profile.
- Exit with a “Sawa!”.

## File Structure
- `lib/cli.py`: Your matatu dashboard with menus.
- `lib/helpers.py`: Functions to log rides and crunch fares.
- `lib/db/models.py`: `Rider` and `MatatuRide` models.
- `lib/db/seed.py`: Fills the database with test rides.

## Key Functions
- `create_rider()`: Sets your profile (e.g., “Juma, Kawangware”).
- `log_ride()`: Logs a ride (e.g., “Route 46, 50 KES, rainy day”).
- `display_rides()`: Shows all your matatu journeys.
- `find_rides_by_route()`: Finds rides on a route.
- `analyze_fares()`: Averages fares per route.
- `delete_rider()`: Wipes your profile and rides.
- `delete_ride()`: Ditches a single ride.

## Models
- `Rider`: Your name and stop (e.g., “Nairobi CBD”). Links to many rides.
- `MatatuRide`: Ride details (route, fare, date, notes). Tied to one rider.

## Requirements
- Python 3.8+
- Pipenv
- SQLAlchemy
- Alembic
- Faker