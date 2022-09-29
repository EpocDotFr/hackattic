from support.data_stream import DataStream
from support import hackattic
import base64
import io

problem = hackattic.Problem('help_me_unpack')

data = problem.fetch()

solution = {}

with io.BytesIO(base64.b64decode(data['bytes'])) as f:
    ds = DataStream(f, DataStream.BSA_LITTLE_ENDIAN)

    solution['int'] = ds.read_int32()
    solution['uint'] = ds.read_uint32()
    solution['short'] = ds.read_int16()

    ds.read_bytes(2)

    solution['float'] = ds.read_float()
    solution['double'] = ds.read_double()

    solution['big_endian_double'] = ds.read_double(bsa=DataStream.BSA_BIG_ENDIAN)

print(problem.solve(solution))
