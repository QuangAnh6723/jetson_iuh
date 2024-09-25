import cv2

from ultralytics import YOLO

# Load the YOLOv8 model
# model = YOLO("yolov8n.pt")
model = YOLO("YOLO/v1.pt")


# Open the video file
video_path = "/home/anh/workspace/IUH/YOLO/video/nhieumau.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        for box in results[0].boxes:
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

        print(pl)
        print(conf_max)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()