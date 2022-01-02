import os
import logging
logging.basicConfig(filename='site.log', encoding='utf-8', level=logging.DEBUG)

from flask import Flask, render_template, url_for, request

import grpc

from translator_pb2 import TranslatorRequest
from translator_pb2_grpc import TranslationStub

translator_host = os.getenv("TRANSLATOR_HOST", "localhost")
channel = grpc.insecure_channel(f"{translator_host}:50051")
client = TranslationStub(channel)

app = Flask(__name__)


def make_seq2seq_request(source_text):
    logging.debug(f'Make seq2seq request with text: {source_text}')
    mt_request = TranslatorRequest()
    mt_request.source_text = source_text
    mt_response = client.Translate(mt_request)

    return mt_response.target_text


def get_favicon():
    favicon = dict()
    favicon['apple'] = url_for('static', filename='favicon_io/apple-touch-icon.png')
    favicon['png32'] = url_for('static', filename='favicon_io/favicon-32x32.png')
    favicon['png16'] = url_for('static', filename='favicon_io/favicon-16x16.png')
    favicon['webmanifest'] = url_for('static', filename='favicon_io/site.webmanifest')

    return favicon


@app.route('/', methods=['post', 'get'])
def main():

    translation = ''
    if request.method == 'POST':
        source_text = request.form.get('text')
        translation = make_seq2seq_request(source_text)

    css = url_for('static', filename='bootstrap.css')

    return render_template('index.html', css=css, favicon=get_favicon(), translation=translation)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
