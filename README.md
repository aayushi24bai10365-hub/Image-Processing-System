# Image Enhancement and Edge Detection System

A Computer Vision project developed using Python and OpenCV for performing image processing operations such as grayscale conversion, Gaussian blurring, edge detection, image enhancement, and image segmentation.

## Project Overview

This project demonstrates fundamental image processing techniques using OpenCV.

The system provides a menu-driven interface where the user can select different image processing operations or run all operations together.

## Features

- Convert an image to Grayscale
- Apply Gaussian Blur
- Detect edges using Canny Edge Detection
- Enhance image using Histogram Equalization
- Segment image using Thresholding
- Run all image processing operations automatically
- Save processed images in an output folder

## Technologies Used

- Python
- OpenCV
- NumPy
- Git
- GitHub

## Image Processing Operations

### 1. Grayscale Conversion

Converts the input color image into a grayscale image.

This reduces the image from three color channels (BGR) to a single intensity channel.

### 2. Gaussian Blur

Gaussian Blur is used to reduce image noise and smooth the image.

It is particularly useful as a preprocessing step before edge detection.

### 3. Canny Edge Detection

Canny Edge Detection identifies important boundaries and edges within an image.

It can be used to detect objects and structural features.

### 4. Histogram Equalization

Histogram Equalization improves the contrast of an image by redistributing pixel intensity values.

This can make details more visible in images with poor contrast.

### 5. Image Segmentation

Thresholding separates regions of an image based on pixel intensity.

The resulting binary image can help distinguish objects from the background.

## Project Structure

```text
Image-Processing-System/
│
├── main.py
├── input.jpg
├── requirements.txt
├── README.md
├── .gitignore
│
└── output/
    ├── grayscale.jpg
    ├── blurred.jpg
    ├── edges.jpg
    ├── enhanced.jpg
    └── threshold.jpg