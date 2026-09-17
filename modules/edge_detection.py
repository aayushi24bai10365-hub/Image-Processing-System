import cv2
import os


def detect_edges(image, output_folder):
    """
    Detect edges using the Canny edge detection algorithm
    and save the result.
    """

    # Convert to grayscale if the image is still in color
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    edges = cv2.Canny(gray, 100, 200)

    output_path = os.path.join(output_folder, "edges.jpg")
    cv2.imwrite(output_path, edges)

    print("✓ Canny edge detection completed.")
    print(f"Saved as: {output_path}")

    return edges