import httplib, urllib, base64, json
import os
import time
import sys
###############################################
#### Update or verify the following values. ###
###############################################

faces ={}
summIm = open('/Users/almas/Documents/Research/demos/azure/idenfied.txt', 'w')


inputDir = '/Users/almas/Documents/Research/face_recog/rcnn_recog_faces/S06_e02_faces_cropped/'
def epIterate():
	count = 0
	for files in os.listdir(inputDir):
		if count < 20:
			count = count + 1
			if 'DS_Store' in files:
				continue
			else:
				fName = inputDir + files
				azureCall(files, open(fName, 'rb'))

		else:
			print 'Waiting for 65s'
			time.sleep(65)
			count = 0


def getFaceID(files, parsed):
	if parsed:
		# print 'FaceID is: ' + str(parsed[0]['faceId'])
		faces[files] = parsed[0]['faceId']
		print str(files)  + "  " + str(parsed[0]['faceId'])

		summIm.write(str(files)  + "  " + str(parsed[0]['faceId']) + '\n')

	else:
		summIm.write(str(files) + '\n')


# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'yourKey'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'Yourregion'

def azureCall(files, body):
	# Request headers.
	headers = {
	    'Content-Type': 'application/octet-stream',
	    'Ocp-Apim-Subscription-Key': subscription_key,
	}

	# Request parameters.
	params = urllib.urlencode({
	    'returnFaceId': 'true',
	    # 'returnFaceLandmarks': 'false',
	})

	# The URL of a JPEG image to analyze.
	try:
	    # Execute the REST API call and get the response.
	    conn = httplib.HTTPSConnection('eastus.api.cognitive.microsoft.com')
	    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
	    response = conn.getresponse()
	    data = response.read()

	    # 'data' contains the JSON data. The following formats the JSON data for display.
	    parsed = json.loads(data)
	    print ("Response:")
	    print (json.dumps(parsed, sort_keys=True, indent=2))
	    conn.close()

	except Exception as e:
	    print("[Errno {0}] {1}".format(e.errno, e.strerror))

	getFaceID(files, parsed)

epIterate()

