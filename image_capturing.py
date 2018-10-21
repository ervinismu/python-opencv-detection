import cv2
import os

# create object zero for external camera
video = cv2.VideoCapture(0)

# define variable
a = 0

while True:
    a = a + 1
    
    # frame object
    check, frame = video.read()
    
    # showing check and frame in terminal log
    print(check)
    print(frame)
    
    # converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # please replace this variable with your folder path for save image in folder
    path = None
    
    # show frame
    cv2.imshow("captureing", gray)
    
    if path is None:
        cv2.imwrite('image_{}.jpg'.format(a), frame)
    else:
        cv2.imwrite(os.path.join(path , 'image_{}.jpg'.format(a)), frame)

    # for playing
    key = cv2.waitKey(2)
    
    # key for close capturing video
    if key == ord('q'):
        break

# show how many milisecond the stream will take
print('number of photos: ', a)

# shutdown the camera
video.release()
cv2.destroyAllWindows
