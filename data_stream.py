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

    def read_boolean(self):
        return self.unpack(DataStream.TYPE_BOOLEAN)

    def write_boolean(self, data):
        self.pack(DataStream.TYPE_BOOLEAN, data)

    def read_float(self):
        return FloatType(self.unpack(DataStream.TYPE_FLOAT, 4))

    def write_float(self, data):
        self.pack(DataStream.TYPE_FLOAT, data)

    def read_double(self):
        return DoubleType(self.unpack(DataStream.TYPE_DOUBLE, 8))

    def write_double(self, data):
        self.pack(DataStream.TYPE_DOUBLE, data)

    def read_int8(self):
        return Int8Type(self.unpack(DataStream.TYPE_INT8))

    def write_int8(self, data):
        self.pack(DataStream.TYPE_INT8, data)

    def read_uint8(self):
        return UInt8Type(self.unpack(DataStream.TYPE_UINT8))

    def write_uint8(self, data):
        self.pack(DataStream.TYPE_UINT8, data)

    def read_int16(self):
        return Int16Type(self.unpack(DataStream.TYPE_INT16, 2))

    def write_int16(self, data):
        self.pack(DataStream.TYPE_INT16, data)

    def read_uint16(self):
        return UInt16Type(self.unpack(DataStream.TYPE_UINT16, 2))

    def write_uint16(self, data):
        self.pack(DataStream.TYPE_UINT16, data)

    def read_int32(self):
        return Int32Type(self.unpack(DataStream.TYPE_INT32, 4))

    def write_int32(self, data):
        self.pack(DataStream.TYPE_INT32, data)

    def read_uint32(self):
        return UInt32Type(self.unpack(DataStream.TYPE_UINT32, 4))

    def write_uint32(self, data):
        self.pack(DataStream.TYPE_UINT32, data)

    def read_int64(self):
        return Int64Type(self.unpack(DataStream.TYPE_INT64, 8))

    def write_int64(self, data):
        self.pack(DataStream.TYPE_INT64, data)

    def read_uint64(self):
        return UInt64Type(self.unpack(DataStream.TYPE_UINT64, 8))

    def write_uint64(self, data):
        self.pack(DataStream.TYPE_UINT64, data)

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
