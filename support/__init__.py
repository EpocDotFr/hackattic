from .hackattic import requests
import subprocess
import tempfile


def run_subprocess(arguments):
    subprocess.run(arguments, check=True)


def download_file(url, suffix=''):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with tempfile.NamedTemporaryFile('wb', delete=False, suffix=suffix) as f:
        for chunk in response.iter_content(512):
            f.write(chunk)

        return f.name
