from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("C:/Users/Minh Hung/Downloads/best.pt")

# Run inference on an image
results = model("D:/Study/tntgmt/jetson_iuh/yolo-seg-tuan3/img243.jpg")  # list of 1 Results object