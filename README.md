# ReviewFaceRecognition
Review Face Recognition packages such as ClarifAI, face_recognition (dlib) and Microsoft Azure

Motivation: For my research, I was tasked to evaluate exisiting face recognition packages and compare their performances. Although, the goal was to use Faster RCNN for both face identification and recognition, Faster RCNN model we used was trained only to identify. As a result, we needed to find package that would classify already identified faces. 

**Goal** Find a package that would recognize faces already identified (and cropped) by Faster RCNN as 'face'.

**Step 1** Faster RCNN 
- My tutorial on how to install Faster RCNN can be found [here](https://github.com/AlmasM/EmotionDetection#installation-of-faster-r-cnn-based-on-face-py-faster-rcnn)
- Extract faces from pictures and crop them using Faster RCNN and OpenCV. 

**NOTE** All the images passed through Testing APIs are classified as 'face' by Faster RCNN. 

**Step 2** Installation of Testing APIs
- **Microsoft Azure**
  - Hardest and least intuitive API (among these APIs) to install. Perhaps it was my inexperience, but I found online modules and guides provided by Microsoft to be unclear, and I couldn't find much information on th internet on how to install/deploy the package.
  - Note 1: when using Free Tier you are limited to 10,000 requests per month AND 20 calls per minute. In other words, you will be able to evaluate only 20 images per minute. 
  - Note 2: Whenever Azure produces an output, the format of the ```ca810040-6727-4500-895d-f2258bbebf83 ```  which I found to be somewhat inconvenient. As a result, I stored result in the following (key-value) format: ```imageName: ca810040-6727-4500-895d-f2258bbebf83 ```, where imageName was treated as key.
- **Clarifai**
  - Perhaps the easiest package to install and employ from the following APIs. First, create account and get you API Key. 
  Second, open terminal and type the following command: ``` pip install clarifai```
  - Clarifai provides many different models such as apparel, food, demographics, and face detection. However, for the purpose of this post, I used [face detection](https://clarifai.com/models/face-detection-image-recognition-model/a403429f2ddf4b49b307e318f00e528b)
  - Installation guide can be found [here](https://clarifai.com/developer/guide/)
  - You can use my code (written in python) located in clarifai folder that are titled:
      - For [demo.py](https://github.com/AlmasM/ReviewFaceRecognition/blob/master/clarifai/demo.py) if you want to test a single image. 
        - Change API key : *app*
        - Input: image path (string) to variable *fName*
        - Output: prints out string in JSON format 
      - For [celebrity_test.py](https://github.com/AlmasM/ReviewFaceRecognition/blob/master/clarifai/celebrity_test.py) if you want to test folder. 
        - Change API key : change variable *app*
        - Input: directory *inputDir*
        - Output: 2 txt files named vectors.txt and identified.txt
          - [identified.txt](https://github.com/AlmasM/ReviewFaceRecognition/blob/master/clarifai/idenfied.txt) is a text file that has the following format: ```imageName : identified face or not```
          - [vector.txt](https://github.com/AlmasM/ReviewFaceRecognition/blob/master/clarifai/vectors.txt) is a text file where you get ```imageLocationPath : either 1024 vector representation or [] if no image```
              
- **face_recognition**
    - My tutorial on how to install face_recognition package can be found [here](https://github.com/AlmasM/EmotionDetection#installing-face-recognition-package-using-dlib)
      - Note: installing package requires only 1 line of code. However, you must get DLIB to work properly, which is usually the hardest part.
    - Peculiar thing about this package is that it can take only 1 image as a training sample (i.e. you can't provide more than 1 training sample for each face you want to identify/recognize).
    - Based on OpenFace and Dlib, face_recognition package is easy to implement and has 99% accuracy rate on LFW benchmark. Written by [Adam Geitgey](https://github.com/ageitgey) who also has [blog posts](https://medium.com/@ageitgey) with tutorials


**Step 3** Testing

- All the images given to Testing APIs were already cropped images from Faster RCNN. The images (faces) given were from TV show 'Friends' Episode 2 Season 6
- Although all the images passed where identified as 'face' by Faster RCNN, Testing packages 

| Face Recognition API | Identified | Recognized | Total | % (Identfied) | % (Recognized)
| --- | --- | --- | --- | --- | --- |
| Microsoft Azure |10,725 | 6038 | 11261 | 95% | 53%
| Clarifai | 2765 | 4558 | 60%
| face_recognition | 1661 | 3119 | 43% 

- Using the following table to compare 3 APIs is not quiet accurate. The reason is that the total amount of 

- **Note** the discrepancy of total varies due to fact that Azure allows only 10,000 calls/month, and Clarifai 5,000 calls/month. Package face_recognition is open source, but 
