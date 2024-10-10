import cv2
import numpy as np
from ultralytics import YOLO

def distance_to_contours(x, y, contours):
    distances = []
    closest_points = []
    point = (x, y)
    for contour in contours:
        distance = cv2.pointPolygonTest(contour, point, True)
        distances.append(abs(distance))
        
        # Find the closest point on the contour
        closest_point = min(contour, key=lambda p: cv2.norm((x, y) - p[0]))
        closest_points.append(tuple(closest_point[0]))
        
    return distances, closest_points

# Đường dẫn tới mô hình YOLO và video
model_path = "C:/Users/Minh Hung/Downloads/last7.pt"
video_path = "D:/Study/tntgmt/jetson_iuh/yolo-seg-tuan3/video_data.mp4"

# Tải mô hình YOLO
model = YOLO(model_path)

# Mở video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Không thể mở video từ đường dẫn: {video_path}")
    exit()

# Lấy thông tin về video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

if __name__ == '__main__': # can khi chay bang GPU
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Chuyển đổi frame sang không gian màu HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Định nghĩa khoảng màu xanh lá trong không gian màu HSV
        lower_green = np.array([40, 40, 40])
        upper_green = np.array([80, 255, 255])

        # Tạo mask để giữ lại các vùng màu xanh lá
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Áp dụng mask lên frame gốc
        green_only = cv2.bitwise_and(frame, frame, mask=mask)

        # Chuyển đổi frame đã lọc sang thang độ xám
        gray = cv2.cvtColor(green_only, cv2.COLOR_BGR2GRAY)

        # Áp dụng Gaussian Blur để làm mờ frame
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Sử dụng Canny Edge Detection để tìm biên
        edges = cv2.Canny(blur, 50, 150)

        # Tìm contours (đường viền) dựa trên ảnh biên
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Sắp xếp các contours dựa trên độ dài của chúng
        contours = sorted(contours, key=lambda x: cv2.arcLength(x, True), reverse=True)

        # Chỉ giữ lại 2 contours dài nhất
        longest_contours = contours[:2]

        # Run YOLOv8 inference on the frame
        results = model(frame, conf=0.7, device=0)

        # Extract the bounding box coordinates
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)

                # Calculate distances from the center of the bounding box to the contours
                distances, closest_points = distance_to_contours(center_x, center_y, longest_contours)
                print(f"Khoảng cách từ điểm ({center_x}, {center_y}) tới 2 đường viền dài nhất: {distances}")

                # Vẽ các đường thẳng lên frame gốc
                frame_with_lines = frame.copy()
                for contour in longest_contours:
                    [vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
                    lefty = int((-x * vy / vx) + y)
                    righty = int(((frame.shape[1] - x) * vy / vx) + y)
                    cv2.line(frame_with_lines, (frame.shape[1] - 1, righty), (0, lefty), (0, 255, 0), 2)

                # Vẽ điểm và khoảng cách lên frame
                cv2.circle(frame_with_lines, (center_x, center_y), 5, (0, 0, 255), -1)
                for i, (distance, closest_point) in enumerate(zip(distances, closest_points)):
                    text = f"Dist {i+1}: {distance:.2f}"
                    # Draw text with a black outline for better contrast
                    cv2.putText(frame_with_lines, text, (center_x + 10, center_y + 30 * (i + 1)), cv2.FONT_HERSHEY_PLAIN, 3.0, (255, 255, 255), 3)
                    # cv2.putText(frame_with_lines, text, (center_x + 10, center_y + 30 * (i + 1)), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
                    
                    # Draw line from center to closest point on contour
                    cv2.line(frame_with_lines, (center_x, center_y), closest_point, (0, 255, 255), 2)

                # Visualize the results on the frame
                annotated_frame = result.plot()

                # Combine the annotated frame with lines
                combined_frame = cv2.addWeighted(annotated_frame, 0.7, frame_with_lines, 0.3, 0)

                # Display the combined frame
                cv2.imshow("YOLOv8 Inference with Lines", combined_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video capture and writer objects and close the display window
    cap.release()
    cv2.destroyAllWindows()