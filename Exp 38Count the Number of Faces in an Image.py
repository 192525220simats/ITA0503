



import cv2

def play_video_reverse_slow(video_path):

    # Read the video
    cap = cv2.VideoCapture(video_path)

    frames = []

    # Extract all frames
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    # Play frames in reverse
    for frame in reversed(frames):

        cv2.imshow(
            'Reverse Slow Motion Video', frame
        )

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

# Example usage
play_video_reverse_slow('C:/Users/Thanuja P/Downloads/New folder (2)/video.mp4')
