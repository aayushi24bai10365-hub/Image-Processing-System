import cv2
import os

def segment_image(image, output_folder):
    """
    Segment the image using Otsu Thresholding
    and save the result.
    """

    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    _, threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    output_path = os.path.join(output_folder, "threshold.jpg")
    cv2.imwrite(output_path, threshold)

    print("✓ Otsu image segmentation completed.")
    print(f"Saved as: {output_path}")

    return threshold