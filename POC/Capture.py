import cv2
import datetime


# capture frames from a video
cap = cv2.VideoCapture()
cap.open('rtsp://admin:calsoft@1234@172.17.4.76:554')

time_stamp = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
image_name = 'camera_192_168_255_64_55_' + time_stamp + '.jpg'

while cap.isOpened():
    time_stamp = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    image_name = 'camera_192_168_255_64_55_' + time_stamp + '.jpg'

    # reads frames from a video
    ret, frames = cap.read()
    # Saves the frames with timestamp in current directory
    cv2.imwrite(image_name, frames)
    # Wait for 'q' key to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# De-allocate any associated memory usage
cap.release()
cv2.destroyAllWindows()















