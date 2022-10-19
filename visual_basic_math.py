# This script requires tesseract to be installed on your system (https://tesseract-ocr.github.io/tessdoc/Installation.html#installation)
from support import hackattic, download_file
import pytesseract


def read_and_calculate(image_path):
    operations = pytesseract.image_to_string(image_path, config='--psm 6')

    result = 0

    for operation in operations.splitlines():
        operation = operation.replace(' ', '').strip()

        symbol = operation[0]
        number = int(operation[1:])

        if symbol == '+':
            result += number
        elif symbol == '-':
            result -= number
        elif symbol in 'x':
            result *= number
        elif symbol == '÷':
            result //= number

    return result


def run():
    problem = hackattic.Problem('visual_basic_math')

    data = problem.fetch()

    image_path = download_file(data['image_url'], '.png')

    print(image_path)

    solution = {
        'result': read_and_calculate(image_path)
    }

    print(solution)

    # print(problem.solve(solution))


if __name__ == '__main__':
    run()
