from helpers import get_or_create_rider, get_all_riders, log_ride, display_rides, find_rides_by_route, analyze_fares, delete_rider, delete_ride, check_traffic_alerts
import os
from datetime import datetime

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear_screen()
    print("=== Matatu Route Diary ===")
    print("1. Switch Rider Profile")
    print("2. Log a Matatu Ride")
    print("3. View All Rides")
    print("4. Find Rides by Route")
    print("5. Analyze Fare Trends")
    print("6. Delete a Ride")
    print("7. Delete Rider Profile")
    print("8. Check Traffic Alerts")
    print("9. View All Riders")
    print("0. Exit (Sawa!)")
    return input("> ")

def get_valid_fare():
    while True:
        fare_input = input("Enter fare in KES: ").strip()
        if fare_input.isdigit():
            return int(fare_input)
        print("Invalid fare! Please enter a numeric value (e.g., 40).")

def get_valid_date():
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD format (e.g., 2025-05-29).")

def select_rider():
    riders = get_all_riders()
    if not riders:
        print("No riders found. Let's create one!")
        name = input("Enter your name: ")
        stop = input("Enter your usual stop (e.g., Kibera): ")
        rider = get_or_create_rider(name, stop)
        return rider.id
    print("\nAvailable Riders:")
    print("-" * 60)
    print(f"{'ID':<4} {'Name':<20} {'Usual Stop':<20}")
    print("-" * 60)
    for rider in riders:
        print(f"{rider.id:<4} {rider.name:<20} {rider.usual_stop:<20}")
    print("-" * 60)
    while True:
        choice = input("Enter rider ID to select (or 'new' to create a new rider): ").strip()
        if choice.lower() == "new":
            name = input("Enter your name: ")
            stop = input("Enter your usual stop (e.g., Kibera): ")
            rider = get_or_create_rider(name, stop)
            return rider.id
        if choice.isdigit():
            rider_id = int(choice)
            if any(rider.id == rider_id for rider in riders):
                print(f"Selected rider ID: {rider_id}")
                return rider_id
        print("Invalid choice! Please enter a valid rider ID or 'new'.")

def main():
    clear_screen()
    print("Welcome to Matatu Route Diary!")
    rider_id = select_rider()
    while True:
        choice = menu()
        if choice == "1":
            rider_id = select_rider()
            input("Press Enter to continue...")
        elif choice == "2" and rider_id:
            route = input("Enter route (e.g., Route 46): ")
            fare = get_valid_fare()
            date = get_valid_date()
            notes = input("Any notes? (e.g., loud music): ")
            driver_vibe = input("Driver vibe? (e.g., Chill, Loud, Hustler): ").capitalize()
            log_ride(rider_id, route, fare, date, notes, driver_vibe)
            print("Ride logged! Pole sana for the hustle.")
            input("Press Enter to continue...")
        elif choice == "3" and rider_id:
            rides = display_rides(rider_id)
            if rides:
                print("\nYour Rides:")
                print("-" * 80)
                print(f"{'ID':<4} {'Route':<12} {'Fare (KES)':<10} {'Date':<12} {'Notes':<20} {'Vibe':<10} {'Matatu':<15}")
                print("-" * 80)
                for ride in rides:
                    print(f"{ride.id:<4} {ride.route:<12} {ride.fare:<10} {str(ride.date):<12} {ride.notes[:19]:<20} {ride.driver_vibe:<10} {ride.matatu_nickname:<15}")
                print("-" * 80)
            else:
                print("No rides logged yet!")
            input("Press Enter to continue...")
        elif choice == "4" and rider_id:
            route = input("Enter route to search: ")
            rides = find_rides_by_route(rider_id, route)
            if rides:
                print(f"\nRides on {route}:")
                for ride in rides:
                    print(f"Date: {ride.date}, Fare: {ride.fare} KES, Notes: {ride.notes}, Vibe: {ride.driver_vibe}, Matatu: {ride.matatu_nickname}")
            else:
                print(f"No rides found on {route}!")
            input("Press Enter to continue...")
        elif choice == "5" and rider_id:
            avg_fare = analyze_fares(rider_id)
            print(f"\nAverage fare for your routes: {avg_fare:.2f} KES")
            input("Press Enter to continue...")
        elif choice == "6" and rider_id:
            ride_id = int(input("Enter ride ID to delete: "))
            if delete_ride(ride_id):
                print("Ride deleted!")
            else:
                print("Ride not found!")
            input("Press Enter to continue...")
        elif choice == "7" and rider_id:
            if delete_rider(rider_id):
                print("Profile wiped! Start fresh anytime.")
                rider_id = None
                rider_id = select_rider()
            else:
                print("Rider not found!")
            input("Press Enter to continue...")
        elif choice == "8" and rider_id:
            traffic_report, suggestions = check_traffic_alerts(rider_id)
            if traffic_report:
                print("\nTraffic Alerts:")
                print("-" * 60)
                print(f"{'Route':<12} {'Congestion Score':<18} {'Latest Report':<15}")
                print("-" * 60)
                for route, score, latest_date in traffic_report:
                    print(f"{route:<12} {score:<18} {latest_date:<15}")
                    print(f"  Alternative: {suggestions[route]}")
                print("-" * 60)
            else:
                print("\nNo traffic alerts today. Safe travels!")
            input("Press Enter to continue...")
        elif choice == "9":
            riders = get_all_riders()
            if riders:
                print("\nAll Riders:")
                print("-" * 60)
                print(f"{'ID':<4} {'Name':<20} {'Usual Stop':<20}")
                print("-" * 60)
                for rider in riders:
                    print(f"{rider.id:<4} {rider.name:<20} {rider.usual_stop:<20}")
                print("-" * 60)
            else:
                print("No riders found!")
            input("Press Enter to continue...")
        elif choice == "0":
            print("Sawa! Thanks for riding with us.")
            break
        else:
            print("Hapana! Pick a valid option or select a rider first.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
    
    