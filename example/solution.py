import csv
import sys

#bags = 1
print(str(sys.argv))


data_file = sys.argv[1]
origin = sys.argv[2]
destination = sys.argv[3]

# import csv file and convert it to the list of dictionaries
with open(data_file, mode='r') as infile:
    reader = csv.reader(infile)
    headings = next(reader)
    all_flights = []

    for row in reader:
        flight = {}
        for i in range(len(row)):
            flight[headings[i]] = row[i]
        all_flights.append(flight)

route = []


def flight_search(ori, dest):
    for flight in all_flights:
        if flight['origin'] == ori and flight['destination'] == dest:
            route.append(flight)
            all_flights.remove(flight)
            return

        elif flight['origin'] == ori:
            route.append(flight)
            all_flights.remove(flight)

            flight_search(flight['destination'], dest)

        else:
            route.clear()
            return "No such flight with a given paramaters."


flight_search(origin, destination)
print(route)
# print(all_flights)
