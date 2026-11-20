
import numpy as np
import cv2

def create_circle_image(image_size):
    height, width = image_size

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Define circle center and radius
    center = (width // 2, height // 2)
    radius = min(width, height) // 4

    # Draw the circle (Blue color)
    cv2.circle(image, center, radius, (255, 0, 0), 2)

    # Display the image
    cv2.imshow("Circle Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))

create_circle_image((user_height, user_width))
