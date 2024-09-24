# Hand Landmark Detection with OpenCV and Mediapipe

This Python code uses OpenCV and Mediapipe to capture and process live video input from a webcam for real-time hand landmark detection. The code tracks the landmarks of one hand, draws connections between key points, and calculates the average frame rate (FPS) over time.

## Code Breakdown

1. **Library Initialization**:
   - OpenCV (`cv2`) is used to handle video input from the webcam and display the processed video.
   - Mediapipe (`mp`) is used for detecting and drawing hand landmarks.

2. **Hand Detection Setup**:
   - The Mediapipe Hands solution is initialized with one-hand detection (`max_num_hands=1`) and landmark drawing utilities are set up.

3. **Main Loop**:
   - The webcam video is captured frame by frame.
   - Each frame is converted from BGR to RGB, as required by Mediapipe.
   - Mediapipe processes the frame to detect hand landmarks.
   - If landmarks are found, they are drawn on the frame.
   - The frame is flipped horizontally before being displayed to provide a mirror effect.
   
4. **FPS Calculation**:
   - The FPS (frames per second) is calculated based on the time difference between consecutive frames.
   - The program calculates the average FPS over the entire session and prints it when the loop ends.

5. **Termination**:
   - The loop continues until any key is pressed (`cv2.waitKey(30)`), after which the average FPS is displayed.

## Summary

This code demonstrates how to use OpenCV and Mediapipe for real-time hand tracking and performance monitoring with FPS calculation.
