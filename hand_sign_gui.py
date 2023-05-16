import PySimpleGUI as sg
import cv2
import numpy as np
from pic_namer import pic_namer
import writing_to_csv as wtcsv
import time
from threading import Timer

FRAME_SIZE = (480,640) # camera gopro - (720,1280) // pc camera - (480,640)
BOX_SIZE = 256 #Should be divisible by 28 or whatever size your model uses
BOX_POS_TL = ((FRAME_SIZE[1]//2)-(BOX_SIZE//2),(FRAME_SIZE[0]//2)-(BOX_SIZE//2))
BOX_POS_BR = ((FRAME_SIZE[1]//2)+(BOX_SIZE//2),(FRAME_SIZE[0]//2)+(BOX_SIZE//2))
CLASS_NAMES = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
IMG_PATH_CSV = r"C:\\Users\graeb\code\inzynierka\datasets\degree_256_hands\dataset_csv\dataset.csv"
IMG_PATH_JPG = r"C:\\Users\graeb\code\inzynierka\datasets\degree_256_hands\dataset_jpg"

def one_hot_encode(CLASS_NAMES, header):
    header_encoded = CLASS_NAMES.index(header)
    return header_encoded
    
def img_ROI(frame, BOX_POS_TL, BOX_POS_BR):
    x1, y1 = BOX_POS_TL
    x2, y2 = BOX_POS_BR
    frame = frame[y1:y2,x1:x2] # our ROI
    return frame

# def img_capt(frame_original, BOX_POS_TL, BOX_POS_BR, CLASS_NAMES, IMG_PATH, values):
#     frame = img_ROI(frame_original, BOX_POS_TL, BOX_POS_BR)
#     header = values.get('letter_sign')
#     header_encoded = one_hot_encode(CLASS_NAMES, header)
#     wtcsv.writing_to_csv(IMG_PATH, frame, header_encoded)
    
def main():
    
    # GUI Theme
    sg.theme('Dark Green 5')
    
    # Timers
    st = time.time()
    el = 0
    
    # define the window layout
    layout = [[sg.Text('Hand Sign Detection', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Record', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Any 14'),
               sg.Button('Capture', size=(10, 1), font='Helvetica 14'),
               sg.Combo(CLASS_NAMES,default_value=CLASS_NAMES[0],key='letter_sign', size=(5,20)),
               sg.Button('Exit', size=(10, 1), font='Helvetica 14')],
              [sg.Button('Start', size=(10, 1), font='Helvetica 14'),
               sg.Button('Pause', size=(10, 1), font='Helvetica 14'), 
               sg.Combo([0.2,0.5,1,2,3,4,5], default_value=1, key='freq', size=(5,20))]]

    # create the window and show it without the plot
    window = sg.Window('Hand Sign Annotation',
                       layout, location=(800, 400))

    # Event LOOP Read and display frames, operate the GUI
    cap = cv2.VideoCapture(0)
    recording = False
    timer_loop = False
    
    while True:
        
        event, values = window.read(timeout=20)
        
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return

        elif event == 'Record':
            recording = True
        
        elif event == 'Stop':
            recording = False
            img = np.full(FRAME_SIZE, 255)
            imgbytes = cv2.imshow('Camera', frame)
            window['image'].update(data=imgbytes)

        if recording:
            ret, frame_original = cap.read()
            try:
                frame = frame_original.copy()
            except AttributeError:
                pass
            frame = cv2.rectangle(frame, BOX_POS_TL, BOX_POS_BR, (255,0,0), 3)
            imgbytes = cv2.imshow('Camera', frame)
            window['image'].update(data=imgbytes) 
                      
            if event == 'Capture':
                frame_original = img_ROI(frame_original, BOX_POS_TL, BOX_POS_BR)
                header = values.get('letter_sign')
                header_encoded = one_hot_encode(CLASS_NAMES, header)
                wtcsv.writing_to_csv(IMG_PATH_CSV, frame_original, header_encoded)
                txt = pic_namer(IMG_PATH_JPG, header, 'image', 'jpg')
                cv2.imwrite(txt,frame_original)
                
            if event == 'Start':
                timer_loop = True
                
            if event == 'Pause':
                el = 0
                timer_loop = False
                continue
   
            if timer_loop == True:
                fre = values.get('freq')
                if fre <= el:
                    frame_original = img_ROI(frame_original, BOX_POS_TL, BOX_POS_BR)
                    header = values.get('letter_sign')
                    header_encoded = one_hot_encode(CLASS_NAMES, header)
                    wtcsv.writing_to_csv(IMG_PATH_CSV, frame_original, header_encoded)
                    
                    txt = pic_namer(IMG_PATH_JPG, header, 'image', 'jpg')
                    cv2.imwrite(txt,frame_original)
                    
                    frame = cv2.rectangle(frame, BOX_POS_TL, BOX_POS_BR, (5,5,255), 12)
                    imgbytes = cv2.imshow('Camera', frame)
                    window['image'].update(data=imgbytes)
                    
                    el = 0
                    st = time.time()
                                                
                else:
                    et = time.time()
                    el = et - st
        
if __name__ == '__main__':
    main()
