from helpers import create_rider, log_ride, display_rides, find_rides_by_route, analyze_fares, delete_rider, delete_ride, check_traffic_alerts
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear_screen()
    print("=== Matatu Route Diary ===")
    print("1. Create Rider Profile")
    print("2. Log a Matatu Ride")
    print("3. View All Rides")
    print("4. Find Rides by Route")
    print("5. Analyze Fare Trends")
    print("6. Delete a Ride")
    print("7. Delete Rider Profile")
    print("8. Check Traffic Alerts")
    print("0. Exit (Sawa!)")
    return input("> ")

def main():
    rider_id = None
    while True:
        choice = menu()
        if choice == "1":
            name = input("Enter your name: ")
            stop = input("Enter your usual stop (e.g., Kibera): ")
            rider = create_rider(name, stop)
            rider_id = rider.id
            print(f"Karibu, {name}! Your ID is {rider_id}.")
        elif choice == "2" and rider_id:
            route = input("Enter route (e.g., Route 46): ")
            fare = int(input("Enter fare in KES: "))
            date = input("Enter date (YYYY-MM-DD): ")
            notes = input("Any notes? (e.g., loud music): ")
            driver_vibe = input("Driver vibe? (e.g., Chill, Loud, Hustler): ")
            log_ride(rider_id, route, fare, date, notes, driver_vibe)
            print("Ride logged! Pole sana for the hustle.")
        elif choice == "3" and rider_id:
            rides = display_rides(rider_id)
            for ride in rides:
                print(f"Ride ID: {ride.id}, Route: {ride.route}, Fare: {ride.fare} KES, Date: {ride.date}, Notes: {ride.notes}, Driver Vibe: {ride.driver_vibe}, Matatu: {ride.matatu_nickname}")
        elif choice == "4" and rider_id:
            route = input("Enter route to search: ")
            rides = find_rides_by_route(rider_id, route)
            for ride in rides:
                print(f"Date: {ride.date}, Fare: {ride.fare} KES, Notes: {ride.notes}, Driver Vibe: {ride.driver_vibe}, Matatu: {ride.matatu_nickname}")
        elif choice == "5" and rider_id:
            avg_fare = analyze_fares(rider_id)
            print(f"Average fare for your routes: {avg_fare:.2f} KES")
        elif choice == "6" and rider_id:
            ride_id = int(input("Enter ride ID to delete: "))
            delete_ride(ride_id)
            print("Ride deleted!")
        elif choice == "7" and rider_id:
            delete_rider(rider_id)
            rider_id = None
            print("Profile wiped! Start fresh anytime.")
        elif choice == "8" and rider_id:
            traffic_routes, suggestions = check_traffic_alerts(rider_id)
            if traffic_routes:
                print("Watch out! Traffic reported on these routes:", ", ".join(traffic_routes))
                for route, alt in suggestions.items():
                    print(f"Alternative for {route}: {alt}")
            else:
                print("No traffic alerts today. Safe travels!")
        elif choice == "0":
            print("Sawa! Thanks for riding with us.")
            break
        else:
            print("Hapana! Pick a valid option or create a profile first.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()