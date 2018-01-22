import json
import sys
import os

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
app = ClarifaiApp(api_key='yourKeyHere')

# image Name + 1024 vector numbers 
vectIm = open('/Users/almas/Documents/Research/demos/clarify/vectors.txt', 'w')
# imName + identified or not
summIm = open('/Users/almas/Documents/Research/demos/clarify/idenfied.txt', 'w')

def clarifyFunc(files):
	model = app.models.get("d02b4508df58432fbb84e800597b8959")
	image = ClImage(file_obj=open(files, 'rb'))
	response = model.predict([image])

	boo = 'no_face'
	res = []
# print json.dumps(response, indent=4)
	if response['outputs'][0]['data']:
		res = response['outputs'][0]['data']['regions'][0]['data']['embeddings'][0]['vector']
		boo = 'no_face'
		print str(res)
		if res:
			boo = 'face'

		return str(res), boo
	return res, boo


inputDir = 'pathToFolder'
def epIterate():
	for files in os.listdir(inputDir):
		if 'DS_Store' in files:
			continue
		else:
			fName = inputDir + files
			clarOut, boo = clarifyFunc(fName)
			vectIm.write(fName + ' : ' + str(clarOut))
			summIm.write(fName + ' : ' + str(boo))
			print files + ' : ' + str(boo) + ' _____ ' + str(clarOut)

epIterate()


