import shutil
import os
from xml.dom.minidom import Element
#cmd gen txt
#todo look for py function
with open ("done.txt") as file:
    array1 = set(file.readlines())

 #constant EDMS file       
with open ("bigfile.txt") as file2:
    array2 = set(file2.readlines())
array3= []
for element in array2:
    if element not in array1:
        array3.append(element)

###to do get rid of this write function
with open("newarr4.txt","w")as out:
    out.writelines(array3)

#regular changed
filsor = r"C:\Users\LENY\Desktop\code\mieeen\folder" + '\\'
targfol = r"C:\Users\LENY\Desktop\code\mieeen\targfold" + '\\'

with open ("newarr4.txt") as file:
    subset = set(file.readlines())
list =[]

for line in subset:
    list.append(line.strip())

#move function

getfile = os.listdir(filsor)
##todo add array3 here instead of list
for g in getfile:
    for element in list:
        if g == element:
            shutil.move(filsor +g, targfol)