import os 
import shutil

TRAINING_FILE = r"C:\Users\graeb\code\inzynierka\datasets\degree_256_hands\dataset_jpg"
DESTINATION = r"C:\Users\graeb\code\inzynierka\datasets\degree_256_hands\dataset_jpg_classes"

possible_labels = set([label[0] for label in os.listdir(TRAINING_FILE)])

# Tworzenie folderów dla każdej z klas
for x in possible_labels:
    try:
        os.mkdir(DESTINATION + '\\' + x)
    except FileExistsError:
        pass

#Grupowanie zdjęć po klasie i przeniesienie do odpowiedniego folderu
for files in os.listdir(TRAINING_FILE):
    for destination in possible_labels:
        if files[0] == destination:
            shutil.copy(TRAINING_FILE + '\\' + files, DESTINATION + '\\' + destination)
