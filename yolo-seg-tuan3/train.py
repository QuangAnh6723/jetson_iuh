from ultralytics import YOLO

model = YOLO("yolov8n-seg.yaml")

model = YOLO("yolov8n-seg.pt")

results = model.train(data="coco8-seg.yaml", epochs=3)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model("https://ultralytics.com/images/bus.jpg")

# Export the model to ONNX format
success = model.export(format="onnx")