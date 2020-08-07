import face_recognition
import cv2
import pickle
import glob, os

knownEncodings = []

os.chdir("./images")
for file in glob.glob("*.png"):
    print("[INFO] processing image" + str(file))
    image = cv2.imread(file)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
        knownEncodings.append(encoding)
data = {"encodings": knownEncodings}
f = open("encodings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()