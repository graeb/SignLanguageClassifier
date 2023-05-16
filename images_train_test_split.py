#Rozdzielanie zbioru danych na zbiór uczenia, walidacji i testowy
import os
import shutil
from sklearn.model_selection import train_test_split

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

for name in names:
    TRAINING_FILE = "C:\\Users\\graeb\\code\\inzynierka\\datasets\\degree_256_hands\\dataset_jpg_classes\\" + name
    DESTINATION_TRAIN = "C:\\Users\\graeb\\code\\inzynierka\\datasets\\degree_256_hands\\train\\" + name
    DESTINATION_TEST = "C:\\Users\\graeb\\code\\inzynierka\\datasets\\degree_256_hands\\test\\" + name
    DESTINATION_VAL = "C:\\Users\\graeb\\code\\inzynierka\\datasets\\degree_256_hands\\val\\" + name

    data_full = [label for label in os.listdir(TRAINING_FILE)]
    # print(data_full)
    data_test_val, data_train = train_test_split(data_full, test_size=0.7, random_state=99)
    data_test, data_val = train_test_split(data_test_val, test_size=0.5, random_state=99)

    for files in data_train:
            shutil.copy(TRAINING_FILE + '\\' + files, DESTINATION_TRAIN)

    for files in data_test:
            shutil.copy(TRAINING_FILE + '\\' + files, DESTINATION_TEST)

    for files in data_val:
            shutil.copy(TRAINING_FILE + '\\' + files, DESTINATION_VAL)
