'''
Developer: Yaxshiliqov Javlon Qaxramon o'g'li
skills: Hardware and Software engineer (A.I , D.S )
telephone: +99894 463 70 30
Robot_name : THE GRYPHON


This software was developed by Yakhshilikov Javlon for Arm Robot.

Please appreciate someone's hard work
'''


import cv2
import Action_1
# import locator
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
model_jointer = joblib.load('Random_forest_V2.joblib')



cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)



# varible for locator package ------------------------------
# loc = locator.Locator(port=port)
# location = 1
# pozitsion = 0



# Activators -----------------------------------------------

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
            # cv2.rectangle(frame, (x, y), (x+h, y+w), (255, 0 , 0))
            a, b = int((h + 2*x)/2), int((w+2*y)/2)
            jointer = model_jointer.predict([[a, b]])
            a, b, c = int(jointer[0][0]), int(jointer[0][1]), int(jointer[0][2])
            act.Action(a , b, c)
            magnit(1)

            act.Action(0, b*(-1))
            act.Action(0 , 0 , c*(-1))
            act.Action(a*(-1))
            rel.pozitsion(1, 4)
            act.Action(0 , 60  , -70)
            magnit(0)
            act.Action(0, -60)
            act.Action(0, 0 , 70)
            rel.pozitsion(4 , 1)

            # pozitsiani obyeklar joylashuvida avtonom joylashitirish ----------------------------------------------------
            # pozitsion = loc.poz(a)
            # if location != pozitsion:
            #     if not pozitsion == 0:
            #         ac = Action_1.Action(port= port)
            #         loc.locator( location , b , a)
            #         location = loc.poz(a)





    #         cv2.putText(frame , str(id), (x , y - 10)  , cv2.FONT_HERSHEY_PLAIN , 1 ,  (255 , 0 , 0)  )
    #         cv2.circle(frame, (a, b), 2, (30, 30, 0), 2)
    #
    # cv2.line(frame, (0, 240), (1500, 240), (0, 0, 0), 2)
    # cv2.line(frame, (660, 0), (660, 900), (0, 0, 0), 2)


    # cv2.imshow('video', frame)
    # cv2.waitKey(1)