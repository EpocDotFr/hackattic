# This script requires a running PostgreSQL database: https://www.postgresql.org/download/ (edit credentials below)
from support import hackattic
import psycopg2
import tempfile
import base64
import os
import sh

PG_HOST = 'localhost'
PG_PORT = 5432
PG_DB = 'postgres'
PG_USERNAME = 'postgres'
PG_PASSWORD = 'postgres'


def restore_db(dump):
    with tempfile.NamedTemporaryFile('wb', delete=False, suffix='.sql.gz') as f:
        f.write(base64.b64decode(dump))

        dump_path = f.name
    
    sh.gunzip(dump_path, d=True)

    dump_path = dump_path.replace('.gz', '')

    os.putenv('PGPASSWORD', PG_PASSWORD)

    sh.psql(PG_DB, h=PG_HOST, p=str(PG_PORT), U=PG_USERNAME, c='DROP TABLE IF EXISTS criminal_records')
    sh.psql(PG_DB, h=PG_HOST, p=str(PG_PORT), U=PG_USERNAME, f=dump_path)


def extract_alive_ssns():
    conn = psycopg2.connect(host=PG_HOST, port=PG_PORT, dbname=PG_DB, user=PG_USERNAME, password=PG_PASSWORD)
    cur = conn.cursor()

    cur.execute("SELECT ssn FROM criminal_records WHERE status = 'alive';")

    ret = [
        row[0] for row in cur.fetchall()
    ]

    cur.close()
    conn.close()

    return ret


def run():
    problem = hackattic.Problem('backup_restore')

    data = problem.fetch()

    restore_db(data['dump'])

    solution = {
        'alive_ssns': extract_alive_ssns(),
    }

    print(problem.solve(solution))


if __name__ == '__main__':
    run()
