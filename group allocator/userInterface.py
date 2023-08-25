# this is the userInterface for the App

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import functionality as f
import os

#array to add on file name to the path of the python files:
filePathArr = []




# here is the ui box made for the interface

root = tk.Tk()


#combo box input for easier data input:
fileNamesList = os.listdir("C:\\Users\\user\\OneDrive - Files\\Desktop\\group allocator\\filesToBeRead")

for filePath in fileNamesList:
    filePathArr.append('filesTobeRead/'+ filePath)



ttk.Label(root, text='file path').pack(padx=30)
entry1 = ttk.Combobox(root, values=filePathArr, state='readonly')
entry1.pack()



#second label
ttk.Label(root, text='number of pple in group').pack(padx=20)
entry2 = ttk.Entry(root)
entry2.pack(pady=20)


#function that generates the next window on click of generate with the groups:
def generateGrps():
    resultFrame = tk.Toplevel(root)
    ttk.Label(resultFrame, text=f.nameAllocator(f.randomizeArray(f.fileArray(entry1.get())),int(entry2.get()))).pack()
    
    
   

ttk.Button(root, text='generate', command=generateGrps).pack(pady=20)





root.mainloop()