
import json
import sys
import os

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
app = ClarifaiApp(api_key='f7a91f12d5664eb4938cd583278e83f9')

def clarifyFunc(files):
	model = app.models.get("d02b4508df58432fbb84e800597b8959")
	image = ClImage(file_obj=open(files, 'rb'))
	response = model.predict([image])
	return str(response)

fName = '/Users/almas/Documents/Research/demos/clarify/S06_e02_02_34.516#0_N_phoebe.jpg'
print clarifyFunc(fName)
