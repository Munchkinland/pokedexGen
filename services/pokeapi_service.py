import requests

class PokeAPIService:
    BASE_URL = "https://pokeapi.co/api/v2/"

    @staticmethod
    def get_pokemon_data(pokemon_name):
        response = requests.get(f"{PokeAPIService.BASE_URL}/pokemon/{pokemon_name.lower()}")
        if response.status_code == 200:
            return response.json()
        return None