from display import display_item


def add_lost_item(names, locations, dates, descriptions):

    print("\n========== REPORT LOST ITEM ==========")

    name = input("Enter item name: ")
    location = input("Enter location where it was lost: ")
    date = input("Enter date: ")
    description = input("Enter description: ")

    names.append(name)
    locations.append(location)
    dates.append(date)
    descriptions.append(description)

    print("\nLost item added successfully.")


def show_lost_items(names, locations, dates, descriptions):

    print("\n========== LOST ITEMS ==========")

    if len(names) == 0:
        print("No lost items have been reported.")
        return

    for i in range(len(names)):

        display_item(
            i + 1,
            names[i],
            locations[i],
            dates[i],
            descriptions[i]
        )