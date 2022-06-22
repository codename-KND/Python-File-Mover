getfile = os.listdir(sourcee)
for g in getfile:
    shutil.move(sourcee +g, destinationn)
    print('done')

modified = []
for line in read:
    modified.append(line.strip())