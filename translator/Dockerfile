FROM huggingface/transformers-pytorch-gpu

RUN mkdir /service
COPY proto/ /service/proto/
COPY translator/ /service/translator/
WORKDIR /service/translator

RUN python3 -m pip install -r requirements.txt
RUN python3 -m grpc_tools.protoc -I ../proto --python_out=. \
           --grpc_python_out=. ../proto/translator.proto

EXPOSE 50051
ENTRYPOINT ["python3", "translator.py"]

