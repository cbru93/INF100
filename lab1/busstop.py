"""Bus stop."""

def busstop():
    """Print the nearest bus stop number (multiple of 7) for a given house number."""
    your_housenumber = int(input("Husnummer:\n"))

    lower_multiple = (your_housenumber // 7) * 7
    upper_multiple = lower_multiple + 7

    distance_to_lower = your_housenumber - lower_multiple
    distance_to_upper = upper_multiple - your_housenumber

    if distance_to_lower <= distance_to_upper:
        closest_busstop_housenumber = lower_multiple
    else:
        closest_busstop_housenumber = upper_multiple

    print(f"Nærmeste busstopp er ved nummer {closest_busstop_housenumber}")

busstop()
