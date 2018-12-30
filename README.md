 ________________________________________
|                                        |
| SECURITY CAMERA OFFICIAL DOCUMENTATION |
|________________________________________|

# IoT_Camera__Prototype
This repository holds the code and plans made for my IoT camera prototype

# SOFTWARE USED

- Python 2.7

- Virtual environment and virtual environment wrapper
  loaded in profile file (use 'source ~/.profile')

- Virtual Environment (use 'workon cvpy2')

- Numpy 1.15

- execute CMAKE with the following flags:
From: https://stackoverflow.com/questions/40262928/error-compiling-opencv-fatal-error-stdlib-h-no-such-file-or-directory
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
    -D ENABLE_PRECOMPILED_HEADERS=OFF \
    -D BUILD_EXAMPLES=ON ..

- Output result after cmake command was executed:
--   Python 2:
--     Interpreter:                 /home/pi/.virtualenvs/cvpy2/bin/python2.7 (ver 2.7.13)
--     Libraries:                   /usr/lib/arm-linux-gnueabihf/libpython2.7.so (ver 2.7.13)
--     numpy:                       /home/pi/.virtualenvs/cvpy2/local/lib/python2.7/site-packages/numpy/core/include (ver 1.15.3)
--     packages path:               lib/python2.7/site-packages
-- 
--   Python 3:
--     Interpreter:                 /usr/bin/python3 (ver 3.5.3)
--     Libraries:                   /usr/lib/arm-linux-gnueabihf/libpython3.5m.so (ver 3.5.3)
--     numpy:                       /usr/lib/python3/dist-packages/numpy/core/include (ver 1.12.1)
--     packages path:               lib/python3.5/site-packages
-- 
--   Python (for build):            /home/pi/.virtualenvs/cvpy2/bin/python2.7

- Run code:
cd Smart-Security-Camera-master/
source ~/.profile
workon cvpy2
python main.py



# Bugs

- First bug running my code in raspberry pi, this error did not happen in my mac. Error:
OpenCV Error: Assertion failed (scn == 3 || scn == 4) in cvtColor, file /home/pi/opencv-3.1.0/modules/imgproc/src/color.cpp, line 8000
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # face cinza obrigatorio pelo modelo de deteccao
error: /home/pi/opencv-3.1.0/modules/imgproc/src/color.cpp:8000: error: (-215) scn == 3 || scn == 4 in function cvtColor

Fix:https://stackoverflow.com/questions/35224730/trouble-with-raspberry-pi-and-opencv
sudo modprobe bcm2835-v4l2


# OTHER SOURCES

# Smart-Security-Camera
IoT Raspberry Pi security camera running open-cv for object detection. The camera will send an email with an image of any objects it detects. It also runs a server that provides a live video stream over the internet.

[Watch the original video here](https://youtu.be/Y2QFu-tTvTI)

## Setup

This project uses a Raspberry Pi Camera to stream video. Before running the code, make sure to configure the raspberry pi camera on your device.

Open the terminal and run

```
sudo raspi-config
```

Select `Interface Options`, then `Pi Camera` and toggle on. Press `Finish` and exit.

You can verify that the camera works by running

```
raspistill -o image.jpg
```
which will save a image from the camera in your current directory. You can open up the file inspector and view the image.

## Installing Dependencies

This project uses openCV to detect objects in the video feed. You can install openCV by using the following [tutorial](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/). I used the Python 2.7 version of the tutorial.

The installation took almost 8 hours (!!) on my Raspberry Pi Zero, but it would be considerably faster on a more powerful board like the Raspberry Pi 3.

The tutorial will prompt you to create a virtual environment. Make sure you are using the virtual environment by typing the following commands

```bash
source ~/.profile
workon cvpy2
```

Next, navigate to the repository directory

```
cd Smart-Security-Camera
```

and install the dependencies for the project

```
pip install -r requirements.txt
```

*Note: If you're running python3, you'll have to change the import statements at the top of the mail.py file*

```
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
```
*and change your print statements from quotes to parenthesis*

```
print "" => print()
```

## Customization

To get emails when objects are detected, you'll need to make a couple modifications to the `mail.py` file.

Open `mail.py` with vim `vim mail.py`, then press `i` to edit. Scroll down to the following section

```
# Email you want to send the update from (only works with gmail)
fromEmail = 'myemail@gmail.com'
fromEmailPassword = 'password1234'

# Email you want to send the update to
toEmail = 'anotheremail@gmail.com'
```
and replace with your own email/credentials. The `mail.py` file logs into a gmail SMTP server and sends an email with an image of the object detected by the security camera. 

Press `esc` then `ZZ` to save and exit.

You can also modify the `main.py` file to change some other properties.

```
email_update_interval = 600 # sends an email only once in this time interval
video_camera = VideoCamera(flip=True) # creates a camera object, flip vertically
object_classifier = cv2.CascadeClassifier("models/fullbody_recognition_model.xml") # an opencv classifier
```
Notably, you can use a different object detector by changing the path `"models/fullbody_recognition_model.xml"` in `object_classifier = cv2.CascadeClassifier("models/fullbody_recognition_model.xml")`.

to a new model in the models directory.

```
facial_recognition_model.xml
fullbody_recognition_model.xml
upperbody_recognition_model.xml
```

## Running the Program

Run the program

```
python main.py
```

You can view a live stream by visiting the ip address of your pi in a browser on the same network. You can find the ip address of your Raspberry Pi by typing `ifconfig` in the terminal and looking for the `inet` address. 

Visit `<raspberrypi_ip>:5000` in your browser to view the stream.

Note: To view the live stream on a different network than your Raspberry Pi, you can use [ngrok](https://ngrok.com/) to expose a local tunnel. Once downloaded, run ngrok with `./ngrok http 5000` and visit one of the generated links in your browser.

Note: The video stream will not start automatically on startup. To start the video stream automatically, you will need to run the program  from your `/etc/rc.local` file see this [video](https://youtu.be/51dg2MsYHns?t=7m4s) for more information about how to configure that.



