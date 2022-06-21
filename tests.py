import os
import shutil
sourcee = 'C:\Users\LENY\Desktop\code\folder'
destinationn = 'C:\Users\LENY\Desktop\code\targfold'
getfile = os.listdir(sourcee)
for g in getfile:
    shutil.move(sourcee +g, destinationn)
    print('done')

