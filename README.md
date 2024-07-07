# Object-DetectInator
Object DetectInator is a simple web application built with the Flask framework. It lets users upload an image/video and detect the objects in it using the YOLO v10 model. The information is then shown to the user and saved in MongoDB in Json Format.Uploaded images and the output images are saved in the local file. 
# Project Structure
```
├── app.py       # contains the Flask app object
├── utils.py
├── db.py
├── setup/
│   ├── requirements.txt
│   └── setup.sh 
├── static/   
│   ├── output # Output JSON and images stored here
│   └── uploads # User uploads saved here
└── templateFiles /
    ├── index.html
    └── show_file.html
└── README.md
```

# Steps for App Installation
1. Clone the App

     ``` git clone https://github.com/pranayvaranasi/Object-DetectInator ```

2. Create the Virtual Environment and Activate it

    ``` python3 -m venv flaskapp_env ```

    ```source flaskapp_env/bin/activate```

3.  Install Necessary Libraries

    ```pip3 install -r requirements.txt```

Donwload Yolov10n

    ``` wget https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10n.pt ```

Install Tensorflow and TorchVision

    ``` pip install tensorflow torchvision```

5. Set basic environmental variables

    ``` export FLASK_APP= app.py ```

    ```export FLASK_ENV=development ```

6. Run the application

   ``` python3 app.py ```

# App Overview

1. **Image/Video Upload:**
   - Users upload an image or video to Object DetectInator.
   - Upon upload, they are directed to an endpoint where they can view the media.

2. **Object Detection:**
   - When the user clicks "detect object," Object DetectInator performs object detection on the uploaded content.
   - The output includes detected objects, their coordinates (bounding boxes), and confidence scores.

3. **Saving Results:**
   - Results are saved in twoplaces:
     - Locally in JSON format along with the uploaded and output image.
     - JSON results in a MongoDB Atlas database.

4. **Database Fields:**
     - **Label:** A string representing the detected object (e.g., "car," "dog," etc.).
     - **Coordinates of Box:** The bounding box coordinates (usually represented as tensor that is converted to string).
     - **Confidence:** A float indicating the confidence score of the detection.
     - **Timestamp:** The date and time when the detection occurred .
     - **Image Metadata:** width and height of the uploaded image.
# Demonstration 

Click on the image below for video demonstration 👇

[![Object Detect Inator demonstration](https://res.cloudinary.com/drd8empws/image/upload/v1719215244/Object_DetectInator_logo_wlq4xd.jpg)](https://youtu.be/UVslmSBn8NI)


# Tools Used : 

![Flask](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/c9f08ab3-6179-4d3f-8010-a466e8e76b49) ![Jinja2](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/13a90906-8ff9-4399-8219-d116495ca87e)
 ![OpenCV](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/1ae6f603-fadf-47b7-9273-d127232579cd) ![MongoDB](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/34e6444d-7c1e-4f04-aefb-0637092c6690) ![Yolov10](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/fb1aa1f4-c528-4774-b987-88901fd498f3)
 ![HTML](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/d17bde79-ca56-4000-b29a-5fd3c8b70656)
 ![Visual Studio Code](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/98238cea-4cc4-4911-b3aa-2c108ed526b5) 

# Skills

Web Development, Computer Vision, Frontend, Database Management

Note to self :

Press q to stop video

Add current IP to Object DetectInator MongoDB atlas if server timeout




