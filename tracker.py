import cv2
from utils import extract_features

class PlayerTracker:
    def __init__(self, name):
        self.name = name
        self.players = {}
        self.annotated_frame = None
        self.next_id = 1

    def update(self, results, frame, frame_id):
        self.annotated_frame = frame.copy()

        for det in results[0].boxes.xyxy:
            x1, y1, x2, y2 = map(int, det)
            crop = frame[y1:y2, x1:x2]
            features = extract_features(crop)

            # Assign a new ID (you can add matching logic later)
            player_id = self.next_id
            self.players[player_id] = features
            self.next_id += 1

            # Draw box and ID
            cv2.rectangle(self.annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(self.annotated_frame, f'ID: {player_id}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
