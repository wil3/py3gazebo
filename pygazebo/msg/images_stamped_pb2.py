# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import time_pb2
import image_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='images_stamped.proto',
  package='gazebo.msgs',
  serialized_pb='\n\x14images_stamped.proto\x12\x0bgazebo.msgs\x1a\ntime.proto\x1a\x0bimage.proto\"S\n\rImagesStamped\x12\x1f\n\x04time\x18\x01 \x02(\x0b\x32\x11.gazebo.msgs.Time\x12!\n\x05image\x18\x02 \x03(\x0b\x32\x12.gazebo.msgs.Image')




_IMAGESSTAMPED = descriptor.Descriptor(
  name='ImagesStamped',
  full_name='gazebo.msgs.ImagesStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='time', full_name='gazebo.msgs.ImagesStamped.time', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='image', full_name='gazebo.msgs.ImagesStamped.image', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=62,
  serialized_end=145,
)

_IMAGESSTAMPED.fields_by_name['time'].message_type = time_pb2._TIME
_IMAGESSTAMPED.fields_by_name['image'].message_type = image_pb2._IMAGE
DESCRIPTOR.message_types_by_name['ImagesStamped'] = _IMAGESSTAMPED

class ImagesStamped(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IMAGESSTAMPED
  
  # @@protoc_insertion_point(class_scope:gazebo.msgs.ImagesStamped)

# @@protoc_insertion_point(module_scope)
