import cv2

import numpy as np

fn = np.zeros((413, 930, 3), np.uint8)
cv2.circle(fn, (630, 246), (786-630), (255, 255, 255), -1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread("tenis.jpg")
while True:
    img2 = cv2.bitwise_and(fn, img)
    cv2.putText(img, "Pelota verde", (451, 26), font,
                0.65, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("s", img2)
    k = cv2.waitKey(1)

    if k == ord('h'):
        break

cv2.destroyAllWindows()
