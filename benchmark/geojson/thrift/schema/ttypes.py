#
# Autogenerated by Thrift Compiler (0.14.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Main(object):
    """
    Attributes:
     - type
     - coordinates

    """


    def __init__(self, type=None, coordinates=None,):
        self.type = type
        self.coordinates = coordinates

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.type = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.coordinates = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = []
                        (_etype9, _size6) = iprot.readListBegin()
                        for _i10 in range(_size6):
                            _elem11 = []
                            (_etype15, _size12) = iprot.readListBegin()
                            for _i16 in range(_size12):
                                _elem17 = []
                                (_etype21, _size18) = iprot.readListBegin()
                                for _i22 in range(_size18):
                                    _elem23 = iprot.readDouble()
                                    _elem17.append(_elem23)
                                iprot.readListEnd()
                                _elem11.append(_elem17)
                            iprot.readListEnd()
                            _elem5.append(_elem11)
                        iprot.readListEnd()
                        self.coordinates.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Main')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.STRING, 1)
            oprot.writeString(self.type.encode('utf-8') if sys.version_info[0] == 2 else self.type)
            oprot.writeFieldEnd()
        if self.coordinates is not None:
            oprot.writeFieldBegin('coordinates', TType.LIST, 2)
            oprot.writeListBegin(TType.LIST, len(self.coordinates))
            for iter24 in self.coordinates:
                oprot.writeListBegin(TType.LIST, len(iter24))
                for iter25 in iter24:
                    oprot.writeListBegin(TType.LIST, len(iter25))
                    for iter26 in iter25:
                        oprot.writeListBegin(TType.DOUBLE, len(iter26))
                        for iter27 in iter26:
                            oprot.writeDouble(iter27)
                        oprot.writeListEnd()
                    oprot.writeListEnd()
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        if self.coordinates is None:
            raise TProtocolException(message='Required field coordinates is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Main)
Main.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'type', 'UTF8', None, ),  # 1
    (2, TType.LIST, 'coordinates', (TType.LIST, (TType.LIST, (TType.LIST, (TType.DOUBLE, None, False), False), False), False), None, ),  # 2
)
fix_spec(all_structs)
del all_structs
