import hackattic

problem = hackattic.Problem('reading_qr')

data = problem.fetch()

image_url = data['image_url']

solution = {}

print(problem.solve(solution))
