# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/node_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..entity import request_pb2 as entity_dot_request__pb2
from ..entity import response_pb2 as entity_dot_response__pb2
from ..entity import stream_message_pb2 as entity_dot_stream__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bservices/node_service.proto\x12\x04grpc\x1a\x14\x65ntity/request.proto\x1a\x15\x65ntity/response.proto\x1a\x1b\x65ntity/stream_message.proto2\xfa\x01\n\x0bNodeService\x12+\n\x08Register\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12\x30\n\rSendHeartbeat\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12\'\n\x04Ping\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12\x33\n\tSubscribe\x12\r.grpc.Request\x1a\x13.grpc.StreamMessage\"\x00\x30\x01\x12.\n\x0bUnsubscribe\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x42\x08Z\x06.;grpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.node_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\006.;grpc'
  _NODESERVICE._serialized_start=112
  _NODESERVICE._serialized_end=362
# @@protoc_insertion_point(module_scope)