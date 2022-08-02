import cv2,os,shutil
import numpy as np
import argparse
from glob import glob
from sys import exit
import csv
from pathlib import Path
from os.path import exists 

par_dir = '/home/robin/Work/fruitfly/test/'
csv_fln = '/home/robin/Work/fruitfly/done_images.csv'

file_exists = exists(csv_fln) 
if not file_exists:
    print("new csv file created")
    Path(csv_fln).touch()

with open(csv_fln, 'r') as csvfile:
    reader = csv.reader(csvfile)
    temp_list = list(reader) 
    read_list = temp_list if len(temp_list)==0 else temp_list[0]


for fln in (glob("/home/robin/Work/fruitfly/test/*/*", recursive=True)):
    fname=fln.rpartition('/')[-1]
    name = fln.split('/')[-2]+' - '+fln.split('/')[-1]
    
    if fname in read_list:
        continue
    read_list.append(fname)
        
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
            # writing to csv file 
            with open(csv_fln, 'w') as csvfile: 
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerow(read_list)
                
            cv2.destroyAllWindows()
            exit(0)
