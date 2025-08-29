def busstop():
    """Print the nearest bus stop number (multiple of 7) for a given house number."""
    your_housenumber = int(input("Hvilken husnummer har du? "))
    closest_busstop_housenumber = your_housenumber // 7 * 7
    print(f"Nærmeste busstopp er ved nummer {closest_busstop_housenumber}")


busstop()
