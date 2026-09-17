import cv2
import os

# ==========================================
# IMAGE ENHANCEMENT & EDGE DETECTION SYSTEM
# ==========================================

INPUT_IMAGE = "input.jpg"
OUTPUT_FOLDER = "output"


# ------------------------------------------
# Create output folder
# ------------------------------------------

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


# ------------------------------------------
# Load image
# ------------------------------------------

image = cv2.imread(INPUT_IMAGE)

if image is None:
    print("\nERROR: input.jpg was not found.")
    print("Please keep input.jpg in the same folder as main.py.")
    exit()

print("\nInput image loaded successfully!")


# ------------------------------------------
# Grayscale
# ------------------------------------------

def grayscale():

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(
        OUTPUT_FOLDER + "/grayscale.jpg",
        gray
    )

    print("\n✓ Grayscale image created.")
    print("Saved as: output/grayscale.jpg")


# ------------------------------------------
# Gaussian Blur
# ------------------------------------------

def blur():

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    cv2.imwrite(
        OUTPUT_FOLDER + "/blurred.jpg",
        blurred
    )

    print("\n✓ Gaussian blur completed.")
    print("Saved as: output/blurred.jpg")


# ------------------------------------------
# Canny Edge Detection
# ------------------------------------------

def edge_detection():

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    edges = cv2.Canny(
        blurred,
        100,
        200
    )

    cv2.imwrite(
        OUTPUT_FOLDER + "/edges.jpg",
        edges
    )

    print("\n✓ Canny edge detection completed.")
    print("Saved as: output/edges.jpg")


# ------------------------------------------
# Histogram Equalization
# ------------------------------------------

def histogram_enhancement():

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    enhanced = cv2.equalizeHist(gray)

    cv2.imwrite(
        OUTPUT_FOLDER + "/enhanced.jpg",
        enhanced
    )

    print("\n✓ Histogram enhancement completed.")
    print("Saved as: output/enhanced.jpg")


# ------------------------------------------
# Image Segmentation
# ------------------------------------------

def segmentation():

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    _, threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    cv2.imwrite(
        OUTPUT_FOLDER + "/threshold.jpg",
        threshold
    )

    print("\n✓ Image segmentation completed.")
    print("Saved as: output/threshold.jpg")


# ------------------------------------------
# Run all operations
# ------------------------------------------

def run_all():

    print("\nRunning all image processing operations...")

    grayscale()
    blur()
    edge_detection()
    histogram_enhancement()
    segmentation()

    print("\n✓ All operations completed successfully!")


# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:

    print("\n")
    print("=" * 50)
    print("     IMAGE PROCESSING SYSTEM")
    print("=" * 50)

    print("\n1. Convert to Grayscale")
    print("2. Apply Gaussian Blur")
    print("3. Detect Edges")
    print("4. Enhance Image")
    print("5. Segment Image")
    print("6. Run All Operations")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        grayscale()

    elif choice == "2":
        blur()

    elif choice == "3":
        edge_detection()

    elif choice == "4":
        histogram_enhancement()

    elif choice == "5":
        segmentation()

    elif choice == "6":
        run_all()

    elif choice == "7":
        print("\nThank you for using the Image Processing System!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 7.")