import cv2


net = cv2.dnn.readNet('yolov4-tiny-custom_final.weights', 'yolov4-tiny-custom.cfg')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)


cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)



while True:
    _, frame = cap.read()

    (class_ids, scores, boxes) = model.detect(frame)
    for (id, score, box) in zip(class_ids, scores, boxes):
        (x, y, h, w) = box
        if score >= 0.5:
            cv2.rectangle(frame, (x, y), (x+h, y+w), (255, 0 , 0))
            a , b = int((h +2*x)/2) , int((w+2*y)/2)
            print(' a' , a , '  ' , 'b' , b)


            cv2.putText(frame , str(id), (x , y - 10)  , cv2.FONT_HERSHEY_PLAIN , 1 ,  (255 , 0 , 0)  )
            cv2.circle(frame, (a, b), 2, (30, 30, 0), 2)

    cv2.line(frame , (0 , 240) , (1500 , 240) , (0 , 0 , 0) , 2)
    cv2.line(frame , (660 , 0) , (660 , 900), (0 , 0 , 0) , 2)

    cv2.imshow('video', frame)
    cv2.waitKey(1)