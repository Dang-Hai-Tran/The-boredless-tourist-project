destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destinations_index(destination):
    for item in destinations:
        if item == destination:
            index = destinations.index(item)
            return index
# print(get_destinations_index(destination="Los Angeles, USA"))
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destinations_index(traveler_destination)
    return traveler_destination_index

# test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)
attractions = []
for destination in destinations:
    attractions.append([])
# print(attraction)

def add_attraction(destination, attraction):
    try:
        destination_index = get_destinations_index(destination)
        attraction_for_destination = attractions[destination_index].append(attraction)
        
    except ValueError:
        return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
# print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
# print(attractions)

def find_attractions(destination, interests):
    destination_index = get_destinations_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for item in attractions_in_city:
        possible_attraction = item
        attraction_tags = item[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

# print(find_attractions("Los Angeles, USA", ["art"]))
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interest_string = "Hi "+ traveler[0] + " we think you 'll like these places around "+ traveler_destination +": "
    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1] == traveler_attractions[i]:
            interest_string += "the" + traveler_attractions[i] + "."
        else:
            interest_string += "the" + traveler_attractions[i] + ","
    print(interest_string)

# get_attractions_for_traveler(test_traveler)
        
    




