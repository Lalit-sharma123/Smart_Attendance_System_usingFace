import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from tkinter import Toplevel
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from tkinter import Frame
from tkinter import Label

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Corrected window size
        self.root.title("Face Recognition System")
        
        title_lbl=tk.Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top= Image.open(r"C:\Users\sharm\OneDrive\Desktop\face_recognition system\college_images\developerr.jpg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)  # Corrected resize and method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        # Label to display the image
        f_lbl = tk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
        
        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=580,height=600)
        
        img_top1= Image.open(r"C:\Users\sharm\OneDrive\Desktop\face_recognition system\college_images\me.jpg")
        img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)  # Corrected resize and method
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        
        # Label to display the image
        f_lbl = tk.Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)
        
        #Developer info
        dev_label=Label(main_frame,text="Hello my name,Lalit Sharma",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="I am Data Analytics",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=40)
        
        
        img2= Image.open(r"C:\Users\sharm\OneDrive\Desktop\face_recognition system\college_images\devebottomimg.jpg")
        img2 = img2.resize((500, 390), Image.Resampling.LANCZOS)  # Corrected resize and method
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = tk.Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=210, width=500, height=390)
        
        













if __name__ == "__main__":
    root = tk.Tk()  # Corrected tk.TK() to tk.Tk()
    obj = Developer(root)
    root.mainloop()