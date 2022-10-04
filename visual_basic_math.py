# This script requires tesseract to be installed on your system (https://tesseract-ocr.github.io/tessdoc/Installation.html#installation)
from support import hackattic, download_file
from PIL import Image
import pytesseract


def read_and_calculate(image_path):
    image = Image.open(image_path).convert('L')

    width, height = image.size

    for x in range(0, width - 1):
        for y in range(0, height - 1):
            current_color = image.getpixel((x, y))

            if current_color != 255:
                image.putpixel((x, y), 0)

    image.show()

    return pytesseract.image_to_string(image)


problem = hackattic.Problem('visual_basic_math')

data = problem.fetch()

image_path = download_file(data['image_url'], '.png')

print(image_path)

solution = {
    'result': read_and_calculate(image_path)
}

print(solution['result'])

# print(problem.solve(solution))
