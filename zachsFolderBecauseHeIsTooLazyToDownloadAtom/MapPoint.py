class MapPoint:
    def __init__(self, lat=0.0, lng=0.0, dist_to_next=0.0):
        self.lat = lat
        self.lng = lng
        self.dist_to_next = dist_to_next
        self.lat_str = format(lat, '.15f')
        self.lng_str = format(lng, '.15f')
        self.dist_to_next_str = format(float(dist_to_next), '.4f')

    def __init__(self, lat=0.0, lng=0.0):
        self.lat = lat
        self.lng = lng
        self.lat_str = format(lat, '.15f')
        self.lng_str = format(lng, '.15f')

    def __str__(self):
        string = "(" + self.lat_str + ", " + self.lng_str + "), "

        if self.dist_to_next_str != None:
            string += self.dist_to_next_str

        return string

    def eucl_midpoint_between(self, o):
        #Calculate and return euclidean midpoint
        x = (self.lat + o.lat) / 2.0
        y = (self.lng + o.lng) / 2.0
        return MapPoint(x, y)
