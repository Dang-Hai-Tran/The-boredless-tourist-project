destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
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
