
import json
import sys
import os

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
app = ClarifaiApp(api_key='yourKey')

def clarifyFunc(files):
	model = app.models.get("d02b4508df58432fbb84e800597b8959")
	image = ClImage(file_obj=open(files, 'rb'))
	response = model.predict([image])
	return str(response)

fName = 'pathToImage'
print clarifyFunc(fName)
