# This script requires:
#   - a running PostgreSQL database: https://www.postgresql.org/download/ (edit credentials below)
#   - extra Python packages: pip install psycopg2-binary
import subprocess
import hackattic
import psycopg2
import tempfile
import base64
import os

PG_DB = 'postgres'
PG_USERNAME = 'postgres'
PG_PASSWORD = 'postgres'


def run_subprocess(arguments):
    subprocess.run(arguments, check=True)


problem = hackattic.Problem('backup_restore')

data = problem.fetch()

with tempfile.NamedTemporaryFile('wb', delete=False, suffix='.sql.gz') as f:
    f.write(base64.b64decode(data['dump']))

    dump_path = f.name

run_subprocess((
    'gunzip',
    '-d',
    dump_path
))

dump_path = dump_path.replace('.gz', '')

os.putenv('PGPASSWORD', PG_PASSWORD)

run_subprocess((
    'psql',
    PG_DB,
    '-U',
    PG_USERNAME,
    '-c',
    'DROP TABLE IF EXISTS criminal_records'
))

run_subprocess((
    'psql',
    PG_DB,
    '-U',
    PG_USERNAME,
    '-f',
    dump_path
))

solution = {
    'alive_ssns': [],
}

# print(problem.solve(solution))
