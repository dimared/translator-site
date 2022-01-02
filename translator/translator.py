from concurrent import futures

import grpc

import translator_pb2_grpc
from translator_pb2 import TranslatorRequest, TranslatorResponse

from models import transformer_model

MAX_LENGTH = 512


class TranslationService(translator_pb2_grpc.TranslationServicer):
    def Translate(self, request: TranslatorRequest, context):
        source_text = request.source_text
        if len(source_text) > MAX_LENGTH:
            source_text = source_text[:MAX_LENGTH] + "..."

        target_text = transformer_model.translate(source_text)

        return TranslatorResponse(target_text=target_text)


def main():
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=4))
    translator_pb2_grpc.add_TranslationServicer_to_server(
        TranslationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Translation server is started")
    server.wait_for_termination()


if __name__ == "__main__":
    main()
