from environs import Env
import requests

requests = requests.Session()

env = Env()
env.read_env()


class Problem:
    PROBLEM_URL = 'https://hackattic.com/challenges/{problem_id}/problem'
    SOLVE_URL = 'https://hackattic.com/challenges/{problem_id}/solve'

    def __init__(self, problem_id, access_token=None):
        self.problem_id = problem_id
        self.access_token = access_token or env.str('ACCESS_TOKEN')

    def fetch(self):
        return self.call(
            'GET',
            self.PROBLEM_URL.format(problem_id=self.problem_id)
        )

    def solve(self, json):
        return self.call(
            'POST',
            self.SOLVE_URL.format(problem_id=self.problem_id),
            json=json
        )

    def call(self, method, url, json=None):
        params = {
            'access_token': self.access_token,
        }

        response = requests.request(method, url, params=params, json=json)
        response.raise_for_status()

        return response.json()
