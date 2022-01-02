import grpc

from translator_pb2 import TranslatorRequest
from translator_pb2_grpc import TranslationStub

channel = grpc.insecure_channel("localhost:50051")
client = TranslationStub(channel)


def test_empty():
    request = TranslatorRequest()
    response = client.Translate(request)

    assert response.target_text == "It's okay."


def test_full():
    request = TranslatorRequest()
    request.source_text = "Переводчик работает"
    response = client.Translate(request)

    assert response.target_text == "The translator is working."
