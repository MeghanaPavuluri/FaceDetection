import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('in.avi')


while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    print (type(faces))
  
    if len(faces) == 0:
        print ("No faces found")

    else:
        print (faces)
        print (faces.shape)
        print ("Number of faces detected: " + str(faces.shape[0]))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.rectangle(frame, ((0,frame.shape[0] -25)),(270, frame.shape[0]), (255,255,255), -1)
        cv2.putText(frame, "Number of faces detected: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
  

    cv2.imshow('frame',frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

plt.xlabel('No.of Faces')
plt.ylabel('Time Intervals')  

cap.release()
cv2.destroyAllWindows()
