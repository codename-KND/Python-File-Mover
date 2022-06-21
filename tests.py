import os
import shutil
sourcee = r"C:\Users\LENY\Desktop\code\mieeen\folder"
destinationn = r"C:\Users\LENY\Desktop\code\mieeen\targfold"
getfile = os.listdir(sourcee)
for g in getfile:
    shutil.move(sourcee +g, destinationn)
    print('done')

