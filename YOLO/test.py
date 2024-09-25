from ultralytics import YOLO
import cv2 
# Load a pretrained YOLOv8n-pose Pose model
model = YOLO("YOLO/v1.pt")

# Run inference on an image

# img =cv2.imread("/home/anh/workspace/IUH/YOLO/images/img1.jpg")
# cv2.imshow("h", img) 

# cv2.waitKey(0)
results = model.predict("/home/anh/workspace/IUH/YOLO/images/img1.jpg")  # results list

for result in results:
    # Duyệt qua từng đối tượng dự đoán trong ảnh
    for box in result.boxes:
        print('===================')

        cls_id = int(box.cls)  # Lấy id của lớp đối tượng
        confidence = box.conf  # Lấy giá trị độ tin cậy
        label = model.names[cls_id]
        # print(f'Label: {label}, Confidence: {confidence:.2f}')
        # print(label)
        print('lable type ' + str(type(label)))
        print('cls type '+ str(type(cls_id)))
        print('conf type '+str(type(confidence)))

        print(cls_id)
        print(confidence)
cv2.waitKey(0)