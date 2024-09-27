import json
from unicodedata import name
import requests
from pprint import PrettyPrinter
from bs4 import BeautifulSoup
import pprint as pp 
   
# Making a GET request 
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
if response.status_code == 200:
    data = response.json()
    # Process the data here
else:
    print(f"Failed to retrieve data: {response.status_code}")
#access Pokémon abilities
name = data['name']
abilities = [ability['ability']['name'] for ability in data['abilities']]
print(f"Name: {name}")
print(f"Abilities: {', '.join(abilities)}")
#Create a function to fetch Pokémon data, pass the Pokémon name dynamically, and return the JSON response:
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}")
        return None
#Calculating Average Weight:
def calculate_average_weight(pokemon_list):
    weights = [pokemon['weight'] for pokemon in pokemon_list]
    return sum(weights) / len(weights)
#Create a list of Pokémon names, fetch their data, and then calculate the average weight:
pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

# Print names and abilities
for pokemon in pokemon_data:
    name = pokemon['name']
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print(f"Name: {name}, Abilities: {', '.join(abilities)}")

# Calculate and print average weight
average_weight = calculate_average_weight(pokemon_data)
print(f"Average Weight: {average_weight}")
#Fetching Planet Data:Here's how to properly extract planet information:
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_data = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if planet['mass'] else "Unknown"
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else "Unknown"
            planet_data.append((name, mass, orbit_period))
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

    return planet_data
#Finding the Heaviest Planet:You can modify your function to find the heaviest planet as follows:
def find_heaviest_planet(planets):
    return max(planets, key=lambda planet: planet[1] if planet[1] != "Unknown" else 0)

planets = fetch_planet_data()
name, mass, _ = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
