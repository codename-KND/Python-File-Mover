import shutil
import os
#naming folders to use for the move and listing source folder
targfol = r'C:\Users\LENY\Desktop\code\mieeen\targfold' + '\\'
filsor = r"C:\Users\LENY\Desktop\code\mieeen\folder" + '\\'
array1 = os.listdir(filsor)

# function for opening a file/list to be compared with source folder list
def select():
    with open ("files.txt") as file2:
        array = set(file2.readlines())

    array2 = []
    for line in array:
        array2.append(line.strip()) 

    array3= []
#making comparison between the lists
#listing the missing files in another list
    for element in array1:
        if element not in array2:
            array3.append(element + '\n')
#wrriting out the list of files to be moved  
    with open("newarr6.txt","w")as out:
        out.writelines(array3)
    return array3

#main function to move list
def mover():
    getfile = os.listdir(filsor)
    #calling the function to provide the list of files to be moved
    select()
    #reading the list
    with open ("newarr6.txt") as file:
        subset = set(file.readlines())
    list =[]

    for line in subset:
        list.append(line.strip())
    for g in getfile:
        for element in list:
            if g == element:
                shutil.move(filsor +g, targfol)

if __name__ == '__main__':
    mover()