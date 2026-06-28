import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

db_path = "database"

blink_count = 0
eyes_visible = False
LIVENESS = 3
is_live = False

cap = cv2.VideoCapture(0)
print("System started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) >= 2:
            if not eyes_visible:
                eyes_visible = True
        else:
            if eyes_visible:
                blink_count += 1
                eyes_visible = False

        if blink_count >= LIVENESS:
            is_live = True

    if is_live:
        try:
            result = DeepFace.find(
                img_path=frame,
                db_path=db_path,
                enforce_detection=False,
                silent=True
            )

            if len(result) > 0 and not result[0].empty:
                identity = result[0]['identity'][0]
                name = identity.split("\\")[-2]
                cv2.putText(frame, f" {name}!", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        except Exception as e:
            cv2.putText(frame, "Analyzing...", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        cv2.putText(frame, f"Blink ({blink_count}/{LIVENESS})", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)

    cv2.imshow("Face Recognition + Liveness", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
