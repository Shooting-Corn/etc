###pharsing

import cv2
import os
num = 0
print(cv2.__version__)
vidcap = cv2.VideoCapture('/content/gdrive/My Drive/darknet_detect/video/gun_video.mp4')
success,image = vidcap.read()
count = 0
save_count = 0
success = True
while success:
    if(int(vidcap.get(1)) % 25 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))

        path = '/content/gdrive/My Drive/darknet_detect/video_cut/'
        num += 1
        cv2.imwrite(os.path.join(path, "frame%d.png" % num), image)  
        save_count += 1
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    count += 1
