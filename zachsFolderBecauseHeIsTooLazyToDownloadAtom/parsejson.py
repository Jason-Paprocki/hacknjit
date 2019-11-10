from decimal import Decimal
from pprint import pprint
import json
from MapPoint import MapPoint

'''
Given file name, returns a tuple T such that
T[0] is a list of tuples of the lat and long of start(direction1),
lat and long of start(direction2), and lat and long of ending point(direction3)
T[1] is a list of tuples of length 3, with the lat and long as first 2 ele
distance on that as 3rd
'''
def parse_json_for_turns(filename):
    # dictionary, in is tuple (lat, long) : key distance(miles)
    location_distance = []
    start_and_end = []
    visit_distance = False

    with open(filename, 'r') as in_file:
        #word_list = in_file.read().split(' ')
        #lat=long=0.0

        parsed_json = json.load(in_file)
        steps_list = parsed_json[0]['legs'][0]['steps']


        turning_points = []
        #iterate over steps_list and add each step as a MapPoint
        #object to the turning_points list
        for i in steps_list:
            s_lat = i["start_location"]["lat"]
            s_lng = i["start_location"]["lng"]
            dist_string = i["distance"]["text"]
            true_dist_in_miles = parseDistanceToMiles(dist_string)
            s_point = MapPoint(s_lat, s_lng, true_dist_in_miles)
            turning_points.append(s_point)

        #grab pointA and pointB
        pointA_lat = parsed_json[0]['legs'][0]['start_location']['lat']
        pointA_lng = parsed_json[0]['legs'][0]['start_location']['lng']
        pointB_lat = parsed_json[0]['legs'][0]['end_location']['lat']
        pointB_lng = parsed_json[0]['legs'][0]['end_location']['lng']
        pointA = MapPoint(pointA_lat, pointA_lng, 0)
        pointB = MapPoint(pointB_lat, pointB_lng, 0)

        return [(pointA, pointB), turning_points]

        #old code
        """
            if (word == '{"lat":'):
                lat =  format(float(each_word[i+1].strip(',')),  '.f')
                long = format(float(each_word[i+3].strip('},')), '.f')
                if (len(start_and_end) != 3):
                    start_and_end.append((lat, long))
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
        return (start_and_end, location_distance)
        """

def parseDistanceToMiles(dist_string):
    #separate dist_string
    dist_elements = dist_string.split(' ')

    #grab magnitude and units
    mag = float(dist_elements[0])
    unit = dist_elements[-1]

    #convert to miles
    if (unit == 'ft'):
        return format(mag / 5280.0, '.2f')
    elif (unit == 'mi'):
        return format(mag, '.2f')
    else:
        raise NameError('Expected unit in ft/mi')
    return None

#pprint(parse('metadata_dump.json')) # test case

data_from_route = parse_json_for_turns('metadata_dump.json')
#Print: (Point A, Point B)
print("(" + str(data_from_route[0][0]) + ", ", end='')
print(str(data_from_route[0][1]) + ")")

#Print: List of turns
print()
for turn in data_from_route[1]:
    print(turn)
