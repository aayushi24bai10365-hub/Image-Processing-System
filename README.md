# Image Enhancement and Edge Detection System

## Overview

The Image Enhancement and Edge Detection System is a Python-based Computer Vision project developed using OpenCV.

The project allows users to apply different image processing techniques to an input image through a simple menu-driven interface. The processed images are automatically saved in the output folder.

## Features

- Grayscale Conversion
- Gaussian Blur
- Canny Edge Detection
- Histogram Equalization
- Otsu Image Segmentation
- Run All Operations

## Technologies Used

- Python
- OpenCV
- Visual Studio Code
- Git
- GitHub

## Image Processing Operations

### 1. Grayscale Conversion

Converts the input colour image into a grayscale image.

Output file:

`output/grayscale.jpg`

### 2. Gaussian Blur

Applies Gaussian Blur using a 5 × 5 kernel to smooth the image and reduce noise.

Output file:

`output/blurred.jpg`

### 3. Canny Edge Detection

Detects important edges in the image using the Canny Edge Detection algorithm.

Output file:

`output/edges.jpg`

### 4. Histogram Equalization

Improves image contrast by redistributing the intensity values of the image.

Output file:

`output/enhanced.jpg`

### 5. Otsu Image Segmentation

Uses Otsu Thresholding to automatically determine a suitable threshold and create a binary image.

Output file:

`output/threshold.jpg`

### 6. Run All Operations

Runs all five image processing operations together and generates all output images.

## Project Structure

```text
Image-Processing-System/
│
├── modules/
│   ├── grayscale.py
│   ├── blur.py
│   ├── edge_detection.py
│   ├── enhancement.py
│   ├── segmentation.py
│   └── utils.py
│
├── output/
│   ├── grayscale.jpg
│   ├── blurred.jpg
│   ├── edges.jpg
│   ├── enhanced.jpg
│   └── threshold.jpg
│
├── input.jpg
├── main.py
├── requirements.txt
├── README.md
├── statement.md
└── .gitignore 
```
## Installation

### 1. Clone the Repository

Download the project from GitHub using:

```bash
git clone https://github.com/aayushi24bai10365-hub/Image-Processing-System.git