import grpc

import protobuf.api_pb2_grpc as pb2_grpc
import protobuf.api_pb2 as pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.APIStub(channel)
        response = stub.processRequest(
            pb2.apiRequest(symbol="ETH", investment=500))
    print("Greeter client received following from server: " +
          response.message + " with " + response.graph_data)


run()
