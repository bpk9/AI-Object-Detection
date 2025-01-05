from ultralytics import YOLO

# Load the best model from the training run
model = YOLO("./runs/detect/train/weights/best.pt")

# Generates a prediction result in ./runs/detect
model.predict(
    "./datasets/brian/test/img.jpg", 
    imgsz=640,
    save=True
)