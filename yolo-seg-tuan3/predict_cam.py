import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("lastlast.pt")

# Open the video file
video_path = "yolo-seg-tuan3/video_data.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO inference on the frame
        results = model(frame)

        # Extract the detections
        for result in results:
            # Get boxes, scores, and class names
            boxes = result.boxes.xyxy  # Bounding boxes (x1, y1, x2, y2)
            scores = result.boxes.conf  # Confidence scores
            class_ids = result.boxes.cls  # Class IDs
            class_names = [model.names[int(cls_id)] for cls_id in class_ids]  # Convert class IDs to names

            # Print the detected attributes for each object
            for i in range(len(boxes)):
                print(f"Object {i+1}:")
                print(f"  Class: {class_names[i]}")
                print(f"  Confidence: {scores[i]:.2f}")
                print(f"  Bounding box: {boxes[i].numpy()}")  # Convert to numpy array for easier reading

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLO Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
