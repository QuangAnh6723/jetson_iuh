import cv2

# from ultralytics import YOLO

# Load the YOLOv8 model
# model = YOLO("last.pt")
# model = YOLO("D:/Study/tntgmt/runs/detect/train68/weights/best.pt")
# model = YOLO("D:/Study/tntgmt/runs/detect/train71/weights/last.pt")
# model = YOLO("./best.pt")

# Open the video file
# video_path = "D:/Study/tntgmt/YOLO/dataset/nhieumau.mp4"
cap = cv2.VideoCapture(0)

# Loop through the video frames
if __name__ == '__main__': # can khi chay bang GPU
        
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            # results = model(frame, conf = 0.7, device = 0)

            # Visualize the results on the frame
            # annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()