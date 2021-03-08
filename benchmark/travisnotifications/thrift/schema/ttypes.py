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


class Notification(object):
    """
    Attributes:
     - secure

    """


    def __init__(self, secure=None,):
        self.secure = secure

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
                    self.secure = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Notification')
        if self.secure is not None:
            oprot.writeFieldBegin('secure', TType.STRING, 1)
            oprot.writeString(self.secure.encode('utf-8') if sys.version_info[0] == 2 else self.secure)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.secure is None:
            raise TProtocolException(message='Required field secure is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Notifications(object):
    """
    Attributes:
     - campfire
     - irc
     - flowdock
     - hipchat
     - slack
     - webhooks
     - email

    """


    def __init__(self, campfire=None, irc=None, flowdock=None, hipchat=None, slack=None, webhooks=None, email=None,):
        self.campfire = campfire
        self.irc = irc
        self.flowdock = flowdock
        self.hipchat = hipchat
        self.slack = slack
        self.webhooks = webhooks
        self.email = email

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
                    self.campfire = Notification()
                    self.campfire.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.irc = Notification()
                    self.irc.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.flowdock = Notification()
                    self.flowdock.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.hipchat = Notification()
                    self.hipchat.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.slack = Notification()
                    self.slack.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.webhooks = Notification()
                    self.webhooks.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.email = Notification()
                    self.email.read(iprot)
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
        oprot.writeStructBegin('Notifications')
        if self.campfire is not None:
            oprot.writeFieldBegin('campfire', TType.STRUCT, 1)
            self.campfire.write(oprot)
            oprot.writeFieldEnd()
        if self.irc is not None:
            oprot.writeFieldBegin('irc', TType.STRUCT, 2)
            self.irc.write(oprot)
            oprot.writeFieldEnd()
        if self.flowdock is not None:
            oprot.writeFieldBegin('flowdock', TType.STRUCT, 3)
            self.flowdock.write(oprot)
            oprot.writeFieldEnd()
        if self.hipchat is not None:
            oprot.writeFieldBegin('hipchat', TType.STRUCT, 4)
            self.hipchat.write(oprot)
            oprot.writeFieldEnd()
        if self.slack is not None:
            oprot.writeFieldBegin('slack', TType.STRUCT, 5)
            self.slack.write(oprot)
            oprot.writeFieldEnd()
        if self.webhooks is not None:
            oprot.writeFieldBegin('webhooks', TType.STRUCT, 6)
            self.webhooks.write(oprot)
            oprot.writeFieldEnd()
        if self.email is not None:
            oprot.writeFieldBegin('email', TType.STRUCT, 7)
            self.email.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.campfire is None:
            raise TProtocolException(message='Required field campfire is unset!')
        if self.irc is None:
            raise TProtocolException(message='Required field irc is unset!')
        if self.flowdock is None:
            raise TProtocolException(message='Required field flowdock is unset!')
        if self.hipchat is None:
            raise TProtocolException(message='Required field hipchat is unset!')
        if self.slack is None:
            raise TProtocolException(message='Required field slack is unset!')
        if self.webhooks is None:
            raise TProtocolException(message='Required field webhooks is unset!')
        if self.email is None:
            raise TProtocolException(message='Required field email is unset!')
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
     - notifications

    """


    def __init__(self, notifications=None,):
        self.notifications = notifications

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
                    self.notifications = Notifications()
                    self.notifications.read(iprot)
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
        if self.notifications is not None:
            oprot.writeFieldBegin('notifications', TType.STRUCT, 1)
            self.notifications.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.notifications is None:
            raise TProtocolException(message='Required field notifications is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Notification)
Notification.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'secure', 'UTF8', None, ),  # 1
)
all_structs.append(Notifications)
Notifications.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'campfire', [Notification, None], None, ),  # 1
    (2, TType.STRUCT, 'irc', [Notification, None], None, ),  # 2
    (3, TType.STRUCT, 'flowdock', [Notification, None], None, ),  # 3
    (4, TType.STRUCT, 'hipchat', [Notification, None], None, ),  # 4
    (5, TType.STRUCT, 'slack', [Notification, None], None, ),  # 5
    (6, TType.STRUCT, 'webhooks', [Notification, None], None, ),  # 6
    (7, TType.STRUCT, 'email', [Notification, None], None, ),  # 7
)
all_structs.append(Main)
Main.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'notifications', [Notifications, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs
