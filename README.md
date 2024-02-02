**Smart Attendance System**

## Project Overview

The Smart Attendance System is designed to automate the process of taking attendance using facial recognition technology. The system captures images from a webcam, recognizes faces, and records attendance in an Excel sheet. It consists of two main components: `capture_image_from_camera.py` for capturing images of individuals and `face_recognition_code.py` for recognizing faces and recording attendance.

### Components:

1. **capture_image_from_camera.py:**
   - This script captures images from a webcam for creating a database of known faces.
   - Users are prompted to enter their name, and the script captures an image using the webcam.
   - The captured image is saved with the person's name as the filename (e.g., "muaz.png").

2. **face_recognition_code.py:**
   - Utilizes the face_recognition and OpenCV libraries for facial recognition.
   - Reads known faces from the database created by `capture_image_from_camera.py`.
   - Displays live video from the webcam and recognizes faces in real-time.
   - Records attendance in an Excel sheet, marking individuals as "Present" when recognized.

### Setup:

1. **Dependencies:**
   - Install the required Python libraries: `face_recognition`, `cv2`, `xlwt`, `xlrd`, `xlutils`.

2. **Database Creation:**
   - Run `capture_image_from_camera.py` to capture images of individuals and create a database of known faces.

3. **Attendance Recognition:**
   - Run `face_recognition_code.py` for live attendance recognition using the webcam.

### Usage:

- Execute `capture_image_from_camera.py` to create a database of known faces by capturing images.
- Run `face_recognition_code.py` to start the live attendance recognition system.
- The system will display recognized faces and mark attendance in an Excel sheet.

**Note:** Ensure that the necessary dependencies are installed, new person is added in the face_recognition_code and the webcam is properly configured.