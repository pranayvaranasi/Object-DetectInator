#run and solve the error
from flask import Flask, request, session, render_template
import os
import json
import pandas as pd
import numpy as np
import io
import nest_asyncio
from enum import Enum
from utils import filetype, drawbox, adddata
import warnings
from PIL import Image
warnings.filterwarnings('ignore')
app = Flask(__name__, template_folder='templates', static_folder='C:/Users/pranay/ObjectDetectInator/static')
upload = 'C:/Users/pranay/ObjectDetectInator/static/uploads'
output = 'C:/Users/pranay/ObjectDetectInator/static/output'
app.config['upload'] = upload
app.secret_key='secret'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#app.config["MONGO_URI"] = "mongodb://localhost:27017"
os.path.dirname("C:/Users/pranay/ObjectDetectInator/templates")
@app.route('/')
def main():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def uploadfile():
    if not os.path.exists(app.config['upload']):
        os.makedirs(app.config['upload'])
    img = request.files['file uploaded']
    filename = img.filename
    session['filename'] = 'uploads/'+str(filename)
    filetype(filename)
    img.save(os.path.join(app.config['upload'],filename))
    session['uploaded_img_file_path'] = os.path.join(app.config['upload'],filename)
    return render_template('index.html', success=True)
@app.route('/show_file')
def showimage():
    imgpath="file:///"+session.get('uploaded_img_file_path', None).replace('\\', '/')
    if imgpath.split('.')[-1] in ('png', 'jpg', 'jpeg', 'gif', 'png', 'webp'):
        return render_template('showfile.html', img=session.get('filename'), isimage=True, showbutton = True)
    return render_template('showfile.html', img=imgpath, isimage=False, showbutton = True)
@app.route('/detect')
def detect():
    uploadedimgpath = session.get('uploaded_img_file_path', None)
    outputname, type , response= drawbox(uploadedimgpath)
    if type == 'image':
        return render_template('showfile.html', img=outputname, isimage=True, showbutton = False)
    return render_template('showfile.html', img=outputname, isimage=False, showbutton = False)
if __name__ == '__main__':
    app.run(debug=True)


