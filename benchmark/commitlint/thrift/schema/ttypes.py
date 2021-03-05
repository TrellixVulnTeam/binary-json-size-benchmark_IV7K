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


class Rule(object):
    """
    Attributes:
     - textual
     - numeric
     - multitextual

    """


    def __init__(self, textual=None, numeric=None, multitextual=None,):
        self.textual = textual
        self.numeric = numeric
        self.multitextual = multitextual

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
                    self.textual = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.numeric = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.multitextual = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        self.multitextual.append(_elem5)
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
        oprot.writeStructBegin('Rule')
        if self.textual is not None:
            oprot.writeFieldBegin('textual', TType.STRING, 1)
            oprot.writeString(self.textual.encode('utf-8') if sys.version_info[0] == 2 else self.textual)
            oprot.writeFieldEnd()
        if self.numeric is not None:
            oprot.writeFieldBegin('numeric', TType.BYTE, 2)
            oprot.writeByte(self.numeric)
            oprot.writeFieldEnd()
        if self.multitextual is not None:
            oprot.writeFieldBegin('multitextual', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.multitextual))
            for iter6 in self.multitextual:
                oprot.writeString(iter6.encode('utf-8') if sys.version_info[0] == 2 else iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
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
     - scopeCase
     - subjectCase

    """


    def __init__(self, scopeCase=None, subjectCase=None,):
        self.scopeCase = scopeCase
        self.subjectCase = subjectCase

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
                    self.scopeCase = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = Rule()
                        _elem12.read(iprot)
                        self.scopeCase.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.subjectCase = []
                    (_etype16, _size13) = iprot.readListBegin()
                    for _i17 in range(_size13):
                        _elem18 = Rule()
                        _elem18.read(iprot)
                        self.subjectCase.append(_elem18)
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
        oprot.writeStructBegin('Rules')
        if self.scopeCase is not None:
            oprot.writeFieldBegin('scopeCase', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.scopeCase))
            for iter19 in self.scopeCase:
                iter19.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.subjectCase is not None:
            oprot.writeFieldBegin('subjectCase', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.subjectCase))
            for iter20 in self.subjectCase:
                iter20.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.scopeCase is None:
            raise TProtocolException(message='Required field scopeCase is unset!')
        if self.subjectCase is None:
            raise TProtocolException(message='Required field subjectCase is unset!')
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
all_structs.append(Rule)
Rule.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'textual', 'UTF8', None, ),  # 1
    (2, TType.BYTE, 'numeric', None, None, ),  # 2
    (3, TType.LIST, 'multitextual', (TType.STRING, 'UTF8', False), None, ),  # 3
)
all_structs.append(Rules)
Rules.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'scopeCase', (TType.STRUCT, [Rule, None], False), None, ),  # 1
    (2, TType.LIST, 'subjectCase', (TType.STRUCT, [Rule, None], False), None, ),  # 2
)
all_structs.append(Main)
Main.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'rules', [Rules, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs
