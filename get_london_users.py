"""
London coordinates:
(taken from https://latitudelongitude.org/gb/london/)
51.50853, -0.12574
"""
import requests

from math import radians, cos, sin, asin, sqrt

base_url="https://bpdts-test-app.herokuapp.com/"

def get_all_users():
    """Return all users."""
    r = requests.get(base_url + "/users")
    users = r.json()
    return users

def get_users_by_city(city_name):
    """Return all users located in a particular city."""
    r = requests.get(base_url + "/city/"+ city_name + "/users")
    users = r.json()
    return users

def get_user_by_id(id):
    """Return users specified by ID."""
    r = requests.get(base_url + "/user/" + str(id))
    user = r.json()
    return user

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points on the earth
    (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return c * r

def get_users_by_distance_from_london(distance_in_miles):
    """
    Use the Haversine formula to determine whether users are within a
    specified radius of London. We could generalise this by giving the
    coordinates as a function parameter but in this case we are only looking
    at distance from London.
    """
    users = get_all_users()
    london_coords = [{"lat": 51.50853, "long": -0.12574}] # hardcoded here
    distance_in_km = distance_in_miles * 1.609
    users_to_return = []
    for usr in users:
        position_coords = [{"lat": usr["latitude"], "long": usr["longitude"]}]
        lat1 = london_coords[0]["lat"]
        lat1 = float(lat1)
        lon1 = london_coords[0]["long"]
        lon1 = float(lon1)
        lat2 = position_coords[0]["lat"]
        lat2 = float(lat2)
        lon2 = position_coords[0]["long"]
        lon2 = float(lon2)

        dist = haversine(lat1, lon1, lat2, lon2)

        if dist < distance_in_km:
            users_to_return.append(usr)

    return users_to_return

def display_users_nicely(users):
    for usr in users:
        first = usr["first_name"]
        last = usr["last_name"]
        to_print = first + " " + last
        print(to_print)

print("Users located in London:")
display_users_nicely(get_users_by_city("London"))

print("Users located within 50 miles of London:")
display_users_nicely(get_users_by_distance_from_london(50))
