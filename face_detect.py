import numpy as np
import cv2


def view_img(filepath):
    image = cv2.imread(filepath)
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


filepath = "/home/gliu/Downloads/1.jpeg"
view_img(filepath)

imagePath = '/home/gliu/Downloads/1.jpeg' #sys.argv[1]
#cascPath = 'haarcascades/haarcascade_frontalcatface.xml' #sys.argv[2]
#cascPath = 'haarcascades/haarcascade_frontalcatface_extended.xml' #sys.argv[2]
#cascPath = 'haarcascades/haarcascade_frontalface_alt.xml' #sys.argv[2]
#cascPath = 'haarcascades/haarcascade_frontalface_alt_tree.xml' #sys.argv[2]
#cascPath = 'haarcascades/haarcascade_frontalface_alt2.xml' #sys.argv[2]
cascPath = 'haarcascades/haarcascade_frontalface_default.xml' #sys.argv[2]
# cascPath = 'haarcascades/haarcascade_fullbody.xml' #sys.argv[2]
# cascPath = 'haarcascades/haarcascade_eye.xml' #sys.argv[2]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1, ##1.1
    minNeighbors=5,  ##5
    minSize=(20, 20), ##30, 30
    flags = cv2.CV_FEATURE_PARAMS_HAAR #.cv.CV_HAAR_SCALE_IMAGE
)

print ("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print(x,y,w,h)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
