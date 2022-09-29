import struct


class FloatType(float):
    pass


class DoubleType(float):
    pass


class Int8Type(int):
    pass


class UInt8Type(int):
    pass


class Int16Type(int):
    pass


class UInt16Type(int):
    pass


class Int32Type(int):
    pass


class UInt32Type(int):
    pass


class Int64Type(int):
    pass


class UInt64Type(int):
    pass


class DataStream:
    TYPE_BOOLEAN = '?'
    TYPE_FLOAT = 'f'
    TYPE_DOUBLE = 'd'
    TYPE_INT8 = 'b'
    TYPE_UINT8 = 'B'
    TYPE_INT16 = 'h'
    TYPE_UINT16 = 'H'
    TYPE_INT32 = 'i'
    TYPE_UINT32 = 'I'
    TYPE_INT64 = 'q'
    TYPE_UINT64 = 'Q'

    BSA_FULL_NATIVE = '@'
    BSA_BYTE_ORDER_NATIVE_ONLY = '='
    BSA_LITTLE_ENDIAN = '<'
    BSA_BIG_ENDIAN = '>'
    BSA_NETWORK = '!'

    def __init__(self, f, default_bsa=None):
        self.f = f
        self.default_bsa = default_bsa

    def read_boolean(self, bsa=None):
        return self.unpack(DataStream.TYPE_BOOLEAN, bsa=bsa)

    def write_boolean(self, data, bsa=None):
        self.pack(DataStream.TYPE_BOOLEAN, data, bsa=bsa)

    def read_float(self, bsa=None):
        return FloatType(self.unpack(DataStream.TYPE_FLOAT, 4, bsa=bsa))

    def write_float(self, data, bsa=None):
        self.pack(DataStream.TYPE_FLOAT, data, bsa=bsa)

    def read_double(self, bsa=None):
        return DoubleType(self.unpack(DataStream.TYPE_DOUBLE, 8, bsa=bsa))

    def write_double(self, data, bsa=None):
        self.pack(DataStream.TYPE_DOUBLE, data, bsa=bsa)

    def read_int8(self, bsa=None):
        return Int8Type(self.unpack(DataStream.TYPE_INT8, bsa=bsa))

    def write_int8(self, data, bsa=None):
        self.pack(DataStream.TYPE_INT8, data, bsa=bsa)

    def read_uint8(self, bsa=None):
        return UInt8Type(self.unpack(DataStream.TYPE_UINT8, bsa=bsa))

    def write_uint8(self, data, bsa=None):
        self.pack(DataStream.TYPE_UINT8, data, bsa=bsa)

    def read_int16(self, bsa=None):
        return Int16Type(self.unpack(DataStream.TYPE_INT16, 2, bsa=bsa))

    def write_int16(self, data, bsa=None):
        self.pack(DataStream.TYPE_INT16, data, bsa=bsa)

    def read_uint16(self, bsa=None):
        return UInt16Type(self.unpack(DataStream.TYPE_UINT16, 2, bsa=bsa))

    def write_uint16(self, data, bsa=None):
        self.pack(DataStream.TYPE_UINT16, data, bsa=bsa)

    def read_int32(self, bsa=None):
        return Int32Type(self.unpack(DataStream.TYPE_INT32, 4, bsa=bsa))

    def write_int32(self, data, bsa=None):
        self.pack(DataStream.TYPE_INT32, data, bsa=bsa)

    def read_uint32(self, bsa=None):
        return UInt32Type(self.unpack(DataStream.TYPE_UINT32, 4, bsa=bsa))

    def write_uint32(self, data, bsa=None):
        self.pack(DataStream.TYPE_UINT32, data, bsa=bsa)

    def read_int64(self, bsa=None):
        return Int64Type(self.unpack(DataStream.TYPE_INT64, 8, bsa=bsa))

    def write_int64(self, data, bsa=None):
        self.pack(DataStream.TYPE_INT64, data, bsa=bsa)

    def read_uint64(self, bsa=None):
        return UInt64Type(self.unpack(DataStream.TYPE_UINT64, 8, bsa=bsa))

    def write_uint64(self, data, bsa=None):
        self.pack(DataStream.TYPE_UINT64, data, bsa=bsa)

    def read_bytes(self, size):
        return self.f.read(size)

    def write_bytes(self, data):
        self.f.write(data)

    def read_byte(self):
        return self.read_bytes(1)

    def unpack(self, fmt, size=1, bsa=None):
        ret = struct.unpack(
            ''.join([
                bsa or self.default_bsa or '',
                fmt
            ]),
            self.read_bytes(size)
        )

        return ret[0] if len(ret) == 1 else ret

    def pack(self, fmt, data, bsa=None):
        self.write_bytes(
            struct.pack(
                ''.join([
                    bsa or self.default_bsa or '',
                    fmt
                ]),
                *(data if isinstance(data, (tuple, list)) else (data, ))
            )
        )
