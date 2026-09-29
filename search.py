from display import display_item


def search_items(
    lost_names,
    lost_locations,
    lost_dates,
    lost_descriptions,
    found_names,
    found_locations,
    found_dates,
    found_descriptions
):

    print("\n========== SEARCH ITEM ==========")

    search_name = input("Enter item name to search: ")

    found = False

    # Search in lost items
    for i in range(len(lost_names)):

        if lost_names[i].lower() == search_name.lower():

            print("\nLost Item Found:")

            display_item(
                i + 1,
                lost_names[i],
                lost_locations[i],
                lost_dates[i],
                lost_descriptions[i]
            )

            found = True

    # Search in found items
    for i in range(len(found_names)):

        if found_names[i].lower() == search_name.lower():

            print("\nFound Item Found:")

            display_item(
                i + 1,
                found_names[i],
                found_locations[i],
                found_dates[i],
                found_descriptions[i]
            )

            found = True

    if found == False:
        print("\nNo item with that name was found.")