import csv
import sys
from datetime import datetime

#bags = 1

data_file = './example/example.csv'
ticket_origin = 'WIW'
ticket_destination = 'RFZ'


# import csv file and convert it to the list of dictionaries
with open(data_file, mode='r') as infile:
    reader = csv.reader(infile)
    headings = next(reader)
    flights = []

    for row in reader:
        flight = {}
        for i in range(len(row)):
            flight[headings[i]] = row[i]
        flights.append(flight)

route = []


def flight_search(current_flight_origin, current_flight_destination):
    for flight in flights:
        if flight['origin'] == current_flight_origin and flight['destination'] == current_flight_destination:
            route.append(flight)
            flights.remove(flight)
            return

        elif flight['origin'] == current_flight_origin and not route:
            route.append(flight)
            flights.remove(flight)

            flight_search(flight['destination'],
                          current_flight_destination)

        elif flight['origin'] == current_flight_origin:

            route.append(flight)
            flights.remove(flight)

            flight_search(flight['destination'],
                          current_flight_destination)

        else:
            route.clear()
            return "No such flight with a given paramaters."


flight_search(ticket_origin, ticket_destination)
print(route)
