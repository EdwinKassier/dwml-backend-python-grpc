
import grpc
from concurrent import futures
import time
import protobuf.api_pb2_grpc as pb2_grpc
import protobuf.api_pb2 as pb2
import json
import traceback
from utils import data_collector, graph_creator


class APIService(pb2_grpc.APIServicer):

    def __init__(self, *args, **kwargs):
        pass

    def proto2dict(self, msg):
        hsh_val = dict(msg.ListFields())
        d = dict((k, hsh_val[hsh]) for k, hsh in msg.DESCRIPTOR.fields_by_name.items())
        return d

    def processRequest(self, message, metadata):

        try:

            param_dict = self.proto2dict(message)
            symbol = param_dict["symbol"]
            investment = param_dict["investment"]

            print("API class")
            print(f"dict {param_dict}")

            collector = data_collector.DataCollector(symbol, investment)
            creator = graph_creator.GraphCreator(symbol)
            result = collector.driver_logic()
            graph_data = creator.driver_logic()
            final_result = {"message": json.dumps(result), "graph_data": json.dumps(graph_data)}
            return pb2.apiResponse(**final_result)
        except Exception as exc:
            print(exc)
            final_result = {"message": exc, "graph_data": "failure"}
            return pb2.apiResponse(**final_result)
