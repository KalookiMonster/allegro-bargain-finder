import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

class AllegroAPI:
    AUTH_URL = 'https://allegro.pl/auth/oauth/token'
    API_URL = 'https://api.allegro.pl'

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self.get_token()

    def get_token(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url=self.AUTH_URL, client_id=self.client_id, client_secret=self.client_secret)
        return token

    def search_items(self, phrase, limit=20):
        headers = {
            'Authorization': f"Bearer {self.token['access_token']}",
            'Accept': 'application/vnd.allegro.public.v1+json'
        }
        params = {
            'phrase': phrase,
            'limit': limit
        }
        response = requests.get(f"{self.API_URL}/offers/listing", headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        items = []
        for item in data.get('items', {}).get('regular', []):
            price = float(item['sellingMode']['price']['amount'])
            title = item['name']
            url = item['external']['url']
            items.append({'title': title, 'price': price, 'url': url})
        return items
