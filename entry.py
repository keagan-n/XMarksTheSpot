
# Entry is an object that holds information about each
# attraction/image

import requests



class Entry:
    def __init__(self, placename='', location='', image='', description=''):
        self.placename = placename
        # maybe like city name
        self.location = location
        self.image = image
        self.description = description
        # maybe needed to display on google map
        # self.coordinate = (latitude, longitude)

    def __str__ (self):
        return "{} {} {}".format(self.placename, self.location, self.description)


    def coordinates(self):
        try:
            address = self.location
            url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
                .format(address.replace(' ','+'), 'AIzaSyDQe5G3tqd5Vfwefn7w3Djrv1L1bmlKkTw'))

            response = requests.get(url)
            resp_json_payload = response.json()
            lat = resp_json_payload['results'][0]['geometry']['location']['lat']
            lng = resp_json_payload['results'][0]['geometry']['location']['lng']
            return lat, lng
        except Exception as e:
            print(e)

    def returnPlaceLocationTuple(self):
        return (self.placename, self.location)

if __name__ == '__main__':
    entry = Entry(location='10201 Malinda Ln, Garden Grove CA, 92840')
    print(entry.coordinates())
        
        
