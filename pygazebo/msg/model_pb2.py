# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import joint_pb2
import link_pb2
import pose_pb2
import visual_pb2
import vector3d_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='model.proto',
  package='gazebo.msgs',
  serialized_pb='\n\x0bmodel.proto\x12\x0bgazebo.msgs\x1a\x0bjoint.proto\x1a\nlink.proto\x1a\npose.proto\x1a\x0cvisual.proto\x1a\x0evector3d.proto\"\xf5\x01\n\x05Model\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12\x11\n\tis_static\x18\x03 \x01(\x08\x12\x1f\n\x04pose\x18\x04 \x01(\x0b\x32\x11.gazebo.msgs.Pose\x12!\n\x05joint\x18\x05 \x03(\x0b\x32\x12.gazebo.msgs.Joint\x12\x1f\n\x04link\x18\x06 \x03(\x0b\x32\x11.gazebo.msgs.Link\x12\x0f\n\x07\x64\x65leted\x18\x07 \x01(\x08\x12#\n\x06visual\x18\x08 \x03(\x0b\x32\x13.gazebo.msgs.Visual\x12$\n\x05scale\x18\t \x01(\x0b\x32\x15.gazebo.msgs.Vector3d')




_MODEL = descriptor.Descriptor(
  name='Model',
  full_name='gazebo.msgs.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Model.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.Model.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_static', full_name='gazebo.msgs.Model.is_static', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pose', full_name='gazebo.msgs.Model.pose', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='joint', full_name='gazebo.msgs.Model.joint', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='link', full_name='gazebo.msgs.Model.link', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='deleted', full_name='gazebo.msgs.Model.deleted', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='visual', full_name='gazebo.msgs.Model.visual', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='scale', full_name='gazebo.msgs.Model.scale', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=96,
  serialized_end=341,
)

_MODEL.fields_by_name['pose'].message_type = pose_pb2._POSE
_MODEL.fields_by_name['joint'].message_type = joint_pb2._JOINT
_MODEL.fields_by_name['link'].message_type = link_pb2._LINK
_MODEL.fields_by_name['visual'].message_type = visual_pb2._VISUAL
_MODEL.fields_by_name['scale'].message_type = vector3d_pb2._VECTOR3D
DESCRIPTOR.message_types_by_name['Model'] = _MODEL

class Model(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODEL
  
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Model)

# @@protoc_insertion_point(module_scope)
