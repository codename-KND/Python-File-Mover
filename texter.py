from gettext import install
import numpy as np
with open ("done.txt") as file:
    array1 = set(file.readlines())

        
with open ("bigfile.txt") as file2:
    array2 = set(file2.readlines())
array3= []
for element in array2:
    if element not in array1:
        array3.append(element)
with open("newarr4.txt","w")as out:
    out.writelines(array3)