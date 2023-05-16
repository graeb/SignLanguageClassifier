import csv
import numpy as np
import cv2

def writing_to_csv(save_to, img, header):
    with open(save_to, 'a+', newline='') as f:
        csv_lst = []
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (28,28), interpolation = cv2.INTER_AREA) # resizing it to match our model
        img = img.flatten() # reshape to make it easy to save into csv file
        img = img.tolist()
        csv_lst.append(header)
        csv_lst.extend(img)
        writer = csv.writer(f)
        writer.writerow(csv_lst)
 