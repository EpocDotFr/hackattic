from environs import Env
import requests

requests = requests.Session()


class Challenge:
    CHALLENGES_PROBLEM_URL = 'https://hackattic.com/challenges/{challenge_id}/problem'
    CHALLENGES_SOLVE_URL = 'https://hackattic.com/challenges/{challenge_id}/solve'

    def __init__(self, challenge_id, access_token=None):
        self.challenge_id = challenge_id

        if not access_token:
            env = Env()
            env.read_env()

            self.access_token = env.str('ACCESS_TOKEN')
        else:
            self.access_token = None

    def fetch(self):
        return self.call(
            'GET',
            self.CHALLENGES_PROBLEM_URL.format(challenge_id=self.challenge_id)
        )

    def solve(self, json):
        return self.call(
            'POST',
            self.CHALLENGES_SOLVE_URL.format(challenge_id=self.challenge_id),
            json=json
        )

    def call(self, method, url, json=None):
        params = {
            'access_token': self.access_token,
        }

        response = requests.request(method, url, params=params, json=json)
        response.raise_for_status()

        return response.json()
