from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from PIL._imaging import font
from student import  Student


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition")

        # first image
        img=Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\chatboat.jpeg")
        img = img.resize((530, 130))
        self.photoimage=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=530,height=130)

        # second image
        img1 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\face.jpeg")
        img1 = img1.resize((530, 130))
        self.photoimage1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimage1)
        f_lbl.place(x=500, y=0, width=530, height=130)

        # third image
        img2 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\developer.jpeg")
        img2 = img2.resize((530, 130))
        self.photoimage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=1000, y=0, width=530, height=130)

        # back ground images  image
        img3 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\bg3.jpeg")
        img3 = img3.resize((1530,710))
        self.photoimage3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimage3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # student button
        img4 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\exit.jpeg")
        img4 = img4.resize((1530,710))
        self.photoimage4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimage4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # face detector button
        img5 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\bg.jpeg")
        img5 = img5.resize((1530,710))
        self.photoimage5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimage5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        # Attendance button
        img6 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\student.png")
        img6 = img6.resize((1530, 710))
        self.photoimage6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimage6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Chat Bot button
        img7 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\student.png")
        img7 = img6.resize((1530, 710))
        self.photoimage7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimage7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="ChatBot", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train data button
        img8 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\student.png")
        img8 = img6.resize((1530, 710))
        self.photoimage8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimage8, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

        # photos button
        img9 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\bg.jpeg")
        img9 = img9.resize((1530, 710))
        self.photoimage9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimage9, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue",
                      fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        # Developer button
        img10 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\student.png")
        img10 = img10.resize((1530, 710))
        self.photoimage10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimage10, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        # Exit button
        img11 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\student.png")
        img11 = img11.resize((1530, 710))
        self.photoimage11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimage11, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()