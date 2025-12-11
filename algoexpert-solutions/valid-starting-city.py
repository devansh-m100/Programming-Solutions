# Algoexpert problem link - https://www.algoexpert.io/questions/valid-starting-city

# O(n) time | O(1) space, where n is the number of cities

def validStartingCity(distances, fuel, mpg):
    miles_left_with_excess_fuel = 0

    min_miles_to_cover_using_left_fuel_to_starting_city = 0
    starting_city_idx = 0

    for i in range(1, len(distances)):
        dist_betn_curr_and_prev_city = distances[i-1]
        miles_left_with_excess_fuel += mpg * fuel[i-1] - dist_betn_curr_and_prev_city
        if miles_left_with_excess_fuel < min_miles_to_cover_using_left_fuel_to_starting_city:
            min_miles_to_cover_using_left_fuel_to_starting_city = miles_left_with_excess_fuel
            starting_city_idx = i
    return starting_city_idx
