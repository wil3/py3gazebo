# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='request.proto',
  package='gazebo.msgs',
  serialized_pb='\n\rrequest.proto\x12\x0bgazebo.msgs\"F\n\x07Request\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07request\x18\x02 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12\x10\n\x08\x64\x62l_data\x18\x04 \x01(\x01')




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='gazebo.msgs.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.Request.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request', full_name='gazebo.msgs.Request.request', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='gazebo.msgs.Request.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dbl_data', full_name='gazebo.msgs.Request.dbl_data', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST

class Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST

  # @@protoc_insertion_point(class_scope:gazebo.msgs.Request)


# @@protoc_insertion_point(module_scope)
