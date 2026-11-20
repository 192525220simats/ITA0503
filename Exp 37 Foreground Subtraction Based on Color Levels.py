


import cv2
import numpy as np

def subtract_foreground(image_path, lower_color, upper_color):

    # Read the image
    image = cv2.imread(image_path)

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define foreground color range
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Extract the background
    background = cv2.bitwise_and(
        image, image, mask=mask
    )

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Subtracted Image", background)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = "C:/Users/Thanuja P/Downloads/New folder (2)/input_image.jpg"

lower_color = [0, 50, 50]
upper_color = [120, 255, 255]

subtract_foreground(image_path, lower_color, upper_color)
