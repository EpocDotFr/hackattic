# This challenge is WIP
from support import hackattic, download_file
import threading
import itertools
import zipfile
import string
import queue


def add_passwords_to_queue(passwords):
    charset = string.ascii_lowercase + string.digits

    for length in range(4, 7):
        for combination in itertools.product(charset, repeat=length):
            passwords.put(''.join(combination).encode())


def brute_force_zip(passwords, zf):
    while not passwords.empty():
        try:
            secret = zf.read(
                'secret.txt',
                pwd=passwords.get()
            )

            print(f'FOUND: {secret}')

            with passwords.mutex:
                passwords.queue.clear()

            return secret
        except (RuntimeError, zipfile.BadZipFile):
            pass


def run():
    problem = hackattic.Problem('brute_force_zip')

    data = problem.fetch()

    zip_path = download_file(data['zip_url'], '.zip')

    passwords = queue.Queue()

    add_passwords_to_queue(passwords)

    zf = zipfile.ZipFile(zip_path)

    threads = []

    for i in range(1, 6):
        thread = threading.Thread(target=brute_force_zip, args=(passwords, zf), daemon=True)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    solution = {
        'secret': 'TODO'
    }

    zf.close()

    print(solution)

    # print(problem.solve(solution))


if __name__ == '__main__':
    run()
