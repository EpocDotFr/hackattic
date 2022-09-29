from support import hackattic
import struct
import base64

problem = hackattic.Problem('help_me_unpack')

data = problem.fetch()

decoded_bytes = base64.b64decode(data['bytes'])

i, ui, s, f, d = struct.unpack('<iIhxxfd', decoded_bytes[:24])
bed, = struct.unpack('>d', decoded_bytes[24:])

solution = {
    'int': i,
    'uint': ui,
    'short': s,
    'float': f,
    'double': d,
    'big_endian_double': bed,
}

print(problem.solve(solution))
