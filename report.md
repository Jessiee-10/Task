# Player Re-Identification in Sports Footage  
**Selected Task Option: Cross-Camera Player Mapping**  
**Candidate: Mellam Jessica** 
**Company: Liat.ai**  
**Role: AI Intern**

---

## 🔍 1. Objective

The objective of this assignment is to detect and track players across two different camera feeds — `broadcast.mp4` and `tacticam.mp4` — and assign consistent `player_id` values to each individual, even when viewed from different angles.

---

## ⚙️ 2. Approach and Methodology

### 🔹 Object Detection
Used the provided `YOLOv11` model to perform player detection on each frame from both videos.

### 🔹 Feature Extraction
Extracted HSV color histograms from the detected player regions to represent appearance-based features.

### 🔹 Cross-Camera Mapping
Compared features between players in both feeds using **Euclidean distance** to assign the same ID to visually similar players across camera views.

### 🔹 ID Assignment
Implemented a logic where each new player’s features were matched against the existing pool:
- If a match was found (distance < threshold), the same ID was used.
- Otherwise, a new ID was assigned.

---

## 🛠️ 3. Techniques Tried & Outcomes

| Technique | Outcome |
|----------|---------|
| HSV Color Histogram Matching | ✅ Worked well in many cases with consistent lighting |
| IOU-based Matching | ❌ Not usable due to different perspectives |
| Static Thresholding | ✅ Helped assign consistent IDs across feeds |
| Real-time Frame Matching | ✅ Performed adequately in simulation |

---

## 🚧 4. Challenges Faced

- Significant **camera angle variation** made matching challenging.
- Lighting and jersey colors were not always distinct.
- Some players had visually similar uniforms, leading to **ID conflicts**.
- The threshold required careful tuning to avoid false matches.

---


## ✅ 5. Summary

This project successfully built a working prototype for player re-identification across multiple camera feeds using classical computer vision techniques.  
The solution is lightweight, real-time, and can be improved further using deep learning-based feature embeddings and tracking algorithms.

---

## 📎 Attachments

- `main.py`: Main script for video reading, detection, and display
- `tracker.py`: Class handling ID assignment and feature matching
- `utils.py`: Feature extraction logic
- `best.pt`: Model used for detection
- `broadcast.mp4` and `tacticam.mp4`: Input videos
