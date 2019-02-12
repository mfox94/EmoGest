import numpy as np
import keras
import cv2
import scipy.misc
import pandas as pd

#hand_cascade = cv2.CascadeClassifier('haarcascade/cascade4.xml')
model = keras.models.load_model("gesture_recog_NL.h5")

def img_to_mnist(img, i):
    new_img = cv2.resize(img,(28,28))
    new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    #scipy.misc.imsave('test/'+str(i)+'.jpg', new_img)
    new_img = new_img.reshape(1, 28, 28, 1)
    return new_img
	
def index_to_label(index):
    labels = ['fist', 'stop', 'question', 'ok']
    return labels[index]

cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

i = 0
# Read until video is completed
while (cap.isOpened()):
    i += 1
    # Capture frame-by-frame
    ret, frame = cap.read()
    new_img = img_to_mnist(frame, i)
    new_img = new_img/255
    prediction = model.predict(new_img)
    if (prediction.max() >= 0.8):
        print(prediction)
        label = index_to_label(prediction.argmax())
        print(label,prediction.max(),'\n')
    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()