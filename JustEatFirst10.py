import requests
import json
import sys

def get_restaurant_data(postcode):
    url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{}".format(postcode)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data.get("restaurants")[:10] # Return only the first 10 restaurants
    else:
        print("Error fetching data:", response.status_code)
        return None

postcode = sys.argv[1] # User passes desired postcode
restaurant_data = get_restaurant_data(postcode)

if restaurant_data:
    for restaurant in restaurant_data:
        cuisines = ""
        print("Name: "+restaurant.get("name"))
        for cuisine in restaurant.get("cuisines"):
            cuisines += cuisine.get("name")+","
        if cuisines.endswith(","):
            cuisines = cuisines[:-1]
        print("Cuisines: "+cuisines)
        print("Rating: "+str(restaurant.get("rating").get("starRating"))+"/5")
        print("Address: "+restaurant.get("address").get("firstLine")+","+restaurant.get("address").get("city")+","+restaurant.get("address").get("postalCode"))
        print("")
else:
    print("Failed to fetch restaurant data.")