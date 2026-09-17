import os


def create_output_folder(output_folder):
    """
    Create the output folder if it does not already exist.
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


def check_input_image(image):
    """
    Check whether the input image was loaded successfully.
    """

    if image is None:
        print("ERROR: Could not load the input image.")
        return False

    return True