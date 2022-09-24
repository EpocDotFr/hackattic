# This script requires a running PostgreSQL database: https://www.postgresql.org/download/
# This script requires extra Python packages: pip install psycopg2-binary
import hackattic
import tempfile
import base64

problem = hackattic.Problem('backup_restore')

data = problem.fetch()

dump = tempfile.NamedTemporaryFile('wb', delete=False)
dump.write(base64.b64decode(data['dump']))
dump.close()

print(dump.name)

solution = {
    'alive_ssns': [],
}

# print(problem.solve(solution))
