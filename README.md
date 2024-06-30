# Object-DetectInator
Object DetectInator is a simple web application built with the Flask framework. It lets users upload an image/video and detect the objects in it using the YOLO v9 model. The information is then shown to the user and saved in MongoDB in Json Format.Uploaded images and the output images are saved in the local file. 
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

Donwload YoloV9c

    ``` wget https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-converted.pt ```

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

Detection in images




# Tools Used : 

![Flask](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/c9f08ab3-6179-4d3f-8010-a466e8e76b49) ![OpenCV](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/1ae6f603-fadf-47b7-9273-d127232579cd) ![MongoDB](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/34e6444d-7c1e-4f04-aefb-0637092c6690) ![YoloV9](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/d76d3d9e-cc95-41d0-9063-bb55fd6a69e0) ![Visual Studio Code](https://github.com/pranayvaranasi/Object-DetectInator/assets/142153387/98238cea-4cc4-4911-b3aa-2c108ed526b5) 




