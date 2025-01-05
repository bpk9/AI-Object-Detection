# AI Object Detection

This project uses [YOLOv8](https://yolov8.com/) for custom object detection. It's set up to train on custom datasets and perform predictions on images and videos.

**NOTE:** To protect the privacy of the data, the trained model weights as well as the training data is intentionally excluded from this repository.

## Setup

1. Clone this repository:
```bash
git clone https://github.com/bpk9/ai-object-detection.git
cd ai-object-detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
ai-object-detection/
├── datasets/          # Training and validation datasets
│   └── brian/         # Custom dataset (EX: "brian")
│       ├── train/     # Training images
│       ├── valid/     # Validation images
│       ├── test/      # Test images
│       └── data.yaml  # Dataset configuration
├── train.py           # Training script
└── predict.py         # Prediction script
```

## Dataset Generation

This project uses [Roboflow](https://roboflow.com/) for dataset preparation and annotation. To create your own dataset:

1. Create a free account on [Roboflow](https://roboflow.com/)

2. Create a new project:
   - Select "Object Detection" as the project type
   - Choose "YOLOv8" as the annotation format

3. Upload and annotate your images:
   - Upload your images to Roboflow
   - Use Roboflow's annotation tools to draw bounding boxes around objects
   - Label each object with the appropriate class name

4. Generate and export your dataset:
   - Add preprocessing steps if needed (resize, auto-orient, etc.)
   - Add augmentations to increase dataset size (optional)
   - Split your dataset (recommended: 70% train, 20% valid, 10% test)
   - Export in YOLOv8 format
   - Copy the exported dataset into your `datasets/` directory
   - Update the path to your dataset in [train.py](./train.py)

For more information on dataset preparation, visit [Roboflow's YOLOv8 Guide](https://docs.roboflow.com/export-format/yolov8).

## Training

The project uses [YOLOv8](https://yolov8.com/) as the base model for training. 

To train on your custom dataset:

1. Organize your dataset in the following structure:
   - `datasets/<your-dataset-name>/train/images/`: Training images (60%)
   - `datasets/<your-dataset-name>/valid/images/`: Validation images (20%)
   - `datasets/<your-dataset-name>/test/images/`: Test images (20%)

2. Update the `data_path` variable in [train.py](./train.py)

3. Run the training script:
```bash
python train.py
```

Training results will be saved in `runs/detect/train/`.

For additional documentation around training, see [Model Training with Ultralytics YOLO](https://docs.ultralytics.com/modes/train/)

## Prediction

To run predictions on new images or videos:

1. Specify the path to your trained model weights in [predict.py](./predict.py)

2. Run the prediction script:

```bash
python predict.py
```

Prediction results will be saved in `runs/detect/predict/`.

For additional documentation around generating predictions, see [Model Prediction with Ultralytics YOLO](https://docs.ultralytics.com/modes/predict/)

## Hardware Acceleration

The project is configured to use MPS (Metal Performance Shaders) for hardware acceleration on Apple Silicon Macs. Modify the `device` parameter in `train.py` if using different hardware:
- For NVIDIA GPU: `device="cuda"`
- For CPU: `device="cpu"`
- For Apple Silicon: `device="mps"`
