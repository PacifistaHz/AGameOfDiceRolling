import random
import cv2

photos=["1.png","2.png","3.png","4.png","5.png","6.png"]
photos=photos*20
random.shuffle(photos)
for i in range(0,20):
    photo=cv2.imread(photos[i])
    cv2.imshow("Image",photo)
    cv2.waitKey(100)
    if i==19:
        cv2.waitKey(0)
    cv2.destroyAllWindows()