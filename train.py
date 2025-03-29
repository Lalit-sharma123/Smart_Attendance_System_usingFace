import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Frame
from tkinter import LabelFrame
from tkinter import RIDGE
from tkinter import Label
from tkinter import W
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Corrected window size
        self.root.title("Face Recognition System")
        
        
        title_lbl=tk.Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top= Image.open(r"C:\Users\sharm\OneDrive\Desktop\face_recognition system\college_images\IMG-20250317-WA0010.jpg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)  # Corrected resize and method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        # Label to display the image
        f_lbl = tk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)
        
        # button
        b1_1=tk.Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)
        
        img_bottom= Image.open(r"C:\Users\sharm\OneDrive\Desktop\face_recognition system\college_images\photos.jpeg")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)  # Corrected resize and method
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        # Label to display the image
        f_lbl = tk.Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #===============Train the classifier And save========
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
            
        
        







if __name__ == "__main__":
     root=tk.Tk()  
     obj = Train(root)
     root.mainloop()
        