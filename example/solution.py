import csv
import sys
import datetime

#bags = 1

data_file = './example/example.csv'
ticket_origin = 'WIW'
ticket_destination = 'RFS'
route = []

"""Helper function for converting datetime string to the datetime object."""


def parseToDate(dateString):
    return datetime.datetime.strptime(dateString, "%Y-%m-%dT%H:%M:%S")


"""Imports a source csv file and converts it to the list of dictionaries.
"""


def importFlightsFromCSV(data_file):
    flights = []
    with open(data_file, mode='r') as infile:
        reader = csv.reader(infile)
        headings = next(reader)
        for row in reader:
            flight = {}
            flight['flight_no'] = row[0]
            flight['origin'] = row[1]
            flight['destination'] = row[2]
            flight['departure'] = parseToDate(row[3])
            flight['arrival'] = parseToDate(row[4])
            flight['base_price'] = float(row[5])
            flight['bag_price'] = float(row[6])
            flight['bag_allowed'] = int(row[6])
            flights.append(flight)
    return flights


"""This function iterates over the list of all flights and searches for the flight combinations from the origin to destination airport. """


def flight_search(flight_origin, flight_destination, flights):
    for flight in flights:
        # the direct flight origin -> destination
        if flight['origin'] == flight_origin and flight['destination'] == flight_destination and not route:
            route.append(flight)
            flights.remove(flight)
            return route

        # the indirect flight to destination
        if flight['origin'] == flight_origin and flight['destination'] == flight_destination and route:
            layover = flight['departure'] - route[-1]['arrival']
            if layover > datetime.timedelta(hours=1) and layover < datetime.timedelta(hours=6):
                route.append(flight)
                flights.remove(flight)
                return route

        # the indirect flight from origin
        elif flight['origin'] == flight_origin and not route:
            route.append(flight)
            flights.remove(flight)
            flight_search(flight['destination'],
                          flight_destination, flights)

        # the indirect flight
        elif flight['origin'] == flight_origin:
            layover = flight['departure'] - route[-1]['arrival']
            if layover > datetime.timedelta(hours=1) and layover < datetime.timedelta(hours=6):
                route.append(flight)
                flights.remove(flight)
                flight_search(flight['destination'],
                              flight_destination, flights)

        # no path from origin to destination
        elif route:
            route.clear()
            return "No such flight with a given paramaters."


flights = importFlightsFromCSV(data_file)
flight_search(ticket_origin, ticket_destination, flights)
print(route)
