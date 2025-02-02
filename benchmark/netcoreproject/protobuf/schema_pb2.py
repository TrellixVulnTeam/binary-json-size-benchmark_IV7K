# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cschema.proto\".\n\x12\x43ompilationOptions\x12\x18\n\x10warningsAsErrors\x18\x01 \x01(\x08\"\xbe\x01\n\x0c\x44\x65pendencies\x12\x1d\n\x15microsoftBclImmutable\x18\x01 \x01(\t\x12)\n!microsoftAspNetConfigurationModel\x18\x02 \x01(\t\x12*\n\"microsoftAspNetDependencyInjection\x18\x03 \x01(\t\x12\x1e\n\x16microsoftAspNetLogging\x18\x04 \x01(\t\x12\x18\n\x10systemDataCommon\x18\x05 \x01(\t\"E\n\x11Net45Dependencies\x12\x15\n\rsystemRuntime\x18\x01 \x01(\t\x12\x19\n\x11systemCollections\x18\x02 \x01(\t\"\x8c\x04\n\x0fK10Dependencies\x12\x19\n\x11systemCollections\x18\x01 \x01(\t\x12#\n\x1bsystemCollectionsConcurrent\x18\x02 \x01(\t\x12\x1c\n\x14systemComponentModel\x18\x03 \x01(\t\x12\x15\n\rsystemConsole\x18\x04 \x01(\t\x12\"\n\x1asystemDiagnosticsContracts\x18\x05 \x01(\t\x12\x1e\n\x16systemDiagnosticsDebug\x18\x06 \x01(\t\x12\x1b\n\x13systemGlobalization\x18\x07 \x01(\t\x12\x12\n\nsystemLinq\x18\x08 \x01(\t\x12\x1d\n\x15systemLinqExpressions\x18\t \x01(\t\x12\x1b\n\x13systemLinqQueryable\x18\n \x01(\t\x12\x18\n\x10systemReflection\x18\x0b \x01(\t\x12\"\n\x1asystemReflectionExtensions\x18\x0c \x01(\t\x12&\n\x1esystemResourcesResourceManager\x18\r \x01(\t\x12\x15\n\rsystemRuntime\x18\x0e \x01(\t\x12\x1f\n\x17systemRuntimeExtensions\x18\x0f \x01(\t\x12\x17\n\x0fsystemThreading\x18\x10 \x01(\t\x12\x1c\n\x14systemThreadingTasks\x18\x11 \x01(\t\"1\n\x05Net45\x12(\n\x0c\x64\x65pendencies\x18\x01 \x01(\x0b\x32\x12.Net45Dependencies\"-\n\x03K10\x12&\n\x0c\x64\x65pendencies\x18\x01 \x01(\x0b\x32\x10.K10Dependencies\"6\n\nFrameworks\x12\x15\n\x05net45\x18\x01 \x01(\x0b\x32\x06.Net45\x12\x11\n\x03k10\x18\x02 \x01(\x0b\x32\x04.K10\"\x9c\x01\n\x04Main\x12\x0f\n\x07version\x18\x01 \x01(\t\x12/\n\x12\x63ompilationOptions\x18\x02 \x01(\x0b\x32\x13.CompilationOptions\x12#\n\x0c\x64\x65pendencies\x18\x03 \x01(\x0b\x32\r.Dependencies\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\x1f\n\nframeworks\x18\x05 \x01(\x0b\x32\x0b.Frameworksb\x06proto3'
)




_COMPILATIONOPTIONS = _descriptor.Descriptor(
  name='CompilationOptions',
  full_name='CompilationOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='warningsAsErrors', full_name='CompilationOptions.warningsAsErrors', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=62,
)


_DEPENDENCIES = _descriptor.Descriptor(
  name='Dependencies',
  full_name='Dependencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='microsoftBclImmutable', full_name='Dependencies.microsoftBclImmutable', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='microsoftAspNetConfigurationModel', full_name='Dependencies.microsoftAspNetConfigurationModel', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='microsoftAspNetDependencyInjection', full_name='Dependencies.microsoftAspNetDependencyInjection', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='microsoftAspNetLogging', full_name='Dependencies.microsoftAspNetLogging', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemDataCommon', full_name='Dependencies.systemDataCommon', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=255,
)


_NET45DEPENDENCIES = _descriptor.Descriptor(
  name='Net45Dependencies',
  full_name='Net45Dependencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='systemRuntime', full_name='Net45Dependencies.systemRuntime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemCollections', full_name='Net45Dependencies.systemCollections', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=326,
)


_K10DEPENDENCIES = _descriptor.Descriptor(
  name='K10Dependencies',
  full_name='K10Dependencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='systemCollections', full_name='K10Dependencies.systemCollections', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemCollectionsConcurrent', full_name='K10Dependencies.systemCollectionsConcurrent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemComponentModel', full_name='K10Dependencies.systemComponentModel', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemConsole', full_name='K10Dependencies.systemConsole', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemDiagnosticsContracts', full_name='K10Dependencies.systemDiagnosticsContracts', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemDiagnosticsDebug', full_name='K10Dependencies.systemDiagnosticsDebug', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemGlobalization', full_name='K10Dependencies.systemGlobalization', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemLinq', full_name='K10Dependencies.systemLinq', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemLinqExpressions', full_name='K10Dependencies.systemLinqExpressions', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemLinqQueryable', full_name='K10Dependencies.systemLinqQueryable', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemReflection', full_name='K10Dependencies.systemReflection', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemReflectionExtensions', full_name='K10Dependencies.systemReflectionExtensions', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemResourcesResourceManager', full_name='K10Dependencies.systemResourcesResourceManager', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemRuntime', full_name='K10Dependencies.systemRuntime', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemRuntimeExtensions', full_name='K10Dependencies.systemRuntimeExtensions', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemThreading', full_name='K10Dependencies.systemThreading', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemThreadingTasks', full_name='K10Dependencies.systemThreadingTasks', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=853,
)


_NET45 = _descriptor.Descriptor(
  name='Net45',
  full_name='Net45',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='Net45.dependencies', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=904,
)


_K10 = _descriptor.Descriptor(
  name='K10',
  full_name='K10',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='K10.dependencies', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=906,
  serialized_end=951,
)


_FRAMEWORKS = _descriptor.Descriptor(
  name='Frameworks',
  full_name='Frameworks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='net45', full_name='Frameworks.net45', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='k10', full_name='Frameworks.k10', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=953,
  serialized_end=1007,
)


_MAIN = _descriptor.Descriptor(
  name='Main',
  full_name='Main',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Main.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compilationOptions', full_name='Main.compilationOptions', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='Main.dependencies', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='Main.code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frameworks', full_name='Main.frameworks', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1010,
  serialized_end=1166,
)

_NET45.fields_by_name['dependencies'].message_type = _NET45DEPENDENCIES
_K10.fields_by_name['dependencies'].message_type = _K10DEPENDENCIES
_FRAMEWORKS.fields_by_name['net45'].message_type = _NET45
_FRAMEWORKS.fields_by_name['k10'].message_type = _K10
_MAIN.fields_by_name['compilationOptions'].message_type = _COMPILATIONOPTIONS
_MAIN.fields_by_name['dependencies'].message_type = _DEPENDENCIES
_MAIN.fields_by_name['frameworks'].message_type = _FRAMEWORKS
DESCRIPTOR.message_types_by_name['CompilationOptions'] = _COMPILATIONOPTIONS
DESCRIPTOR.message_types_by_name['Dependencies'] = _DEPENDENCIES
DESCRIPTOR.message_types_by_name['Net45Dependencies'] = _NET45DEPENDENCIES
DESCRIPTOR.message_types_by_name['K10Dependencies'] = _K10DEPENDENCIES
DESCRIPTOR.message_types_by_name['Net45'] = _NET45
DESCRIPTOR.message_types_by_name['K10'] = _K10
DESCRIPTOR.message_types_by_name['Frameworks'] = _FRAMEWORKS
DESCRIPTOR.message_types_by_name['Main'] = _MAIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CompilationOptions = _reflection.GeneratedProtocolMessageType('CompilationOptions', (_message.Message,), {
  'DESCRIPTOR' : _COMPILATIONOPTIONS,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:CompilationOptions)
  })
_sym_db.RegisterMessage(CompilationOptions)

Dependencies = _reflection.GeneratedProtocolMessageType('Dependencies', (_message.Message,), {
  'DESCRIPTOR' : _DEPENDENCIES,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:Dependencies)
  })
_sym_db.RegisterMessage(Dependencies)

Net45Dependencies = _reflection.GeneratedProtocolMessageType('Net45Dependencies', (_message.Message,), {
  'DESCRIPTOR' : _NET45DEPENDENCIES,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:Net45Dependencies)
  })
_sym_db.RegisterMessage(Net45Dependencies)

K10Dependencies = _reflection.GeneratedProtocolMessageType('K10Dependencies', (_message.Message,), {
  'DESCRIPTOR' : _K10DEPENDENCIES,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:K10Dependencies)
  })
_sym_db.RegisterMessage(K10Dependencies)

Net45 = _reflection.GeneratedProtocolMessageType('Net45', (_message.Message,), {
  'DESCRIPTOR' : _NET45,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:Net45)
  })
_sym_db.RegisterMessage(Net45)

K10 = _reflection.GeneratedProtocolMessageType('K10', (_message.Message,), {
  'DESCRIPTOR' : _K10,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:K10)
  })
_sym_db.RegisterMessage(K10)

Frameworks = _reflection.GeneratedProtocolMessageType('Frameworks', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEWORKS,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:Frameworks)
  })
_sym_db.RegisterMessage(Frameworks)

Main = _reflection.GeneratedProtocolMessageType('Main', (_message.Message,), {
  'DESCRIPTOR' : _MAIN,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:Main)
  })
_sym_db.RegisterMessage(Main)


# @@protoc_insertion_point(module_scope)
