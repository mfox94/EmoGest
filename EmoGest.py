import numpy as np
# import keras
import cv2

hand_cascade = cv2.CascadeClassifier('haarcascade/cascade.xml')


# model = keras.models.load_model("gesture_recog.h5")

def img_to_mnist(img):
    new_img = cv2.resize(img, (28, 28))
    new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    new_img = new_img.reshape(1, 28, 28, 1)
    return new_img


cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)  # DETECTING HAND IN THE THRESHOLDE IMAGE)
    for (x, y, w, h) in hand:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # new_img = img_to_mnist(frame)
    # new_img = new_img/255
    # prediction = model.predict(new_img)
    # if (prediction.max() >= 0.7):
    #    print(prediction.argmax(),prediction.max())
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
