from support import hackattic
import binascii
import hashlib
import base64
import hmac


problem = hackattic.Problem('password_hashing')

data = problem.fetch()

password = data['password'].encode()
salt = base64.b64decode(data['salt'])
pbkdf2_hash = data['pbkdf2']['hash']
pbkdf2_rounds = data['pbkdf2']['rounds']
scrypt_n = data['scrypt']['N']
scrypt_p = data['scrypt']['p']
scrypt_r = data['scrypt']['r']
scrypt_buflen = data['scrypt']['buflen']

solution_sha256 = hashlib.sha256(password)
solution_hmac = hmac.new(salt, password, digestmod=hashlib.sha256)
solution_pbkdf2 = hashlib.pbkdf2_hmac(pbkdf2_hash, password, salt, pbkdf2_rounds)
solution_scrypt = hashlib.scrypt(password, salt=salt, n=scrypt_n, r=scrypt_r, p=scrypt_p, dklen=scrypt_buflen, maxmem=(scrypt_n * 2 * scrypt_r * 65))

solution = {
    'sha256': solution_sha256.hexdigest(),
    'hmac': solution_hmac.hexdigest(),
    'pbkdf2': binascii.hexlify(solution_pbkdf2).decode(),
    'scrypt': binascii.hexlify(solution_scrypt).decode(),
}

print(problem.solve(solution))
