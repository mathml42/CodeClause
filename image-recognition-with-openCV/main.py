import cv2
import numpy as np

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

web_cam = False
a = input("Use webcam? (y/n): ")
if a.lower() == 'y':
    web_cam = True
else:
    image_path = input("Enter path to image: ")

if web_cam:
    cap = cv2.VideoCapture(0)
else:
    frame = cv2.imread(image_path)
    if frame is None:
        print("Could not read the image.")
        exit()



while True:
    if web_cam:
        ret, frame = cap.read()
        if not ret:
            break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw an oval for the face
        center = (x + w // 2, y + h // 2)
        axes = (int(w // 2 * 0.9), int(h * 0.65)) 
        cv2.ellipse(frame, center, axes, 0, 0, 360, (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Eyes detection
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 8)
        for (ex, ey, ew, eh) in eyes:
            eye_center = (x + ex + ew//2, y + ey + eh//2)
            axes = (ew//2, int(eh*0.3)) 
            cv2.ellipse(frame, eye_center, axes, 0, 0, 360, (0, 255, 0), 2)
            cv2.circle(frame, eye_center, 2, (0, 255, 0), -1) 

        # Smile detection
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.5, 15)
        for (sx, sy, sw, sh) in smiles:
            if sy > h / 2:
                mouth_center_x = x + sx + sw // 2
                mouth_center_y = y + sy + sh // 2
                mouth_width = sw // 2
                mouth_height = sh // 6

                cv2.ellipse(frame, (mouth_center_x, mouth_center_y),
                            (mouth_width, mouth_height), 0, 0, 180, (255, 255, 0), 2)
                
                left_x = mouth_center_x - mouth_width
                right_x = mouth_center_x + mouth_width
                bottom_y = mouth_center_y

                cv2.line(frame, (left_x, bottom_y), (right_x, bottom_y), (255, 255, 0), 2)

                break  

    cv2.imshow("Facial Feature Detection", frame)
    if web_cam:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        cv2.waitKey(0)
        break
if web_cam:
    cap.release()
cv2.destroyAllWindows()
