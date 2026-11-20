import cv2
import os

folder = os.path.dirname(os.path.abspath(__file__))

# Read input image in grayscale
image_path = os.path.join(folder, "input_image.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
else:
    # Apply thresholding
    threshold_value = 127

    ret, segmented_image = cv2.threshold(
        image, threshold_value, 255, cv2.THRESH_BINARY
    )

    # Display original and segmented images
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented_image)

    # Save output
    cv2.imwrite(
        os.path.join(folder, "segmented_output.jpg"),
        segmented_image
    )

    print("Image segmentation completed")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
