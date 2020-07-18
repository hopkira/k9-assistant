import face_recognition
import cv2
import numpy as np
import os
import time
import pickle

known_face_encodings = [] # a list of all the face encodings
known_face_names = [] # a list of the unique people that have been trained on
known_people = [] # the list of the people in each trained image

data = pickle.loads(open(args["encodings"], "rb").read())
detector = cv2.CascadeClassifier(args["cascade"])

vs = VideoStream(usePiCamera=True).start()

while True:
    frame = vs.read()
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30))
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
		matches = face_recognition.compare_faces(data["encodings"], encoding)
    cv2.rectangle(frame, (left, top), (right, bottom),
    (0, 255, 0), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    # display the image to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()