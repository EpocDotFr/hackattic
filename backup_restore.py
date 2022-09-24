# This script requires:
#   - a running PostgreSQL database: https://www.postgresql.org/download/ (edit credentials below)
#   - extra Python packages: pip install psycopg2-binary
import subprocess
import hackattic
import psycopg2
import tempfile
import base64

problem = hackattic.Problem('backup_restore')

data = problem.fetch()

with tempfile.NamedTemporaryFile('wb', delete=False, suffix='.sql.gz') as f:
    f.write(base64.b64decode(data['dump']))

    dump_path = f.name

print(dump_path)

# gunzip -d /tmp/name.sql.gz
# => /tmp/name.sql

solution = {
    'alive_ssns': [],
}

# print(problem.solve(solution))
