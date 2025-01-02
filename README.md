# Underwater Pipeline Detection Dataset (YOLO Format)

This project provides a YOLO-format dataset for underwater pipeline detection, including training sets, validation sets, corresponding annotation files, and a class definition file (`classes.txt`).

---

## Dataset Contents

- **Training Set (train)**: Contains 6396 images and their corresponding annotation files.
- **Validation Set (val)**: Contains 1575 images and their corresponding annotation files.
- **Class File (classes.txt)**: Defines the names of all classes in the object detection task.

The dataset is fully compatible with the [YOLO format](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data) and works with frameworks like YOLOv4, YOLOv5, and YOLOv7.

---

## Directory Structure

```
project/
├── images/
│   ├── train/      # Training images
│   ├── val/        # Validation images
├── labels/
│   ├── train/      # Training annotations
│   ├── val/        # Validation annotations
├── classes.txt     # Class definition file
└── README.md       # Project description file
```

---

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/underwater-pipeline-dataset.git
   cd underwater-pipeline-dataset
   ```

2. Set up your YOLO environment (e.g., YOLOv5 or YOLOv7) and configure the dataset path in the `data.yaml` file:

   ```yaml
   train: /path/to/project/images/train
   val: /path/to/project/images/val

   nc: 2  # Number of classes (modify as needed)
   names: ['pipeline', 'other']  # Class names (modify based on classes.txt)
   ```

3. Run the training script:

   ```bash
   python train.py --data data.yaml --cfg yolov5s.yaml --epochs 50
   ```

---

## Data Format Explanation

- **Image Files**: Supported formats include `JPG`, `PNG`, etc.
- **Annotation Files**:
  - Each image has a corresponding `.txt` file with the same name.
  - Each line in the file represents one object, formatted as: `<class_id> <x_center> <y_center> <width> <height>`.
    - `class_id`: The class index, starting from `0`.
    - `x_center` and `y_center`: The normalized coordinates of the object’s center point (relative to the image size).
    - `width` and `height`: The normalized width and height of the bounding box (relative to the image size).

---

## Example Files

### Example Image and Annotation

#### Image

`images/train/sample.jpg`

#### Annotation

`labels/train/sample.txt` content example:

```
0 0.5 0.5 0.4 0.3
1 0.7 0.8 0.2 0.1
```

---



