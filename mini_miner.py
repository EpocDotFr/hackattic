from support import hackattic
import bitstring
import hashlib
import json
import sys


def run():
    problem = hackattic.Problem('mini_miner')

    data = problem.fetch()

    difficulty = int(data['difficulty'])
    block = data['block']

    nonce = None

    for i in range(1, sys.maxsize):
        block['nonce'] = i

        hash_bits = bitstring.Bits(bytes=hashlib.sha256(json.dumps(block, separators=(',', ':'), sort_keys=True).encode()).digest())

        if hash_bits.startswith('0b{}'.format('0' * difficulty)):
            nonce = i

            break

    solution = {
        'nonce': nonce
    }

    print(problem.solve(solution))


if __name__ == '__main__':
    run()
