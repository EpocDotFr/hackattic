# This script requires zbar to be installed on your system (https://github.com/NaturalHistoryMuseum/pyzbar#installation)
from support import hackattic, download_file
from pyzbar import pyzbar
from PIL import Image


def decode_image(path):
    code = pyzbar.decode(
        Image.open(path)
    )

    if len(code) == 1:
        return code[0].data.decode()

    return None


problem = hackattic.Problem('reading_qr')

data = problem.fetch()

image_path = download_file(data['image_url'], '.png')

solution = {
    'code': decode_image(image_path)
}

print(problem.solve(solution))
