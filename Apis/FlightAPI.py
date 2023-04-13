def flightapi():
    lat = 0.0
    long = 0.0
    distance = 0.0
    fuel = 0.0
    destination = ""

    return {
        "latitude": lat,
        "longitude": long,
        "distance": distance,
        "fuel": fuel,
        "destination": destination,
    }


def main():
    flightapi()


if __name__ == "__main__":
    main()
