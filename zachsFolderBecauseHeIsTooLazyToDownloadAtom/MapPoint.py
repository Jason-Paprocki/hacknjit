class MapPoint:
    #constructor for turn MapPoints
    def __init__(self, lat=0.0, lng=0.0, dist_to_next=0.0, address=""):
        self.lat = lat
        self.lng = lng
        self.dist_to_next = dist_to_next
        self.lat_str = format(lat, '.15f')
        self.lng_str = format(lng, '.15f')
        self.dist_to_next_str = format(float(dist_to_next), '.4f')

        #some address was specified at instantiation
        if address != "":
            self.address = address
        else: #build address from lat, lng
            self.address = reverse_geocode()

    #constructor for pointA and pointB
    def __init__(self, lat=0.0, lng=0.0):
        self.lat = lat
        self.lng = lng
        self.lat_str = format(lat, '.15f')
        self.lng_str = format(lng, '.15f')

    #construct MapPoint given a literal address
    def geocode(address):
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        payload = {"key" : key,
                   "input" : address,
                   "inputtype" : textquery,
                   "fields" : "geometry"}
        response = requests.get(url, params=payload)
        parsed_json = json.load(response)
        location = parsed_json["candidates"][0]["geometry"]["location"]

        self.lat = location["lat"]
        self.lng = location["lng"]


    def __str__(self):
        string = "(" + self.lat_str + ", " + self.lng_str + "), "

        if self.dist_to_next_str != None:
            string += self.dist_to_next_str

        return string

    #Calculate and return euclidean midpoint
    def eucl_midpoint_between(self, o):
        x = (self.lat + o.lat) / 2.0
        y = (self.lng + o.lng) / 2.0
        return MapPoint(x, y)

    #reverse geocode an address and get a pair of (lat, lng) coords
    def reverse_geocode(self):
        gmap = googlemaps.Client(key='AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk')
        return str(gmap.reverse_geocode((self.lat, self.lng)))

    #format (lat, lng) appropriately for urls
    def get_lat_lng_str(self):
        return self.lat_str + "," + self.lng_str
