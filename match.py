from display import display_item


def find_matches(
    lost_names,
    lost_locations,
    lost_dates,
    lost_descriptions,
    found_names,
    found_locations,
    found_dates,
    found_descriptions
):

    print("\n========== POSSIBLE MATCHES ==========")

    match_found = False

    for i in range(len(lost_names)):

        for j in range(len(found_names)):

            if lost_names[i].lower() == found_names[j].lower():

                print("\nPossible Match Found!")

                print("\nLost Item:")
                display_item(
                    i + 1,
                    lost_names[i],
                    lost_locations[i],
                    lost_dates[i],
                    lost_descriptions[i]
                )

                print("\nFound Item:")
                display_item(
                    j + 1,
                    found_names[j],
                    found_locations[j],
                    found_dates[j],
                    found_descriptions[j]
                )

                match_found = True

    if match_found == False:
        print("\nNo possible matches found.")