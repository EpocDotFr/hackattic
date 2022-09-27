# This script requires:
#   - extra Python packages: pip install cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from cryptography import x509
import hackattic
import datetime
import base64

def get_country_code(country):
    if country == 'Tokelau Islands':
        return 'TK'
    elif country == 'Christmas Island':
        return 'CX'
    elif country in ('Cocos Islands', 'Keeling Islands'):
        return 'CC'
    elif country == 'Sint Maarten':
        return 'SX'

    return None

problem = hackattic.Problem('tales_of_ssl')

data = problem.fetch()

private_key = data['private_key']
domain = data['required_data']['domain']
serial_number = int(data['required_data']['serial_number'], 0)
country_code = get_country_code(data['required_data']['country'])

key = serialization.load_der_private_key(base64.b64decode(private_key), password=None)

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, country_code),
    x509.NameAttribute(NameOID.COMMON_NAME, domain),
])

cert = x509.CertificateBuilder() \
    .subject_name(subject) \
    .issuer_name(issuer) \
    .public_key(key.public_key()) \
    .serial_number(serial_number) \
    .not_valid_before(datetime.datetime.utcnow()) \
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=30)) \
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName(domain)]),
        critical=False
    ) \
    .sign(key, hashes.SHA256())

solution = {
    'certificate': base64.b64encode(cert.public_bytes(serialization.Encoding.DER)).decode('ascii')
}

print(problem.solve(solution))
