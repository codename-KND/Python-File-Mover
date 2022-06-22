from importlib.metadata import files
import os
import shutil
sourcee = r"C:\Users\LENY\Desktop\code\mieeen\folder" + '\\'
destinationn = r"C:\Users\LENY\Desktop\code\mieeen\targfold" + '\\'

def movefile(sourcefolder, targetfolder):
    try:
        for path,dir, files in os.walk(sourcefolder):
            if files:
                for file in files:
                    if not os.path.isfile(targetfolder + file):
                        os.rename(path + '\\' +file, targetfolder + file)
        print('done')
    except Exception as e:
        print(e)

movefile(sourcee,destinationn)