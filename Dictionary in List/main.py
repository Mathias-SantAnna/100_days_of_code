country = input(f"\nEnter a country name: ")  # Add country name
visits = int(input(f"Enter number of visits: "))  # Number of visits
list_of_cities = input("Enter cities visited (comma-separated): ").split(",")  # Create list from formatted string
list_of_cities = [city.strip() for city in list_of_cities]  # Strip extra spaces

travel_log = [
    {
        "country": "Brazil",
        "visits": 10,
        "cities": ["São Paulo", "Rio de Janeiro", "Salvador"]
    },
    {
        "country": "Brazil",
        "visits": 4,
        "cities": ["Brasília", "Curitiba", "Florianópolis"]
    },
]

# Add a new country to the travel log
def add_new_country(name, times_visited, cities_visited):
    new_country = {
        "country": name,
        "visits": times_visited,
        "cities": cities_visited
    }
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)

print(f"\nI've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")