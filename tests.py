from importlib.metadata import files
import os
from re import sub
import shutil
sourcee = r"C:\Users\LENY\Desktop\code\mieeen\folder" + '\\'
destinationn = r"C:\Users\LENY\Desktop\code\mieeen\targfold" + '\\'


def movefile(sourcefolder, targetfolder, fold):
    try:
        for path,dir in os.walk(sourcefolder):
            if files:
                for file in dir:
                    if file in fold:
                        if not os.path.isfile(targetfolder + file):
                            os.rename(path + '\\' + file, targetfolder + file)
        print('done')
    except Exception as e:
        print(e)

with open ("files.txt") as file:
    subset = set(file.readlines())
list =[]

for line in subset:
    list.append(line.strip())


for element in list:
    movefile(sourcee,destinationn,element)