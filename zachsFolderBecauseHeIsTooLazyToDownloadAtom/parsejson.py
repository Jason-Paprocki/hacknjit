from decimal import Decimal

'''
Given file name, returns a tuple T such that
T[0] is a list of tuples of the lat and long of start(direction1),
lat and long of start(direction2), and lat and long of ending point(direction3)
T[1] is a list of tuples of length 3, with the lat and long as first 2 ele
distance on that as 3rd
'''
def parse(filename):
    # dictionary, in is tuple (lat, long) : key distance(miles)
    location_distance = []
    startandend = []
    visitDistance = False
    with open(filename, 'r') as ifile:
        each_word = ifile.read().split(' ')
        lat=long=0.0
        for i in range(len(each_word)):
            word = each_word[i]
            if (word == '{"lat":'):
                lat = float(each_word[i+1].strip(','))
                long = float(each_word[i+3].strip('},'))
                if (len(startandend) != 3):
                    startandend.append((lat, long))
                else:
                    visitDistance = True
                continue
            if (visitDistance):
                if (word == '{"text":'):
                    unparsed_distance = each_word[i+1].strip('"')
                    # true distance is in miles
                    trueDistance = parseDistance(unparsed_distance, each_word[i+2].strip('",'))
                    visitDistance = False
                    location_distance.append((lat, long, trueDistance))
    return (startandend, location_distance)
                
def parseDistance(number, unit):
    amount = float(number)
    if (unit == 'ft'):
        return amount / 5280.0
    elif (unit == 'mi'):
        return amount
    else:
        raise NameError('Expected unit in ft/mi')
    return none

print(parse('metadata_dump.json')) # test case
