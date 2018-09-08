import grpc

import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        result = stub.Add(calculator_pb2.AddRequest(n1=100, n2=10))
    print("Result:", result.res)


if __name__ == '__main__':
    run()