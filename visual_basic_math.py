# This script requires tesseract to be installed on your system (https://tesseract-ocr.github.io/tessdoc/Installation.html#installation)
from support import hackattic, download_file
import pytesseract


def read_and_calculate(image_path):
    return pytesseract.image_to_string(image_path)


problem = hackattic.Problem('visual_basic_math')

data = problem.fetch()

image_path = download_file(data['image_url'], '.png')

print(image_path)

solution = {
    'result': read_and_calculate(image_path)
}

print(solution['result'])

# print(problem.solve(solution))
