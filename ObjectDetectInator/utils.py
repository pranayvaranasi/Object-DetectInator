
from cvlib.object_detection import draw_bbox
import cv2
import cvlib as cv
import os
import json
import datetime
import db
from bson import json_util
import numpy as np
from imageai.Detection import VideoObjectDetection
from flask_pymongo import PyMongo
from flask import current_app as app
import tensorflow as tf
from werkzeug.exceptions import HTTPException
from ultralytics import YOLO
global output, upload, model
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
upload = 'C:/Users/pranay/ObjectDetectInator/static/uploads'
output = 'C:/Users/pranay/ObjectDetectInator/static/output'
model = YOLO('yolov9c.pt')

def filetype(filename):
        extension = filename.split('.')[-1] in ('png', 'jpg', 'jpeg', 'gif', 'png', 'webp', 'mp4', 'mov', 'avi')
        if not extension:
             raise HTTPException(status_code=415, detail="Unsupported file format")
def drawbox(imgpath: str, model = model, confidence=0.2):
       if imgpath.split('.')[-1] in ('png', 'jpg', 'jpeg', 'gif', 'png', 'webp'):
           img = cv2.imread(imgpath)
           box, label, conf = predict(img,model)
           for l, c in zip(label, conf):
                 print(f"Detected object: {1} with confidence of  {c}")
           outputimg = drawpredictedbox(img, box, label, conf)
           name = imgpath.split('/')[-1].split('.')[0].split('\\')[-1]
           outputimgpath = os.path.join(output, 'outputimg_{name}.jpg'.format(name=name))
           print(f"Saving processed image to {outputimgpath}")
           cv2.imwrite(outputimgpath, outputimg)
           response = writeresponse(box, label, conf, width = img.shape[1], height = img.shape[0])
           writejson(os.path.join(output,f"{name}.json") , data=response)
           type = 'image'
           outputname='output/'+'outputimg_{name}.jpg'.format(name=name)
           return outputname, type, response
       else:
             print("\nVideo file uploaded")
             return detectvideo(imgpath, model, confidence)
def writeresponse(box, label, conf, width, height):
      response = dict()
      response['Cordinates of box']=str(box)
      response['Labels']=label
      response['Confidence']=float(conf)
      now = datetime.datetime.now()
      timestamp = str(now.strftime("%Y-%m-%d_%H:%M:%S"))
      response['Timestamp'] = str(timestamp)
      response['Metadata']={'width':width, 'height':height}
      adddata(response)
      return response
def writejson(path, data):
      with open(path, 'w+') as f:
            json.dump(data, f)
def detectvideo(vidpath, model = str, confidence=float):
      name = vidpath.split('/')[-1].split('.')[0].split('\\')[-1]
      oupath = os.path.join(output, f'outputvid_{name}.mp4')
      cap = cv2.VideoCapture(vidpath)
      width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)+0.5)
      height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)+0.5)
      size = (width, height)
      fourcc = cv2.VideoWriter_fourcc(*'MJPG')
      fps = int(round(cap.get(5)))
      response = dict()
      while cap.isOpened():
            ret, frame = cap.read()
            height, width, _ = frame.shape
            if not ret:
                  print("Can't receive frame. Exiting ...")
                  break
            frame = cv2.flip(frame, 1)
            box, label, conf = predict(frame, model=model)
            outputframe = drawpredictedbox(frame, box, label, conf)
            out = cv2.VideoWriter(oupath, fourcc, 10.0, (640,480))
            out.write(outputframe)
            print("Video Playing")
            cv2.imshow('frame', outputframe)
            response['response']=(writeresponse(box, label, conf, width, height))
            k = cv2.waitKey(1)
            if k == 113: #presss q to stop the video
                  break
      cap.release()
      out.release()
      cv2.destroyAllWindows()
      writejson(os.path.join(output, "outresponse_{name}.json".format(name=name)), data=response)
      type = 'video'
      return vidpath, type, response['response']
def adddata(response):
    rs = json.loads(json_util.dumps(response))
    db.db.collection.insert_one(rs)
def predict(img, model):
      results = model.predict(img)
      for result in results:
            for x in result.boxes:
                  box= x.xyxy
                  label = result.names[int(x.cls)]
                  conf = x.conf
      return box, label, conf
def drawpredictedbox(img,box,label,conf):
      cv2.rectangle(img, (int(box[0][0]), int(box[0][1])),
                          (int(box[0][2]), int(box[0][3])), (255, 0, 0), 2)
      cv2.putText(img, f"{label}",
                        (int(box[0][0]), int(box[0][1]) - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0),1)
      return img