import requests

# Pokémon API URL
POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_data(pokemon_name):
    try:
        response = requests.get(f"{POKEMON_API_URL}{pokemon_name.lower()}")
        response.raise_for_status()
        pokemon_data = response.json()
        return pokemon_data
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        return None


def display_pokemon_details(pokemon_data):
    if pokemon_data:
        print(f"Name: {pokemon_data['name'].capitalize()}")
        print(f"ID: {pokemon_data['id']}")
        print("Abilities:")
        for ability in pokemon_data['abilities']:
            print(f"  - {ability['ability']['name'].capitalize()}")
        print(f"Height: {pokemon_data['height'] / 10} m")
        print(f"Weight: {pokemon_data['weight'] / 10} kg")
    else:
        print("Pokemon not found!")


def main():
    print("Welcome to the Pokémon CLI Game!")

    while True:
        print("\nEnter a Pokémon name (or 'q' to quit):")
        user_input = input().lower()

        if user_input == 'q':
            print("Thanks for playing!")
            break

        pokemon_data = get_pokemon_data(user_input)
        display_pokemon_details(pokemon_data)


if __name__ == "__main__":
    main()