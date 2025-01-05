from os import path
from ultralytics import YOLO

# Load the YOLO v8 model
# NOTE: If the model is not already downloaded, it will download the model automatically 
model = YOLO("yolov8m.pt")

# Get path to the data.yaml file
data_path = path.abspath("datasets/brian/data.yaml")

# Generates a training result in ./runs/detect
results = model.train(
    data=data_path, 
    device="mps",
    epochs=20
)