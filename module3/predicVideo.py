import cv2

from ultralytics import YOLO

model = YOLO("qaqbest.pt")

# Open the video file
video_path = "D:/Study/tntgmt/YOLO/dataset/video_check.mp4"
cap = cv2.VideoCapture(0)

# Loop through the video frames
# if __name__ == '__main__': # can khi chay bang GPU
        
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame, conf = 0.7)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

    # Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()