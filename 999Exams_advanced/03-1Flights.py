def flights(*args):
    values = list(args)
    dict_for_flights = {}
    while len(values):
        current_destination = values[0]
        if current_destination == "Finish":
            break
        people = values[1]
        if current_destination in dict_for_flights.keys():
            dict_for_flights[current_destination] += people
        else:
            dict_for_flights[current_destination] = people
        values.remove(current_destination)
        values.remove(people)
    return dict_for_flights



print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))