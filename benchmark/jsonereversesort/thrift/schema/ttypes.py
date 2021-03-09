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


class Let(object):
    """
    Attributes:
     - x

    """


    def __init__(self, x=None,):
        self.x = x

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
                if ftype == TType.LIST:
                    self.x = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readByte()
                        self.x.append(_elem5)
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
        oprot.writeStructBegin('Let')
        if self.x is not None:
            oprot.writeFieldBegin('x', TType.LIST, 1)
            oprot.writeListBegin(TType.BYTE, len(self.x))
            for iter6 in self.x:
                oprot.writeByte(iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.x is None:
            raise TProtocolException(message='Required field x is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Sort(object):
    """
    Attributes:
     - eval

    """


    def __init__(self, eval=None,):
        self.eval = eval

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
                    self.eval = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Sort')
        if self.eval is not None:
            oprot.writeFieldBegin('eval', TType.STRING, 1)
            oprot.writeString(self.eval.encode('utf-8') if sys.version_info[0] == 2 else self.eval)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.eval is None:
            raise TProtocolException(message='Required field eval is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Reverse(object):
    """
    Attributes:
     - sort
     - byX

    """


    def __init__(self, sort=None, byX=None,):
        self.sort = sort
        self.byX = byX

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
                if ftype == TType.STRUCT:
                    self.sort = Sort()
                    self.sort.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.byX = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Reverse')
        if self.sort is not None:
            oprot.writeFieldBegin('sort', TType.STRUCT, 1)
            self.sort.write(oprot)
            oprot.writeFieldEnd()
        if self.byX is not None:
            oprot.writeFieldBegin('byX', TType.STRING, 2)
            oprot.writeString(self.byX.encode('utf-8') if sys.version_info[0] == 2 else self.byX)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.sort is None:
            raise TProtocolException(message='Required field sort is unset!')
        if self.byX is None:
            raise TProtocolException(message='Required field byX is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class In(object):
    """
    Attributes:
     - reverse

    """


    def __init__(self, reverse=None,):
        self.reverse = reverse

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
                if ftype == TType.STRUCT:
                    self.reverse = Reverse()
                    self.reverse.read(iprot)
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
        oprot.writeStructBegin('In')
        if self.reverse is not None:
            oprot.writeFieldBegin('reverse', TType.STRUCT, 1)
            self.reverse.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.reverse is None:
            raise TProtocolException(message='Required field reverse is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Main(object):
    """
    Attributes:
     - let
     - in1

    """


    def __init__(self, let=None, in1=None,):
        self.let = let
        self.in1 = in1

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
                if ftype == TType.STRUCT:
                    self.let = Let()
                    self.let.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.in1 = In()
                    self.in1.read(iprot)
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
        if self.let is not None:
            oprot.writeFieldBegin('let', TType.STRUCT, 1)
            self.let.write(oprot)
            oprot.writeFieldEnd()
        if self.in1 is not None:
            oprot.writeFieldBegin('in1', TType.STRUCT, 2)
            self.in1.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.let is None:
            raise TProtocolException(message='Required field let is unset!')
        if self.in1 is None:
            raise TProtocolException(message='Required field in1 is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Let)
Let.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'x', (TType.BYTE, None, False), None, ),  # 1
)
all_structs.append(Sort)
Sort.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'eval', 'UTF8', None, ),  # 1
)
all_structs.append(Reverse)
Reverse.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'sort', [Sort, None], None, ),  # 1
    (2, TType.STRING, 'byX', 'UTF8', None, ),  # 2
)
all_structs.append(In)
In.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'reverse', [Reverse, None], None, ),  # 1
)
all_structs.append(Main)
Main.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'let', [Let, None], None, ),  # 1
    (2, TType.STRUCT, 'in1', [In, None], None, ),  # 2
)
fix_spec(all_structs)
del all_structs
