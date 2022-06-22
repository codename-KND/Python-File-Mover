getfile = os.listdir(sourcee)
for g in getfile:
    shutil.move(sourcee +g, destinationn)
    print('done')
