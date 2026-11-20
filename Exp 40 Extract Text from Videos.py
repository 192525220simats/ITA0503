





import cv2
import pytesseract

# Set Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_video(video_path):

    # Read the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video file")
        return

    print("Extracted Text from Video:")

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(
            frame, cv2.COLOR_BGR2GRAY
        )

        # Extract text using OCR
        text = pytesseract.image_to_string(
            gray_frame
        )

        if text.strip():
            print(text)

    cap.release()
    cv2.destroyAllWindows()


# Example usage
extract_text_from_video(
    r"C:\Users\Thanuja P\Downloads\New folder (2)\video.mp4"
)
