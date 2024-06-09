import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import os
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
offset = 20
imgSize = 400
counter = 0

folder = "images/9"

while True:
    sucess, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        if len(hands) == 1:
            hand = hands[0]
            x, y, w, h = hand["bbox"]
            imageWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            cv2.imshow("ImageCropped", imgCrop)

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCalc = math.ceil(w * k)

                wGap = math.ceil((imgSize - wCalc) / 2)

                imgResize = cv2.resize(imgCrop, (wCalc, imgSize))
                imageResizeShape = imgResize.shape
                imageWhite[:, wGap:wCalc + wGap] = imgResize

            else:
                k = imgSize / w
                hCalc = math.ceil(h * k)

                hGap = math.ceil((imgSize - hCalc) / 2)

                imgResize = cv2.resize(imgCrop, (imgSize, hCalc))
                imageResizeShape = imgResize.shape
                imageWhite[hGap:hCalc + hGap, :] = imgResize

            cv2.imshow("ImageSquared", imageWhite)

        elif len(hands) == 2:
            x1, y1, w1, h1 = hands[0]["bbox"]
            x2, y2, w2, h2 = hands[1]["bbox"]
            x, y = min(x1, x2), min(y1, y2)
            w, h = max(x1 + w1, x2 + w2) - x, max(y1 + h1, y2 + h2) - y
            imageWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            cv2.imshow("ImageCropped", imgCrop)

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCalc = math.ceil(w * k)

                wGap = math.ceil((imgSize - wCalc) / 2)

                imgResize = cv2.resize(imgCrop, (wCalc, imgSize))
                imageResizeShape = imgResize.shape
                imageWhite[:, wGap:wCalc + wGap] = imgResize

            else:
                k = imgSize / w
                hCalc = math.ceil(h * k)

                hGap = math.ceil((imgSize - hCalc) / 2)

                imgResize = cv2.resize(imgCrop, (imgSize, hCalc))
                imageResizeShape = imgResize.shape
                imageWhite[hGap:hCalc + hGap, :] = imgResize

            cv2.imshow("ImageSquared", imageWhite)

    cv2.imshow("VideoLive", img)
    key = cv2.waitKey(1)

    if key == ord('s'):
        counter += 1
        cv2.imwrite(f"{folder}/Image_{time.time()}.jpg",imageWhite)
        print(counter)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
