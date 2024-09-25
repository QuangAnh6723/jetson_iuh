import arm 
from ultralytics import YOLO
import cv2 

model = YOLO("YOLO/v1.pt")

results = model("YOLO/images/img866.jpg")  # results list

pl = -1
conf_max = 0


for result in results:
    pl = -1
    conf_max = 0  

    for box in result.boxes:
        print('======== lay mau ===========')

        cls_id = int(box.cls)  # Lấy id của lớp đối tượng
        confidence = box.conf  # Lấy giá trị độ tin cậy
        label = model.names[cls_id]
        
        # print('lable type ' + str(type(label)))
        # print('cls type '+ str(type(cls_id)))
        # print('conf type '+str(type(confidence)))

        print(cls_id)
        print(confidence)
        if( conf_max < confidence):
            conf_max = confidence
            pl = cls_id

print("==========ket qua cuoi cung=========")
print(pl)
print(conf_max)
arm.go_pos(pl)
