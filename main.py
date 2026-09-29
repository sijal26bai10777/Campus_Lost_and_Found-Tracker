from lost import add_lost_item, show_lost_items
from found import add_found_item, show_found_items
from search import search_items
from match import find_matches



def main():

    # Lists for lost items
    lost_names = []
    lost_locations = []
    lost_dates = []
    lost_descriptions = []

    # Lists for found items
    found_names = []
    found_locations = []
    found_dates = []
    found_descriptions = []

    while True:

        print("\n======================================")
        print("       CAMPUS LOST & FOUND TRACKER")
        print("======================================")
        print("1. Report Lost Item")
        print("2. Report Found Item")
        print("3. View Lost Items")
        print("4. View Found Items")
        print("5. Search for an Item")
        print("6. Find Possible Matches")
        print("7. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_lost_item(
                lost_names,
                lost_locations,
                lost_dates,
                lost_descriptions
            )

        elif choice == "2":

            add_found_item(
                found_names,
                found_locations,
                found_dates,
                found_descriptions
            )

        elif choice == "3":

            show_lost_items(
                lost_names,
                lost_locations,
                lost_dates,
                lost_descriptions
            )

        elif choice == "4":

            show_found_items(
                found_names,
                found_locations,
                found_dates,
                found_descriptions
            )

        elif choice == "5":

            search_items(
                lost_names,
                lost_locations,
                lost_dates,
                lost_descriptions,
                found_names,
                found_locations,
                found_dates,
                found_descriptions
            )

        elif choice == "6":

            find_matches(
                lost_names,
                lost_locations,
                lost_dates,
                lost_descriptions,
                found_names,
                found_locations,
                found_dates,
                found_descriptions
            )

        elif choice == "7":

            print("\nThank you for using Campus Lost & Found Tracker!")
            break

        else:

            print("\nInvalid choice.")
            print("Please enter a number from 1 to 7.")


main()
