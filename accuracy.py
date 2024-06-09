
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import cv2
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
def sign():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=2)
    classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

    offset = 20
    imgSize = 300

    def dialogbox():
        root = tk.Tk()
        root.withdraw()
        folder = simpledialog.askstring(title="Gesture", prompt="Enter the gesture you want to show:")
        return folder
    
        

    def display_message(imgOutput, message):
        cv2.putText(imgOutput, message, (20, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


    folder = dialogbox()
    counter = 0

    labels = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9"]

    total_frames = 0
    correct_predictions = 0
    open_dialogbox = False  # Flag to control opening dialog box

    while True:
        success, img = cap.read()
        imgOutput = img.copy()
        hands, img = detector.findHands(img, flipType=False)

        if hands:
            hand_points = []
            for hand in hands:
                hand_points += hand["lmList"]

            hand_x = [p[0] for p in hand_points]
            hand_y = [p[1] for p in hand_points]
            x, y, w, h = min(hand_x), min(hand_y), max(hand_x) - min(hand_x), max(hand_y) - min(hand_y)
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

            imgCropShape = imgCrop.shape
            if imgCropShape[0] > 0 and imgCropShape[1] > 0:

                aspectRatio = h / w

                if aspectRatio > 1:
                    k = imgSize / h
                    wCal = math.ceil(k * w)
                    imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                    imgResizeShape = imgResize.shape
                    wGap = math.ceil((imgSize - wCal) / 2)
                    imgWhite[:, wGap:wCal + wGap] = imgResize
                    prediction, index = classifier.getPrediction(imgWhite, draw=False)

                else:
                    k = imgSize / w
                    hCal = math.ceil(k * h)
                    imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                    imgResizeShape = imgResize.shape
                    hGap = math.ceil((imgSize - hCal) / 2)
                    imgWhite[hGap:hCal + hGap, :] = imgResize
                    prediction, index = classifier.getPrediction(imgWhite, draw=False)
            else:
                print("Error: imgCrop is empty")

            # Calculate accuracy
            total_frames += 1
            if labels[index] == folder:
                correct_predictions += 1
                cv2.putText(imgOutput, f"Accuracy: 100%", (20, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2) # Set accuracy to 100%
                message = "CORRECT"
                open_dialogbox = True  # Open dialog box for new gesture
            else:
                # accuracy = 0.0 
                cv2.putText(imgOutput, f"Accuracy: 0%", (20, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2) # Set accuracy to 0%
                message = "WRONG"
            accuracy = correct_predictions / total_frames if total_frames > 0 else 0.0

            cv2.rectangle(imgOutput, (x - offset, y - offset - 50),
                        (x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
            cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset),
                        (x + w + offset, y + h + offset), (255, 0, 255), 4)
            display_message(imgOutput, message)


        cv2.imshow("Image", imgOutput)

        if open_dialogbox:
            folder = dialogbox()
            counter = 0
            open_dialogbox = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('r'):
            dialogbox()

    cap.release()
    cv2.destroyAllWindows()


