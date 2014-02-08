# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import color_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='shadows.proto',
  package='gazebo.msgs',
  serialized_pb='\n\rshadows.proto\x12\x0bgazebo.msgs\x1a\x0b\x63olor.proto\"\xc5\x01\n\x07Shadows\x12-\n\x04type\x18\x05 \x01(\x0e\x32\x1f.gazebo.msgs.Shadows.ShadowType\x12!\n\x05\x63olor\x18\x06 \x01(\x0b\x32\x12.gazebo.msgs.Color\"h\n\nShadowType\x12\x14\n\x10STENCIL_ADDITIVE\x10\x01\x12\x16\n\x12STENCIL_MODULATIVE\x10\x02\x12\x14\n\x10TEXTURE_ADDITIVE\x10\x03\x12\x16\n\x12TEXTURE_MODULATIVE\x10\x04')



_SHADOWS_SHADOWTYPE = descriptor.EnumDescriptor(
  name='ShadowType',
  full_name='gazebo.msgs.Shadows.ShadowType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='STENCIL_ADDITIVE', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STENCIL_MODULATIVE', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TEXTURE_ADDITIVE', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TEXTURE_MODULATIVE', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=137,
  serialized_end=241,
)


_SHADOWS = descriptor.Descriptor(
  name='Shadows',
  full_name='gazebo.msgs.Shadows',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='gazebo.msgs.Shadows.type', index=0,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='color', full_name='gazebo.msgs.Shadows.color', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SHADOWS_SHADOWTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=44,
  serialized_end=241,
)

_SHADOWS.fields_by_name['type'].enum_type = _SHADOWS_SHADOWTYPE
_SHADOWS.fields_by_name['color'].message_type = color_pb2._COLOR
_SHADOWS_SHADOWTYPE.containing_type = _SHADOWS;
DESCRIPTOR.message_types_by_name['Shadows'] = _SHADOWS

class Shadows(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHADOWS
  
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Shadows)

# @@protoc_insertion_point(module_scope)
