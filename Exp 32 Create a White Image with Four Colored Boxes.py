import numpy as np
import cv2

def create_colored_corners(image_size):

    height, width = image_size

    # Create white image
    image = np.ones(
        (height, width, 3), dtype=np.uint8
    ) * 255

    # Calculate box size
    box_h = height // 10
    box_w = width // 10

    # Top-left - Black
    image[0:box_h, 0:box_w] = [0, 0, 0]

    # Top-right - Blue
    image[0:box_h, width-box_w:width] = [255, 0, 0]

    # Bottom-left - Green
    image[height-box_h:height, 0:box_w] = [0, 255, 0]

    # Bottom-right - Red
    image[height-box_h:height, width-box_w:width] = [0, 0, 255]

    # Display image
    cv2.imshow("Colored Corners Image", image)

    cv2.imwrite("colored_corners_output.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get user input
user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))

create_colored_corners((user_height, user_width))
