import requests

def make_post():

    data = {"first_name": "Cole", "last_name": "Vertikoff", "netid": "crv9", "github_username": "vertikoff", "team_name": "OlderThanYou"}
    r = requests.post("http://bme590.suyash.io/student", json=data)
    site_array = r.json() # parses the JSON response from the GET request into a python entity (in this case an array)
    return site_array


make_post()
