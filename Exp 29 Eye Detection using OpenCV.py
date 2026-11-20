import cv2
import os

# Get program folder
folder = os.path.dirname(os.path.abspath(__file__))

# Load face classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Load eye classifier
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Read input image
image_path = os.path.join(folder, "eye_image.jpg")
image = cv2.imread(image_path)

if image is None:
    print("Error: eye_image.jpg not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, 1.1, 5
    )

    # Detect eyes
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray, 1.1, 5
        )

        # Draw rectangles around eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex+ew, ey+eh),
                (0, 255, 0), 2
            )

    print("Number of faces detected:", len(faces))

    # Display output
    cv2.imshow("Eye Detection", image)

    # Save output image
    cv2.imwrite(
        os.path.join(folder, "eye_output.jpg"), image
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()
