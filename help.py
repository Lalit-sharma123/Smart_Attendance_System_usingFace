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

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Corrected window size
        self.root.title("Face Recognition System")
        
        title_lbl=tk.Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top= Image.open(r"C:\Users\sharm\OneDrive\Desktop\face_recognition system\college_images\helpdeskimage.jpg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)  # Corrected resize and method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        # Label to display the image
        f_lbl = tk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
        
        dev_label=Label(f_lbl,text="Email:sharmaalalit55@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=550,y=220)
        
        
        
        
if __name__ == "__main__":
    root = tk.Tk()  # Corrected tk.TK() to tk.Tk()
    obj = Help(root)
    root.mainloop()