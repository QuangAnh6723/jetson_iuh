import cv2
import arm 
from ultralytics import YOLO
import time

model = YOLO("YOLO/v1.pt")

video_path = "./YOLO/video/nhieumau.mp4"
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        pl = -1
        conf_max = 0    
        for box in results[0].boxes:
            print('======== lay mau ===========')

            cls_id = int(box.cls)  
            confidence = box.conf 
            label = model.names[cls_id]

            print(cls_id)
            print(confidence)
            if( conf_max < confidence):
                conf_max = confidence
                pl = cls_id

        print("==========ket qua cuoi cung=========")
        print(pl)
        print(conf_max)
        arm.go_pos(pl)


        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()