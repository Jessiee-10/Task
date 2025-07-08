import cv2
from ultralytics import YOLO
from tracker import PlayerTracker

# Load YOLOv11 model
model = YOLO("best.pt")

# Initialize trackers
broadcast_tracker = PlayerTracker("broadcast")
tacticam_tracker = PlayerTracker("tacticam")

# Load videos
cap1 = cv2.VideoCapture("broadcast.mp4")
cap2 = cv2.VideoCapture("tacticam.mp4")

frame_id = 0
while cap1.isOpened() and cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if not ret1 or not ret2:
        break

    results1 = model(frame1)
    results2 = model(frame2)

    broadcast_tracker.update(results1, frame1, frame_id)
    tacticam_tracker.update(results2, frame2, frame_id)

    # Show frames
    cv2.imshow("Broadcast View", broadcast_tracker.annotated_frame)
    cv2.imshow("Tacticam View", tacticam_tracker.annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_id += 1

cap1.release()
cap2.release()
cv2.destroyAllWindows()
