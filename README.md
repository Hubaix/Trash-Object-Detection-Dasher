
# TrashCan Camera Project

This project uses a TrashCan Camera and Raspberry Pi to classify recyclable and non-recyclable objects using TensorFlow Runtime.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Windows](#windows)
  - [Linux](#linux)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
- Python 3.8 or higher
- Raspberry Pi (if deploying on the Raspberry Pi)
- Camera module
- TensorFlow Runtime

## Installation

### Windows
1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/trashcan-camera.git
    cd trashcan-camera
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. **Install the required packages**
    ```bash
    pip install -r requirements.txt
    ```

### Linux
1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/trashcan-camera.git
    cd trashcan-camera
    ```

2. **Create and activate a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Set paths for `IMAGE_DIR` and `ANNOTATIONS_DIR` in the `xmlconvert` script**
    Ensure that the paths are relative to the script's location in the `src/` folder.

2. **Run the project**
    ```bash
    python cv_code.py
    ```

3. **Deploy on Raspberry Pi**
    Ensure the camera module is connected and configured properly. Use the TensorFlow Lite model optimized for the Raspberry Pi.

## File Structure
```
trashcan-camera/
│
├── .gitignore
├── requirements.txt
├── src/
│   ├── xmlconvert
│   └── cv_code.py
└── models/
    └── torch_optimized_model.pt
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
