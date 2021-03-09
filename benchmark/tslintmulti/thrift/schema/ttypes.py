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


class Options(object):
    """
    Attributes:
     - groupedImports

    """


    def __init__(self, groupedImports=None,):
        self.groupedImports = groupedImports

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
                if ftype == TType.BOOL:
                    self.groupedImports = iprot.readBool()
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
        oprot.writeStructBegin('Options')
        if self.groupedImports is not None:
            oprot.writeFieldBegin('groupedImports', TType.BOOL, 1)
            oprot.writeBool(self.groupedImports)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.groupedImports is None:
            raise TProtocolException(message='Required field groupedImports is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class OrderedImports(object):
    """
    Attributes:
     - options

    """


    def __init__(self, options=None,):
        self.options = options

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
                    self.options = Options()
                    self.options.read(iprot)
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
        oprot.writeStructBegin('OrderedImports')
        if self.options is not None:
            oprot.writeFieldBegin('options', TType.STRUCT, 1)
            self.options.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.options is None:
            raise TProtocolException(message='Required field options is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Rules(object):
    """
    Attributes:
     - noAny
     - radix
     - orderedImports

    """


    def __init__(self, noAny=None, radix=None, orderedImports=None,):
        self.noAny = noAny
        self.radix = radix
        self.orderedImports = orderedImports

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
                    self.noAny = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readBool()
                        self.noAny.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.radix = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readBool()
                        self.radix.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.orderedImports = OrderedImports()
                    self.orderedImports.read(iprot)
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
        oprot.writeStructBegin('Rules')
        if self.noAny is not None:
            oprot.writeFieldBegin('noAny', TType.LIST, 1)
            oprot.writeListBegin(TType.BOOL, len(self.noAny))
            for iter12 in self.noAny:
                oprot.writeBool(iter12)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.radix is not None:
            oprot.writeFieldBegin('radix', TType.LIST, 2)
            oprot.writeListBegin(TType.BOOL, len(self.radix))
            for iter13 in self.radix:
                oprot.writeBool(iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.orderedImports is not None:
            oprot.writeFieldBegin('orderedImports', TType.STRUCT, 3)
            self.orderedImports.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.noAny is None:
            raise TProtocolException(message='Required field noAny is unset!')
        if self.radix is None:
            raise TProtocolException(message='Required field radix is unset!')
        if self.orderedImports is None:
            raise TProtocolException(message='Required field orderedImports is unset!')
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
     - rules

    """


    def __init__(self, rules=None,):
        self.rules = rules

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
                    self.rules = Rules()
                    self.rules.read(iprot)
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
        if self.rules is not None:
            oprot.writeFieldBegin('rules', TType.STRUCT, 1)
            self.rules.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.rules is None:
            raise TProtocolException(message='Required field rules is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Options)
Options.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'groupedImports', None, None, ),  # 1
)
all_structs.append(OrderedImports)
OrderedImports.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'options', [Options, None], None, ),  # 1
)
all_structs.append(Rules)
Rules.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'noAny', (TType.BOOL, None, False), None, ),  # 1
    (2, TType.LIST, 'radix', (TType.BOOL, None, False), None, ),  # 2
    (3, TType.STRUCT, 'orderedImports', [OrderedImports, None], None, ),  # 3
)
all_structs.append(Main)
Main.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'rules', [Rules, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs
