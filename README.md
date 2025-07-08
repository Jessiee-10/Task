
# Player Re-Identification in Sports Footage

## 🎯 Task: Cross-Camera Player Mapping

This project focuses on detecting and identifying players across two different camera feeds in a sports setting. The objective is to maintain consistent identities (\`player_id\`) for players appearing in both camera views: \`broadcast.mp4\` and \`tacticam.mp4\`.

---

## 🧠 Approach

- **Object Detection**: Used a pre-trained YOLOv11 model to detect players in each frame of both video feeds.
- **Feature Extraction**: Extracted HSV color histogram features from detected player regions.
- **Cross-Camera Matching**: Compared extracted features across feeds using Euclidean distance to assign consistent IDs.
- **ID Management**: If similarity exceeded a threshold, the same \`player_id\` was reused; otherwise, a new ID was assigned.

---

## 📁 Project Structure

\`\`\`
player-reid-cross-camera/
├── main.py         # Main script to process both video feeds
├── tracker.py      # Handles ID assignment and cross-camera logic
├── utils.py        # Utility functions for feature extraction, etc.
├── best.pt      # YOLOv11 model file (used for player detection)
├── broadcast.mp4   # First camera view input (not uploaded)
├── tacticam.mp4    # Second camera view input (not uploaded)
├── README.md       # Project overview and instructions
├── report.pdf      # Project report (approach, challenges, summary)
\`\`\`

---

## 🚀 How to Run

1. Place the following files in the root directory:
   - YOLOv11 model file: \`best.pt\`
   - Input videos: \`broadcast.mp4\` and \`tacticam.mp4\`

2. Run the project:

\`\`\`bash
python main.py
\`\`\`

This will open two video windows and display detected players with consistent IDs across both feeds.

---

## 📝 Report

See \`report.md\` for:
- Methodology
- Matching logic and thresholding
- Limitations and future enhancements

---

## 🧑‍💻 Author

- **Name**: Mellam Jessica
- **Role**: AI Intern Candidate at Liat.ai

---

## 📌 Notes

- The YOLO model and video files are expected to be in the same folder as the code.
- The model file and video inputs are not included in this repository due to size constraints.
- The logic can be extended with deep ReID models or integrated tracking algorithms like Deep SORT.

---


