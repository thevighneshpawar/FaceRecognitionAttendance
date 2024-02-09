from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from PIL._imaging import font
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition")

        #    variables
        # self.var_


        # first image
        img = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\chatboat.jpeg")
        img = img.resize((530, 130))
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=530, height=130)

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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1480,height=600)

        # lef label side

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details ",font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=10,width=730,height=580)

        img_left = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\developer.jpeg")
        img_left = img_left.resize((720, 130))
        self.photoimage_left = ImageTk.PhotoImage(img2)

        f_lbl = Label(Left_frame, image=self.photoimage_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Cour\se ",font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        # Department
        dep_label=Label(current_course_frame,text="Deparrtment",font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman", 12, "bold"),state="readonly")
        dep_combo["values"]=("select deparmrent","sce","it","mech","civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # DCourse
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("select deparmrent", "FE","SE","TE","B,Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("select year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # DSemester
        sem_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10)

        sem_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly")
        sem_combo["values"] = ("select  Semester","sem1","sem2","sem3","sem4","sem5","sem6","sem7","sem8",)
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Clas Student Information ",font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)

        #Student id
        StudentId_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        StudentId_label.grid(row=0, column=0, padx=10,sticky=W)

        StudentId_entry=ttk.Entry(class_student_frame,width=20, font=("times new roman", 12, "bold"))
        StudentId_entry.grid(row=0,column=1,padx=10 , sticky=W)

        #Student name
        StudentName_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        StudentName_label.grid(row=0, column=2, padx=10,sticky=W)

        StudentId_entry=ttk.Entry(class_student_frame,width=20, font=("times new roman", 12, "bold"))
        StudentId_entry.grid(row=0,column=3,padx=10 , sticky=W)

        #Student division
        StudentDivision_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        StudentDivision_label.grid(row=1, column=0, padx=10,sticky=W)

        StudentId_entry=ttk.Entry(class_student_frame,width=20, font=("times new roman", 12, "bold"))
        StudentId_entry.grid(row=1,column=1,padx=10 , sticky=W)

        # rOLL NO
        Student_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        StudentId_label.grid(row=0, column=2, padx=10,sticky=W)

        StudentId_entry=ttk.Entry(class_student_frame,width=20, font=("times new roman", 12, "bold"))
        StudentId_entry.grid(row=0,column=1,padx=10 , sticky=W)

        #Student Name
        StudentId_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        StudentId_label.grid(row=0, column=2, padx=10,sticky=W)

        StudentId_entry=ttk.Entry(class_student_frame,width=20, font=("times new roman", 12, "bold"))
        StudentId_entry.grid(row=0,column=1,padx=10 , sticky=W)




        # right label side

        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details ",font=("times new roman", 12, "bold"))
        right_frame.place(x=780, y=10, width=660, height=580)



        # img4 = Image.open(r"C:\Users\suraj\PycharmProjects\FaceRecognitionAttendance\img\exit.jpeg")
        # img4 = img4.resize((1530, 710))
        # self.photoimage4 = ImageTk.PhotoImage(img4)
        #
        # b1 = Button(bg_img, image=self.photoimage4, cursor="hand2")
        # b1.place(x=600, y=100, width=270, height=270)




# =================================Generate data set or take  sample photo ===================
#     def generate_dataset(self):
#         if self.var_dep.get()=="Select Department " or self.var_std_name.get()=="" or self.va_s
#             messagebox.showerror("Error","all Field are rq",parent=self.root)
#         else:
#              try:
#
#                  conn=mysql.connector.connect(hodt="localhost",username="root",password="Suraj8956@")
#                  my_cursor=conn.cursor()
#                  my_cursor.execute("sekect * form student")
#                  myresult=my_cursor.fetchall()
#                  id=0
#                  for x  in myresult:
#                      id=id+1
#
#















if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()




