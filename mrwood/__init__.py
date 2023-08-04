import secrets

import requests

from . import exceptions
from . import proof


class MrWood:
    def __init__(self, proxy: str = None):
        self.session = requests.Session()

        if proxy:
            self.session.proxies = {
                "https": f"http://{proxy}",
                "http": f"http://{proxy}"
            }

        self.session.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'application-type': 'application/json',
            'content-type': 'application/json',
            'origin': 'https://vantage.rip',
            'referer': 'https://vantage.rip/',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }

        self.email = secrets.token_hex(16) + "@gmail.com"
        self.password = secrets.token_hex(16)

    def create_account(self):
        data = self.session.post(
            'https://api.vantage.rip/auth/register',
            json={
                'username': secrets.token_hex(8),
                'password': self.password,
                'captcha': proof.get_proof(),
                'email': self.email,
            }
        )
        if data.status_code != 200:
            raise exceptions.WoodHTTPException(f"Failed to register account: {data.json()['msg']}")

