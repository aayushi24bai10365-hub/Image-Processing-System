import cv2
import os


def apply_gaussian_blur(image, output_folder):
    """
    Apply Gaussian Blur to the input image and save the result.
    """

    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    output_path = os.path.join(output_folder, "blurred.jpg")
    cv2.imwrite(output_path, blurred)

    print("✓ Gaussian blur completed.")
    print(f"Saved as: {output_path}")

    return blurred