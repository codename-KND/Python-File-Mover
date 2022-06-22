getfile = os.listdir(sourcee)
for g in getfile:
    shutil.move(sourcee +g, destinationn)
    print('done')

modified = []
for line in read:
    modified.append(line.strip())

    if element not in sourcee:
        print('skipped')
    else:
def movefile(sourcefolder, targetfolder, fold):
    try:
        for path,dir, files in os.walk(sourcefolder):
            if files:
                for file in files:
                    if not os.path.isfile(targetfolder + file):
                        os.rename(path + '\\' + file, targetfolder + file)
        print('done')
    except Exception as e:
        print(e)

try:
        for path,dir, files in os.walk(sourcefolder):
            if files:
                for file in files:
                    if file in fold:
                        if not os.path.isfile(targetfolder + file):
                            os.rename(path + '\\' + file, targetfolder + file)
        print('done')