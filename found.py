from display import display_item


def add_found_item(names, locations, dates, descriptions):

    print("\n========== REPORT FOUND ITEM ==========")

    name = input("Enter item name: ")
    location = input("Enter location where it was found: ")
    date = input("Enter date: ")
    description = input("Enter description: ")

    names.append(name)
    locations.append(location)
    dates.append(date)
    descriptions.append(description)

    print("\nFound item added successfully.")


def show_found_items(names, locations, dates, descriptions):

    print("\n========== FOUND ITEMS ==========")

    if len(names) == 0:
        print("No found items have been reported.")
        return

    for i in range(len(names)):

        display_item(
            i + 1,
            names[i],
            locations[i],
            dates[i],
            descriptions[i]
        )