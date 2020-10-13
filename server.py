from __future__ import print_function
from flask import Flask
from flask import request
import base64
import io
import logging
import sys

app = Flask(__name__)


@app.route('/uploadfile', methods=['GET', 'POST', 'PUT'])
def uploadfile():
    # if request.method == 'GET':
    # f = request.files['file']
    # filePath = "./somedir/"+secure_filename(f.filename)
    # f.save(filePath)
    app.logger.info('testing info log')
    print(request.json['sound'], file=sys.stderr)
    sound_from_phone = request.json['sound']
    wav_file = open("temp.wav", "wb")
    decode_string = base64.b64decode(sound_from_phone)
    wav_file.write(decode_string)
    return request.data


if __name__ == "__main__":
    app.run()
