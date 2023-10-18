"""This is the core of the api,
creating a central point for blueprinted frameworks to flow through"""

import grpc
from concurrent import futures
import time
import protobuf.api_pb2_grpc as pb2_grpc
import protobuf.api_pb2 as pb2
from proto_classes.api_class import APIService

def serve():
    print('Starting serve')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_APIServicer_to_server(APIService(), server)
    server.add_insecure_port('[::]:50051')
    print('About to serve port')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
