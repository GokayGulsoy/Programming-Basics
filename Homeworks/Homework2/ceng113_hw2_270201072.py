path = "provinces.txt"
infile = open(path ,'r')
dictionary = {}
i = 0
while i <81:
  a = infile.readline()
  a = a.split(',')
  dictionary[a[0]] = a[1] + ',' + a[2][:-1]
  dictionary[a[0]] = dictionary[a[0]].split(',')
  i += 1


departure = 'x'
while departure not in dictionary:
    departure = input("Departure province:")
    departure = departure.upper()
    if departure in dictionary:
        pass
    elif departure == 'W' or departure == 'Q' or departure == 'X':
        print("Province not found!")
    else:
        print("province not found!")
        b = dictionary.keys()
        b = list(b)
        list1 = []
        i = 0

        while i < 80:
            if (departure == b[i][0]) or (departure == b[i][0] + b[i][1]) or (
                    departure[:3] == b[i][0] + b[i][1] + b[i][2]):
                list1.append(b[i])
                i += 1
            else:
                i += 1


        list1 = tuple(list1)
        m = sorted(list1)

        sep = ','
        m = sep.join(m)
        print(f"Possible provinces:{m}")

###########################################################################

arrival = 'x'
while arrival not in dictionary:
    arrival = input("Arrival province:")
    arrival = arrival.upper()
    if arrival in dictionary:
        if arrival == departure:
            print("Enter a different province!")
            arrival = 'x'
    elif arrival == 'W' or arrival == 'Q' or arrival == 'X':
        print("Province not found!")
    else:
        print("province not found!")
        b = dictionary.keys()
        b = list(b)
        print(b)
        list2 = []
        i = 0

        while i < 80:
            if (arrival == b[i][0]) or (arrival == b[i][0] + b[i][1]) or (
                    arrival[:3] == b[i][0] + b[i][1] + b[i][2]):
                list2.append(b[i])
                i += 1
            else:
                i += 1

        print(list2)
        list1 = tuple(list2)
        m = sorted(list2)
        print(m)

        sep = ','
        m = sep.join(m)
        print(m)
        print(f"Possible provinces:{m}")

####################################################

travel_type = input("Enter travel type:")
travel_type = travel_type.upper()

while travel_type != 'CAR' and travel_type != 'MOTORCYCLE' and travel_type != 'BICYCLE':
    travel_type = input("Enter travel type:")
    travel_type = travel_type.upper()

print(travel_type)

#############################################################################
speed = 0
if travel_type == 'CAR':
    speed = 90
if travel_type == 'MOTORCYCLE':
    speed = 80
if travel_type == 'BICYCLE':
    speed =25

x1 = float(dictionary[departure][0])
x2 = float(dictionary[arrival][0])

y1 = float(dictionary[departure][1])
y2 = float(dictionary[arrival][1])

dx = x2-x1
dy = y2-y1
distance = dx**2 + dy**2

square_root = 1/2
distance = distance**square_root
distance_km = distance*100
distance_km_int_part = int(distance_km)
float_part = distance_km - distance_km_int_part
float_part = float_part + 1/100
float_part = str(float_part)
float_part = float(float_part[:4])
distance_km = distance_km_int_part + float_part
print(f"I am calculating the distance between {departure} and {arrival} ...")
print(f"Distance:{distance_km} km")
#######################################################
time = distance_km / speed
hours = int(time)
minutes = (time - hours)*60
minutes = int(minutes)
print(f"Approximate travel time with {travel_type}:{hours} hours {minutes} minutes")
##################################################################################
items = list(dictionary.items())
list_closest = []
i = 0
while i <81:
   closest_x = float(items[i][1][0])
   closest_y = float(items[i][1][1])
   closest_distance = (closest_x -x1)**2 + (closest_y -y1)**2
   closest_distance = closest_distance**square_root
   closest_distance_km = closest_distance*100
   if closest_distance_km == 0:
       i += 1
   else:
       list_closest.append(int(closest_distance_km))
       i += 1

key = list(dictionary.keys())

closest_places_list = []
#print(list_closest)
#######################################

#print(min(list_closest))
n = 0
for i in key:
    n += 1
    if i == departure:
        del key[n-1]

distance_city = dict(zip(key,list_closest))
closest_places = []

n = min(list_closest)
k = 0
for i in distance_city:
    k += 1
    if distance_city[i] == n:
        closest_places.append(i)
        del distance_city[i]
        del list_closest[k-1]
        break


n = min(list_closest)
k = 0
for i in distance_city:
    k += 1
    if distance_city[i] == n:
        closest_places.append(i)
        del distance_city[i]
        del list_closest[k-1]
        break



n = min(list_closest)
k = 0
for i in distance_city:
    k += 1
    if distance_city[i] == n:
        closest_places.append(i)
        del distance_city[i]
        del list_closest[k-1]
        break

print(closest_places)
closest_places = sorted(closest_places)
sep = ','
closest_places = sep.join(closest_places)
print(f"Recommended places close to {departure}:{closest_places}")