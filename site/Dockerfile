FROM python:3.11

RUN mkdir /site_service
COPY proto/ /site_service/proto/
COPY site/ /site_service/site/
WORKDIR /site_service/site
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../proto --python_out=. \
           --grpc_python_out=. ../proto/translator.proto

EXPOSE 5000
CMD ["python", "__main__.py"]
