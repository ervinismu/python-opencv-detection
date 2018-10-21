import cv2

# create object zero for external camera
video = cv2.VideoCapture(0)

# define variable
a = 0

while True:
    a = a + 1

    # frame object
    check, frame = video.read()

    print(check)
    print(frame)

    # converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # show frame
    cv2.imshow("captureing", gray)

    # for press any key to out (miliseconds)
    #cv2.waitKey(0)

    # for playing
    key = cv2.waitKey(2)

    if key == ord('q'):
        break

# show how many milisecond the stream will take
print(a)

# shutdown the camera
video.release()

cv2.destroyAllWindows
