import numpy as np
import cv2
from sys import exit
from scipy.spatial import distance as dist


video_fn = "Downloads/Telegram Desktop/PC1Cam1__21919557__20220517_151739174.avi"
vs = cv2.VideoCapture(video_fn)

r =[]
ret, frame = vs.read()
cv2.namedWindow("fln", cv2.WINDOW_NORMAL)
r = cv2.selectROIs("fln", frame)
cv2.destroyWindow('fln')

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 100;

# Filter by Area.
params.filterByArea = True
params.minArea = 50
params.maxArea = 500

# Filter by Circularity
#params.filterByCircularity = True
#params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.1

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0
params.maxInertiaRatio = 1

detector = cv2.SimpleBlobDetector_create(params)

for i in range(len(r)):   
    x1, y1, wid, hig = r[i]
    
    vs = cv2.VideoCapture(video_fn)
    while True:
        # grab the current frame     
        frame = vs.read()[1]
        if frame is None:
            break
        orig = frame.copy()
        frame = frame[y1:y1+hig, x1:x1+wid]   
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        keypoints = detector.detect(gray)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        im_with_keypoints = cv2.drawKeypoints(gray, keypoints, np.array([]), (0,0,255),\
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                                      
                                      
        coords = np.around(cv2.KeyPoint_convert(keypoints)).astype(int)
        diameter = [round(x.size) for x in keypoints]
        
        if len(diameter)==1:
            cutout = orig[coords[0][1]-40+y1:coords[0][1]+40+y1, \
                           coords[0][0]-40+x1:coords[0][0]+40+x1]
        else:
            dis = dist.euclidean(coords[0] , coords[1])
            if dis<50:
                mid_x = (coords[0][0] + coords[1][0])//2
                mid_y = (coords[0][1] + coords[1][1])//2
                cutout = orig[mid_y-40+y1:mid_y+40+y1, mid_x-40+x1:mid_x+40+x1]
            else:
                cutout = frame.copy()
                  
        cv2.namedWindow("hi", cv2.WINDOW_NORMAL)
        #cv2.imshow('hi', cv2.bitwise_and(edges, canvas))
        cv2.imshow('hi', cutout)
        key = cv2.waitKey(1) & 0xFF
        # if the `q` key is pressed, break from the loop
        if key == ord("q") :
            break
        elif key == ord('p'):
            cv2.waitKey(0)
            continue
        elif key == 27:
            vs.release()
            cv2.destroyAllWindows()
            exit(0)
            

vs.release()
cv2.destroyAllWindows()
