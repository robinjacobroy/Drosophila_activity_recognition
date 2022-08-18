#!mkdir -p ./to_predict/{attempt_copulate,following,licking,wing_song,orientation} 
import cv2,os,shutil
import numpy as np
from glob import glob
from sys import exit
from os.path import exists 

par_dir = '/home/robin/Work/fruitfly/to_predict/'


for fln in (glob("/home/robin/Work/fruitfly/unsorted/*", recursive=True)):
    fname = fln.rpartition('/')[-1]
    name = fln.split('/')[-2]+' - '+fln.split('/')[-1]
           
    img = cv2.imread(fln)
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name,img)
    
    while(1):
        k=cv2.waitKey(0) & 0xFF
        if k==ord("a"):
            cv2.destroyAllWindows()
            shutil.move(fln, par_dir+'attempt_copulate/'+fname)
            break
        if k==ord("f"):
            cv2.destroyAllWindows()
            shutil.move(fln, par_dir+'following/'+fname)
            break
        if k==ord("l"):
            cv2.destroyAllWindows()
            shutil.move(fln, par_dir+'licking/'+fname)
            break
        if k==ord("w"):
            cv2.destroyAllWindows()
            shutil.move(fln, par_dir+'wing_song/'+fname)
            break
        if k==ord("o"):
            cv2.destroyAllWindows()
            shutil.move(fln, par_dir+'orientation/'+fname)
            break
        
        if k==27:             
            cv2.destroyAllWindows()
            exit(0)
