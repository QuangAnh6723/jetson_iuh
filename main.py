# from misc import arm, lcd, led, motor
from misc import  motor
from misc.config import *

def main():
    print('start')

    model = YOLO("v1.pt")

    cap = cv2.VideoCapture(0) # open camera
    
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
                
            if pl != cls_id_odd:
                print("==========ket qua cuoi cung=========")
                print(pl)
                print(conf_max)
                arm.go_pos(pl)
                cls_id_odd = pl

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break





if __name__ == "__main__" :
    motor.init()
    led.init()
    lcd.int()
    arm.init()

    main()