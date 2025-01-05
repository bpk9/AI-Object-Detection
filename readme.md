# AI Object Detection

This project uses [YOLOv8](https://yolov8.com/) for custom object detection. It's set up to train on custom datasets and perform predictions on images and videos.

## Additional Documentation

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

## Training

The project uses [YOLOv8](https://yolov8.com/) as the base model for training. 

To train on your custom dataset:

1. Organize your dataset in the following structure:
   - `train/images/`: Training images (60%)
   - `valid/images/`: Validation images (20%)
   - `test/images/`: Test images (20%)
   - Update `data.yaml` with your class names

2. Run the training script:
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
