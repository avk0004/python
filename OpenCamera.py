import cv2
from datetime import  datetime
capture = cv2.VideoCapture(0)
while True:
    r,f = capture.read()
    if not r:
        print("Camera Issue")
        break
    cv2.imshow("C to Capture E to Quite",f)

    k = cv2.waitKey(1)
    if k== ord('c') or k ==ord("C"):
        frame = datetime.now().strftime(r"./%Y-%m-%d-%H-%M-%S.png")
        cv2.imwrite(frame,f)
        print("STORED")
    elif k == ord("E") or k == ord('e'):
        break
capture.release()
cv2.destroyAllWindows()