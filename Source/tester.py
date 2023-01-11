import pyfirmata
import Action_1
import cv2
import joblib
import numpy

model_1 = joblib.load('Random_forest.joblib')


net = cv2.dnn.readNet('yolov4-tiny-custom_final.weights', 'yolov4-tiny-custom.cfg')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)



cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)


port = pyfirmata.Arduino('COM10')
act = Action_1.Action(port= port)
aa = True
while aa:
    _, frame = cap.read()
    (class_ids, scores, boxes) = model.detect(frame)
    for (id, score, box) in zip(class_ids, scores, boxes):
        (x, y, h, w) = box
        if score >= 0.5:
            a , b = int((h +2*x)/2) , int((w+2*y)/2)
            xx = numpy.asarray([[a, b]])
            xx = model_1.predict(xx)
            a , b , c = xx[0][0] ,  xx[0][1] , xx[0][2]
            act.Action(a , b , c , 0 )
            aa =  False