import cv2
import os


def convert_to_grayscale(image, output_folder):
    """
    Convert the input image to grayscale and save the result.
    """

    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    output_path = os.path.join(output_folder, "grayscale.jpg")
    cv2.imwrite(output_path, grayscale)

    print("✓ Grayscale conversion completed.")
    print(f"Saved as: {output_path}")

    return grayscale