import os

import requests


class CockTailApi:
    """Cocktail Api Integration"""
    def __init__(self):
        api_key = os.getenv('COCKTAIL_API_KEY')
        self.api_url = f"https://www.thecocktaildb.com/api/json/v1/{api_key}"

    def get_random_cocktails(self, cocktail_count):
        url = f'{self.api_url}/random.php'
        cocktails = []
        for i in range(0, cocktail_count):
            cocktails.append(requests.get(url).json()["drinks"][0])
        return cocktails

    def get_single_cocktail(self, cocktail_id):
        url = f'{self.api_url}/lookup.php?i={cocktail_id}'
        cocktails = requests.get(url)
        return cocktails.json()

    def get_latest_cocktails(self):
        url = f'{self.api_url}/latest.php'
        cocktails = requests.get(url)
        return cocktails.json()

