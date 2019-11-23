# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
import csv

class City():
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

# REMEMBER to add relative path !!!!
path_name = 'src/cityreader/cities.csv'

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open(path_name, 'r', newline = '') as csv_file:
    read_file = csv.DictReader(csv_file)
    for row in read_file:
          city = City(row['city'], float(row['lat']), float(row['lng']))
          cities.append(city)

  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c.name, c.lat, c.lon)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
print(f'STRETCH GOAL: list out cities that are within coordinates')

prompt = "Enter 2 pairs of latitude & longitude separated by commas\n"
prompt += "The pairs should be diagonal coordinates in the format below:\n"
prompt += "\t    lat1, long1, lat2, long2 "
prompt += "\n\t example: 32, -120, 45, -100\n enter values: "

user_input = (input(prompt))

coordinate_pairs = user_input.split(",")

# can't do this
#def cityreader_stretch(lat1 = float(lat1), lon1 = float(lat2), lat2 = float(lat2), lon2 = float(lon2), cities=[]):
def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  lat1 = float(lat1)
  lat2 = float(lat2)
  lon1 = float(lon1)
  lon2 = float(lon2)

  lat_pair = []
  lon_pair = []


  if(lat1 < lat2):
    lat_pair = [lat2, lat1]
  else:
    lat_pair = [lat1, lat2]

  if(lon1 < lon2):
    lon_pair = [lon2, lon1]
  else:
    lon_pair = [lon1, lon2]    

  print(f' lat_pair -> {lat_pair}\n')
  print(f' lon_pair -> {lon_pair}\n')

  # TODO Ensure that the lat and lon values are all floats            # fixed typo
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  within = [city for city in cities if city.lat < lat_pair[0] and city.lat > lat_pair[1] and city.lon < lon_pair[0] and city.lon > lon_pair[1]]

  if(len(within) >=1):
    return within
  else:
    print(f'There are no cities within these diagonal coordinates')  


cities_result = cityreader_stretch(*coordinate_pairs, cities)

if(cities_result != None):
  for city in cities_result:
    print(city.name, city.lat, city.lon)


# 45, -100, 32, -120