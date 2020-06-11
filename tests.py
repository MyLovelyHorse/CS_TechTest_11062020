import get_london_users


def test_get_all_users_has_length_1000():
    test_json = get_london_users.get_all_users()
    size = len(test_json)
    assert size == 1000


def test_get_users_by_city():
    expected = [
        {
            "id": 135,
            "first_name": "Mechelle",
            "last_name": "Boam",
            "email": "mboam3q@thetimes.co.uk",
            "ip_address": "113.71.242.187",
            "latitude": -6.5115909,
            "longitude": 105.652983,
        },
        {
            "id": 396,
            "first_name": "Terry",
            "last_name": "Stowgill",
            "email": "tstowgillaz@webeden.co.uk",
            "ip_address": "143.190.50.240",
            "latitude": -6.7098551,
            "longitude": 111.3479498,
        },
        {
            "id": 520,
            "first_name": "Andrew",
            "last_name": "Seabrocke",
            "email": "aseabrockeef@indiegogo.com",
            "ip_address": "28.146.197.176",
            "latitude": "27.69417",
            "longitude": "109.73583",
        },
        {
            "id": 658,
            "first_name": "Stephen",
            "last_name": "Mapstone",
            "email": "smapstonei9@bandcamp.com",
            "ip_address": "187.79.141.124",
            "latitude": -8.1844859,
            "longitude": 113.6680747,
        },
        {
            "id": 688,
            "first_name": "Tiffi",
            "last_name": "Colbertson",
            "email": "tcolbertsonj3@vimeo.com",
            "ip_address": "141.49.93.0",
            "latitude": 37.13,
            "longitude": -84.08,
        },
        {
            "id": 794,
            "first_name": "Katee",
            "last_name": "Gopsall",
            "email": "kgopsallm1@cam.ac.uk",
            "ip_address": "203.138.133.164",
            "latitude": 5.7204203,
            "longitude": 10.901604,
        },
    ]
    result = get_london_users.get_users_by_city("London")
    assert result == expected


def test_get_user_by_id():
    expected = {
        "id": 135,
        "first_name": "Mechelle",
        "last_name": "Boam",
        "email": "mboam3q@thetimes.co.uk",
        "ip_address": "113.71.242.187",
        "latitude": -6.5115909,
        "longitude": 105.652983,
        "city": "London",
    }
    result = get_london_users.get_user_by_id(135)
    assert result == expected


def test_haversine_distance_between_two_points():
    # Test case is London to Manchester.
    london_coords = [{"lat": 51.50853, "long": -0.12574}]
    manchester_coords = [{"lat": 53.48095, "long": -2.23743}]
    lat1 = london_coords[0]["lat"]
    lat1 = float(lat1)
    lon1 = london_coords[0]["long"]
    lon1 = float(lon1)
    lat2 = manchester_coords[0]["lat"]
    lat2 = float(lat2)
    lon2 = manchester_coords[0]["long"]
    lon2 = float(lon2)

    dist = get_london_users.haversine(lat1, lon1, lat2, lon2)

    assert round(dist, 2) == 321.27  # distance in km

def test_get_users_by_distance_from_london():
    result = get_london_users.get_users_by_distance_from_london(200)
    expected = [
        {
            "id": 266,
            "first_name": "Ancell",
            "last_name": "Garnsworthy",
            "email": "agarnsworthy7d@seattletimes.com",
            "ip_address": "67.4.69.137",
            "latitude": 51.6553959,
            "longitude": 0.0572553,
        },
        {
            "id": 322,
            "first_name": "Hugo",
            "last_name": "Lynd",
            "email": "hlynd8x@merriam-webster.com",
            "ip_address": "109.0.153.166",
            "latitude": 51.6710832,
            "longitude": 0.8078532,
        },
        {
            "id": 554,
            "first_name": "Phyllys",
            "last_name": "Hebbs",
            "email": "phebbsfd@umn.edu",
            "ip_address": "100.89.186.13",
            "latitude": 51.5489435,
            "longitude": 0.3860497,
        },
        {
            "id": 577,
            "first_name": "Fernande",
            "last_name": "Flips",
            "email": "fflipsg0@washingtonpost.com",
            "ip_address": "249.52.132.144",
            "latitude": 49.6355347,
            "longitude": -1.6272462,
        },
    ]

    assert result == expected
