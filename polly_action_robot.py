'''
Developer: Yaxshiliqov Javlon Qaxramon o'g'li
skills: Hardware and Software engineer (A.I , D.S )
telephone: +99894 463 70 30
Robot_name : THE GRYPHON

This software was developed by Yakhshilikov Javlon for Arm Robot.

Please appreciate someone's hard work
'''

from sklearn.preprocessing import PolynomialFeatures
import cv2
import Action_1
import joblib
from pyfirmata import Arduino, util
import Reles_action



# connector software with hardware
port = Arduino('COM10')
it = util.Iterator(port)
it.start()




# Suniy intellect " Object detection model "------------------------------
net = cv2.dnn.readNet('yolov4-tiny-custom_final.weights', 'yolov4-tiny-custom.cfg')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)



# Joints activator Artificial inteligance
model_jointer = joblib.load('polly_15_v3.joblib')



cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)


# Activators -----------------------------------------------
poly = PolynomialFeatures(degree=15)
act = Action_1.Action(port= port)
rel = Reles_action.Reles_action(port=port)
servo = port.get_pin('d:3:s')
servo.write(90)


def magnit(a):
    port.digital[2].write(a)


done  = True
while done:
    _, frame = cap.read()

    (class_ids, scores, boxes) = model.detect(frame)
    for (id, score, box) in zip(class_ids, scores, boxes):
        (x, y, h, w) = box
        if score >= 0.5:
            a, b = int((h + 2*x)/2), int((w+2*y)/2)
            X_ = poly.fit_transform([[a , b]])

            jointer = model_jointer.predict(X_)
            a1, a2, a3 = int(jointer[0][0]), int(jointer[0][1]), int(jointer[0][2])



            # act.Action(a1 , a2, a3)
            # magnit(1)
            #
            # act.Action(0, a2*(-1))
            # act.Action(0 , 0 , a3*(-1))
            # act.Action(a1*(-1))
            #
            #
            # rel.pozitsion(1, 4)
            # act.Action(0 , 60  , -70)
            # magnit(0)
            # act.Action(0, -60)
            # act.Action(0, 0 , 70)
            # rel.pozitsion(4 , 1)
            #
