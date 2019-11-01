from guizero import App, Text, TextBox, PushButton
import cv2
from datetime import datetime

un = "Jay"
pw = "letmein"
cam = cv2.VideoCapture(0)  # set camera
cam.set(cv2.CAP_PROP_FPS, 60)  # set FPS
cam.set(3, 1920)  # x axis resolution
cam.set(4, 1080)  # y axis resolution
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX  # set font
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # set codec (*'DVIX')
out = cv2.VideoWriter('What.avi', fourcc, 20, (1280, 720))


def check_user():
    if un_box.value == un and pw_box.value == pw:
        message = Text(app, text="Access Granted")
    else:
        message = Text(app, text="Incorrect")
        while True:
            re, img = cam.read()  # set camera read

            img = cv2.flip(img, 1)  # flip image

            cv2.putText(img, "Enemy Spotted", (300, 400), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

            cv2.putText(img, str(datetime.now()), (1000, 675), font, .5, (0, 0, 255), 1, cv2.LINE_AA)

            cv2.imshow('Security Camera', img)  # display window

            out.write(img)

            k = cv2.waitKey(30) & 0xff
            if k == 27:  # pres ESC to quit
                break


app = App(title="Hello GUI")

message = Text(app, text='Enter Username and Password')
message = Text(app, text=' ')
message = Text(app, text='Username')
un_box = TextBox(app)
message = Text(app, text='Password')
pw_box = TextBox(app)
message = Text(app, text=' ')
submit = PushButton(app, command=check_user)
app.display()
