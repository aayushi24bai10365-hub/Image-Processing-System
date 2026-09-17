import cv2
import os


def enhance_image(image, output_folder):
    """
    Enhance image contrast using Histogram Equalization
    and save the result.
    """

    # Convert to grayscale if the image is in color
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    # Apply histogram equalization
    enhanced = cv2.equalizeHist(gray)

    output_path = os.path.join(output_folder, "enhanced.jpg")
    cv2.imwrite(output_path, enhanced)

    print("✓ Histogram enhancement completed.")
    print(f"Saved as: {output_path}")

    return enhanced