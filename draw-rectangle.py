import cv2
import numpy as np

#VAR

#True while mouse button down, false while up
drawing = False
ix, iy = -1, -1

#FUNCTIONS
def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

#SHOW IMAGE


#BLACK
img = np.zeros((512, 512, 3))

cv2.namedWindow(winname='Drawing')

cv2.setMouseCallback('Drawing', draw_rectangle)

while True:

    cv2.imshow('Drawing', img)

    # CHECKS FOR ESc
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows