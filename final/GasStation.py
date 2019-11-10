from MapPoint import MapPoint

class GasStation:
    def __init__(self, address, price):
        self.address = address
        self.price = price
        self.point = MapPoint(address)
    
