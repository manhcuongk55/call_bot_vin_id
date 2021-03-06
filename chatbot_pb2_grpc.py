# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import chatbot_pb2 as chatbot__pb2


class ChatBotStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListBot = channel.unary_unary(
        '/chatbot.ChatBot/ListBot',
        request_serializer=chatbot__pb2.ListBotRequest.SerializeToString,
        response_deserializer=chatbot__pb2.ListBotResponse.FromString,
        )
    self.ChatToBot = channel.stream_stream(
        '/chatbot.ChatBot/ChatToBot',
        request_serializer=chatbot__pb2.ChatBotRequest.SerializeToString,
        response_deserializer=chatbot__pb2.ChatBotResponse.FromString,
        )


class ChatBotServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListBot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChatToBot(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatBotServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListBot': grpc.unary_unary_rpc_method_handler(
          servicer.ListBot,
          request_deserializer=chatbot__pb2.ListBotRequest.FromString,
          response_serializer=chatbot__pb2.ListBotResponse.SerializeToString,
      ),
      'ChatToBot': grpc.stream_stream_rpc_method_handler(
          servicer.ChatToBot,
          request_deserializer=chatbot__pb2.ChatBotRequest.FromString,
          response_serializer=chatbot__pb2.ChatBotResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'chatbot.ChatBot', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
