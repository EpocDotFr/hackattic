# This script requires:
#   - extra Python packages: pip install pyzbar pillow (see package's installation instructions as it has a system dependency)
from PIL import Image
from pyzbar import pyzbar
import hackattic
import tempfile
import requests

requests = requests.Session()


def download_image(image_url):
    response = requests.get(image_url, stream=True)
    response.raise_for_status()

    with tempfile.NamedTemporaryFile('wb', delete=False, suffix='.png') as f:
        for chunk in response.iter_content(512):
            f.write(chunk)

        return f.name


def decode_image(path):
    code = pyzbar.decode(
        Image.open(path)
    )

    if len(code) == 1:
        return code[0].data.decode()

    return None


problem = hackattic.Problem('reading_qr')

data = problem.fetch()

image_path = download_image(data['image_url'])

solution = {
    'code': decode_image(image_path)
}

print(problem.solve(solution))
