import shutil
import os
from xml.dom.minidom import Element

filsor = r"C:\Users\LENY\Desktop\code\mieeen\folder" + '\\'
targfol = r"C:\Users\LENY\Desktop\code\mieeen\targfold" + '\\'

with open ("files.txt") as file:
    subset = set(file.readlines())
list =[]

for line in subset:
    list.append(line.strip())

getfile = os.listdir(filsor)

for g in getfile:
    for element in list:
        if g == element:
            shutil.move(filsor +g, targfol)