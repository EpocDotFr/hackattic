from support import hackattic
import itertools
import requests
import tempfile
import zipfile
import string

requests = requests.Session()


def download_zip(zip_url):
    response = requests.get(zip_url, stream=True)
    response.raise_for_status()

    with tempfile.NamedTemporaryFile('wb', delete=False, suffix='.zip') as f:
        for chunk in response.iter_content(512):
            f.write(chunk)

        return f.name


def brute_force_zip(zip_path):
    charset = string.ascii_lowercase + string.digits

    with zipfile.ZipFile(zip_path) as zf:
        for length in range(4, 7):
            for combination in itertools.product(charset, repeat=length):
                try:
                    return zf.read(
                        'secret.txt',
                        pwd=''.join(combination).encode()
                    )
                except (RuntimeError, zipfile.BadZipFile):
                    continue

    return ''


problem = hackattic.Problem('brute_force_zip')

data = problem.fetch()

zip_path = download_zip(data['zip_url'])

solution = {
    'secret': brute_force_zip(zip_path)
}

print(solution)

# print(problem.solve(solution))
