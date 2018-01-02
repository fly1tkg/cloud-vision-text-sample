# -*- coding: utf_8 -*-
import io
import os
import json
import glob

from pprint import pprint

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from google.protobuf.json_format import MessageToJson

def annotate(basename):
    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources/{}'.format(basename))

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Specify language hints
    image_context = types.ImageContext(language_hints=['ja'])

    response = client.text_detection(image=image,image_context=image_context)

    # Write JSON File
    serialized = MessageToJson(response)
    data = json.loads(serialized)

    f = open('results/{}.json'.format(os.path.splitext(basename)[0]), 'w')
    f.write(json.dumps(data,ensure_ascii=False))
    f.close()

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Annotate images in resources folder
paths = glob.glob("resources/*.jpg")

for path in paths:
    annotate(os.path.basename(path))
