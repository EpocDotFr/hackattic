from support import hackattic, download_file
import itertools
import zipfile
import string


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

zip_path = download_file(data['zip_url'], '.zip')

solution = {
    'secret': brute_force_zip(zip_path)
}

print(solution)

# print(problem.solve(solution))
