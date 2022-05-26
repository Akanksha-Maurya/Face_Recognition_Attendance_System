from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        self.root.iconbitmap("face_attendance.ico")

        self.DepVar=StringVar()
        self.CourVar=StringVar()
        self.SessYVar=StringVar()
        self.SemVar=StringVar()
        self.IdVar=StringVar()
        self.SNameVar=StringVar()
        self.EmailVar=StringVar()
        self.Mob_NoVar=StringVar()
        self.GenderVar=StringVar()
        self.AddrVar=StringVar()

        #top image
        imge = Image.open(r"ImageFolder\studentm.png")
        imge = imge.resize((1300,200), Image.ANTIALIAS)
        self.imgPhoto = ImageTk.PhotoImage(imge)
        first_label = Label(self.root, image=self.imgPhoto)
        first_label.place(x=0, y=0, width=1300, height=200)

        #background image
        imge1 = Image.open(r"ImageFolder\bng-img.jpg")
        imge1 = imge1.resize((1300, 598), Image.ANTIALIAS)
        self.imgPhoto1 = ImageTk.PhotoImage(imge1)
        bng_img = Label(self.root, image=self.imgPhoto1)
        bng_img.place(x=0, y=130, width=1300, height=598)

        label_title = Label(bng_img, text="STUDENT MANAGEMENT SYSTEM", font=("Rubik", 30, "bold"), bg="#525252", fg="black")
        label_title.place(x=0, y=0, width=1300, height=45)

        Back_Button = Button(label_title, text="Back", command=self.root.destroy, font=("Rubik", 13, "bold"), width=14,bg="black", fg="white")
        Back_Button.pack(side=RIGHT)

        def time():
            string = strftime("%H:%M:%S %p")
            label.config(text=string)
            label.after(1000, time)

        label = Label(label_title, font=("Rubik", 18, "bold"), background="#525252", foreground="#293462")
        label.place(x=5, y=0, width=160, height=50)
        time()

        mainFrame=Frame(bng_img,bd=3,bg="#73777B")
        mainFrame.place(x=10,y=55,width=1250,height=440)

        leftFrame=LabelFrame(mainFrame,bd=3,bg="#73777B",relief=GROOVE,text="Student Details",font=("Rubik",16,"bold"))
        leftFrame.place(x=10,y=5,width=620,height=428)

        imgeLeft = Image.open(r"ImageFolder\p.jpg")
        imgeLeft = imgeLeft.resize((620, 100), Image.ANTIALIAS)
        self.imgPhotoLeft = ImageTk.PhotoImage(imgeLeft)
        imgeLeft_label = Label(leftFrame, image=self.imgPhotoLeft)
        imgeLeft_label.place(x=0, y=0, width=620, height=100)

        #current course details frame
        ccFrame = LabelFrame(leftFrame, bd=3, bg="#73777B", relief=GROOVE, text="Ongoing Course Details",font=("Rubik", 16, "bold"))
        ccFrame.place(x=5, y=105, width=600, height=105)

        #department
        depLabel=Label(ccFrame,bg="#73777B",text="Department",font=("Rubik", 9, "bold"))
        depLabel.grid(row=0,column=0,padx=4,sticky=W)

        depCombo=ttk.Combobox(ccFrame,textvariable=self.DepVar,font=("Rubik", 8, "bold"),width=18,state="readonly")
        depCombo["values"]=("Select Department","Computer Science and Engineering","Electronics Engineering","Electrical Engineering","Mechanical Engineering","Civil Engineering","Other")
        depCombo.current(0)
        depCombo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        courLabel = Label(ccFrame, bg="#73777B", text="Course", font=("Rubik", 9, "bold"))
        courLabel.grid(row=0, column=2, padx=4,sticky=W)

        courCombo = ttk.Combobox(ccFrame,textvariable=self.CourVar, font=("Rubik", 8, "bold"),width=18, state="readonly")
        courCombo["values"] = ("Select Course", "B.S.","B.Tech","M.Tech","B.Arch")
        courCombo.current(0)
        courCombo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        #Session Year
        yrLabel = Label(ccFrame, bg="#73777B", text="Session-Year", font=("Rubik", 9, "bold"))
        yrLabel.grid(row=1, column=0, padx=4, sticky=W)

        yrCombo = ttk.Combobox(ccFrame,textvariable=self.SessYVar, font=("Rubik", 8, "bold"), width=18, state="readonly")
        yrCombo["values"] = ("Select Year", "2020-2021","2021-2022","2022-2023","2023-2024")
        yrCombo.current(0)
        yrCombo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Semester
        semLabel = Label(ccFrame, bg="#73777B", text="Semester", font=("Rubik", 9, "bold"))
        semLabel.grid(row=1, column=2, padx=4, sticky=W)

        semCombo = ttk.Combobox(ccFrame,textvariable=self.SemVar,font=("Rubik", 8, "bold"), width=18, state="readonly")
        semCombo["values"] = ("Select Semester", "I", "II", "III", "IV","V","VI","VII","VIII")
        semCombo.current(0)
        semCombo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #Students Personal Details frame
        classStFrame = LabelFrame(leftFrame, bd=3, bg="#73777B", relief=GROOVE, text="Students Personal Information",font=("Rubik", 16, "bold"))
        classStFrame.place(x=5, y=215, width=600, height=175)

        #student id
        stIDLabel = Label(classStFrame, bg="#73777B", text="Student Id",font=("Rubik", 9, "bold"))
        stIDLabel.grid(row=0, column=0, padx=5, pady=1,sticky=W)

        stIDEntry=ttk.Entry(classStFrame,textvariable=self.IdVar,width=18,font=("Rubik", 8, "bold"))
        stIDEntry.grid(row=0,column=1,padx=5,pady=1,sticky=W)

        #Student Name
        stNameLabel = Label(classStFrame, bg="#73777B", text="Student Name", font=("Rubik", 9, "bold"))
        stNameLabel.grid(row=0, column=2, padx=5,pady=1, sticky=W)

        stNameEntry = ttk.Entry(classStFrame,textvariable=self.SNameVar,width=18,font=("Rubik", 8, "bold"))
        stNameEntry.grid(row=0, column=3, padx=5, pady=1,sticky=W)

        #Student Email id
        stEmailLabel = Label(classStFrame, bg="#73777B", text="Email Id", font=("Rubik", 9, "bold"))
        stEmailLabel.grid(row=1, column=0, padx=5, pady=1,sticky=W)

        stEmailEntry = ttk.Entry(classStFrame,textvariable=self.EmailVar , width=18,font=("Rubik", 8, "bold"))
        stEmailEntry.grid(row=1, column=1, padx=5,pady=1, sticky=W)

        #Student Mobile No
        stMobileNoLabel = Label(classStFrame, bg="#73777B", text="Mobile No", font=("Rubik", 9, "bold"))
        stMobileNoLabel.grid(row=1, column=2, padx=5,pady=1, sticky=W)

        stMobileNoEntry = ttk.Entry(classStFrame,textvariable=self.Mob_NoVar, width=18, font=("Rubik", 8, "bold"))
        stMobileNoEntry.grid(row=1, column=3, padx=5,pady=1,sticky=W)

        #Gender of Student
        stGenderLabel = Label(classStFrame, bg="#73777B", text="Gender", font=("Rubik", 9, "bold"))
        stGenderLabel.grid(row=2, column=0, padx=5, pady=1,sticky=W)

        GenCombo = ttk.Combobox(classStFrame, textvariable=self.GenderVar, font=("Rubik", 8, "bold"), width=15,state="readonly")
        GenCombo["values"] = ("Select", "Male","Female","Other")
        GenCombo.current(0)
        GenCombo.grid(row=2, column=1, padx=5, pady=1, sticky=W)

        #Address of student
        stAddressLabel = Label(classStFrame, bg="#73777B", text="Address", font=("Rubik", 9, "bold"))
        stAddressLabel.grid(row=2, column=2, padx=5, pady=1,sticky=W)

        stAddressEntry = ttk.Entry(classStFrame,textvariable=self.AddrVar,width=18,font=("Rubik", 8, "bold"))
        stAddressEntry.grid(row=2, column=3, padx=5, pady=1,sticky=W)

        #radio button for sample photo status
        self.rbtnVar=StringVar()
        rbtn=ttk.Radiobutton(classStFrame,variable=self.rbtnVar,text="Take Photo Sample",value="Yes")
        rbtn.grid(row=3,column=0,padx=5)

        #save button
        svebtn=Button(classStFrame,width=15,text="Save",command=self.addData,font=("Rubik", 8, "bold"),bg="#112B3C",fg="white")
        svebtn.grid(row=4,column=0,padx=6,pady=2)

        #update button
        updbtn = Button(classStFrame,width=15, text="Update",command=self.dataUpd, font=("Rubik", 8, "bold"), bg="#112B3C", fg="white")
        updbtn.grid(row=4, column=1,padx=6,pady=2)

        #delete button
        delbtn = Button(classStFrame,width=15, text="Delete",command=self.delData, font=("Rubik", 8, "bold"), bg="#112B3C", fg="white")
        delbtn.grid(row=4, column=2,padx=6,pady=2)

        #reset button
        resbtn = Button(classStFrame,width=15, text="Reset", command=self.resData,font=("Rubik", 8, "bold"), bg="#112B3C", fg="white")
        resbtn.grid(row=4, column=3,padx=6,pady=2)

        #for taking the photosamples
        tkbtn = Button(classStFrame, width=20, text="Take Photo Sample",command=self.genDataSet, font=("Rubik", 8, "bold"), bg="#112B3C", fg="white")
        tkbtn.grid(row=5, column=0, padx=6)

        rightFrame = LabelFrame(mainFrame, bd=3,bg="#73777B", relief=GROOVE, text="Student Details", font=("Rubik", 16, "bold"))
        rightFrame.place(x=660, y=5, width=570, height=428)

        SearchingFrame = LabelFrame(rightFrame, bd=3, bg="#73777B", relief=GROOVE, text="Search System",font=("Rubik", 14, "bold"))
        SearchingFrame.place(x=5, y=10, width=554, height=80)

        #for searching the data
        searchLabel = Label(SearchingFrame, bg="#251D3A", text="Search By", fg="white",font=("Rubik", 12, "bold"))
        searchLabel.grid(row=0, column=0, padx=5, pady=15, sticky=W)

        self.searComboVar = StringVar()
        searchCombo = ttk.Combobox(SearchingFrame,textvariable=self.searComboVar, font=("Rubik", 10, "bold"), width=13, state="readonly")
        searchCombo["values"] = ("Select Option", "Department" ,"Name", "Student_Id")
        searchCombo.current(0)
        searchCombo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.seaEntryVar=StringVar()
        searchEntry = ttk.Entry(SearchingFrame,textvariable=self.seaEntryVar, width=20, font=("Rubik", 9, "bold"))
        searchEntry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        searchbtn = Button(SearchingFrame, width=10, text="Search",command=self.searchData, font=("Rubik", 9, "bold"), bg="#112B3C",fg="white")
        searchbtn.grid(row=0, column=3, padx=2,pady=6)

        showbtn = Button(SearchingFrame, width=10, text="Show All",command=self.fetchingData, font=("Rubik", 9, "bold"), bg="#112B3C",fg="white")
        showbtn.grid(row=0, column=4, padx=2,pady=6)

        #table frame
        tFrame = Frame(rightFrame, bd=3, bg="#73777B", relief=GROOVE,)
        tFrame.place(x=5, y=100, width=554, height=300)

        #for scrolling
        scrX=ttk.Scrollbar(tFrame,orient=HORIZONTAL)
        scrY=ttk.Scrollbar(tFrame,orient=VERTICAL)

        self.table=ttk.Treeview(tFrame,columns=("Dep","Cour","Sess-Y","Sem","Id","SName","Email","Mob No","Gender","Addr","photo"),xscrollcommand=scrX.set,yscrollcommand=scrY.set)
        scrX.pack(side=BOTTOM,fill=X)
        scrY.pack(side=RIGHT, fill=Y)
        scrX.config(command=self.table.xview)
        scrY.config(command=self.table.yview)

        self.table.heading("Dep",text="Department")
        self.table.heading("Cour",text="Course")
        self.table.heading("Sess-Y",text="Session Year")
        self.table.heading("Sem", text="Semester")
        self.table.heading("Id",text="Student Id")
        self.table.heading("SName",text="Student Name")
        self.table.heading("Email",text="Email Id")
        self.table.heading("Mob No",text="Mobile No")
        self.table.heading("Gender",text="Gender")
        self.table.heading("Addr",text="Address")
        self.table.heading("photo",text="SamplePhotoStatus")

        self.table["show"]="headings"

        self.table.column("Dep", width=200)
        self.table.column("Cour",width=80)
        self.table.column("Sess-Y", width=100)
        self.table.column("Sem",width=80)
        self.table.column("Id",width=80)
        self.table.column("SName", width=120)
        self.table.column("Email",width=200)
        self.table.column("Mob No",width=80 )
        self.table.column("Gender",width=80)
        self.table.column("Addr",width=150)
        self.table.column("photo",width=110)


        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease>",self.getCur)
        self.fetchingData()

    #for adding the data to the database
    def addData(self):
        if (self.DepVar.get()=="Select Department" or self.SNameVar.get()==""or self.EmailVar.get()=="" or self.IdVar.get()==""or self.CourVar.get()=="Select Course" or self.SessYVar.get()=="Select Year" or self.SemVar.get()=="Select Semester"or self.GenderVar.get()=="Select" or self.AddrVar.get()==""or self.Mob_NoVar.get()==""or self.rbtnVar.get()==""):
            messagebox.showwarning("Warning","All fields are required",parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host="localhost",username="root",password="ak201020",database="myproject")
                cur=connection.cursor()
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.DepVar.get(),
                                                                                            self.CourVar.get(),
                                                                                            self.SessYVar.get(),
                                                                                            self.SemVar.get(),
                                                                                            self.IdVar.get(),
                                                                                            self.SNameVar.get(),
                                                                                            self.EmailVar.get(),
                                                                                            self.Mob_NoVar.get(),
                                                                                            self.GenderVar.get(),
                                                                                            self.AddrVar.get(),
                                                                                            self.rbtnVar.get()
                                                                                        ))
                connection.commit()
                self.fetchingData()
                connection.close()
                messagebox.showinfo("Success","Details of Student has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)

    #for fetching the data from the database to the table
    def fetchingData(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="ak201020",database="myproject")
        cur = connection.cursor()
        cur.execute("select * from student")
        data=cur.fetchall()

        if len(data)!=0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("",END,values=i)
            connection.commit()
        connection.close()

    def getCur(self,event=""):
        curFocus=self.table.focus()
        cont=self.table.item(curFocus)
        data=cont["values"]
        self.DepVar.set(data[0]),
        self.CourVar.set(data[1]),
        self.SessYVar.set(data[2]),
        self.SemVar.set(data[3]),
        self.IdVar.set(data[4]),
        self.SNameVar.set(data[5]),
        self.EmailVar.set(data[6]),
        self.Mob_NoVar.set(data[7]),
        self.GenderVar.set(data[8]),
        self.AddrVar.set(data[9]),
        self.rbtnVar.set(data[10])

    #for updating the data
    def dataUpd(self):
        if (self.DepVar.get()=="Select Department" or self.SNameVar.get()==""or self.EmailVar.get()=="" or self.IdVar.get()==""or self.CourVar.get()=="Select Course" or self.SessYVar.get()=="Select Year" or self.SemVar.get()=="Select Semester"or self.GenderVar.get()=="Select" or self.AddrVar.get()==""or self.Mob_NoVar.get()==""or self.rbtnVar.get()==""):
            messagebox.showwarning("Warning","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this already filled details",parent=self.root)
                if Update>0:
                    connection = mysql.connector.connect(host="localhost", username="root", password="ak201020",database="myproject")
                    cur = connection.cursor()
                    cur.execute("Update student set `Department`=%s, `Course`=%s,`Session_Year`=%s,`Semester`=%s,`Name`=%s,`Email_Id`=%s,`Mobile_No`=%s,`Gender`=%s,`Address`=%s,`PhotoStatus`=%s where `Student_Id`=%s",(
                                                                                                                                                                                      self.DepVar.get(),
                                                                                                                                                                                      self.CourVar.get(),
                                                                                                                                                                                      self.SessYVar.get(),
                                                                                                                                                                                      self.SemVar.get(),
                                                                                                                                                                                      self.SNameVar.get(),
                                                                                                                                                                                      self.EmailVar.get(),
                                                                                                                                                                                      self.Mob_NoVar.get(),
                                                                                                                                                                                      self.GenderVar.get(),
                                                                                                                                                                                      self.AddrVar.get(),
                                                                                                                                                                                      self.rbtnVar.get(),
                                                                                                                                                                                      self.IdVar.get()

                                                                                                                                                                                   ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Updation occurs successfully", parent=self.root)
                connection.commit()
                self.fetchingData()
                connection.close()

            except Exception as e:
                messagebox.showerror("Error", f"Due To:{str(e)}", parent=self.root)

    # for deleting the data
    def delData(self):
        if self.IdVar.get()=="":
            messagebox.showwarning("Warning","Student Id must be required",parent=self.root)
        else:
            try:
                delt=messagebox.askyesno("Delete","Do you want to delete this data",parent=self.root)
                if delt>0:
                    connection = mysql.connector.connect(host="localhost", username="root", password="ak201020",database="myproject")
                    cur = connection.cursor()
                    sql="delete from student where Student_Id=%s"
                    value=(self.IdVar.get(),)
                    cur.execute(sql,value)
                else:
                    if not delt:
                        return
                connection.commit()
                self.fetchingData()
                connection.close()
                messagebox.showinfo("Success","Deletion occurs successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due To:{str(e)}", parent=self.root)

    #for resetting the data
    def resData(self):
        self.DepVar.set("Select Department")
        self.CourVar.set("Select Course")
        self.SessYVar.set("Select Year")
        self.SemVar.set("Select Semester")
        self.IdVar.set("")
        self.SNameVar.set("")
        self.EmailVar.set("")
        self.Mob_NoVar.set("")
        self.GenderVar.set("Select")
        self.AddrVar.set("")
        self.rbtnVar.set("")

    #for searching the data in the table
    def searchData(self):
        if  self.searComboVar.get() == "Select" or self.seaEntryVar.get() == "" :
            messagebox.showerror("Error", "Select Combo option and Enter entry box", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="ak201020",database="myproject")
                cur = connection.cursor()
                cur.execute("SELECT * FROM student WHERE " +str(self.searComboVar.get())+" LIKE '%"+str(self.seaEntryVar.get())+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.table.delete(*self.table.get_children())
                    for i in rows:
                        self.table.insert("", END, values=i)
                    if rows == None:
                        messagebox.showerror("Error", "Data Not Found", parent=self.root)
                        connection.commit()
                connection.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # Generating data set
    def genDataSet(self):
        if (self.DepVar.get()=="Select Department" or self.SNameVar.get()==""or self.EmailVar.get()=="" or self.IdVar.get()==""or self.CourVar.get()=="Select Course" or self.SessYVar.get()=="Select Year" or self.SemVar.get()=="Select Semester"or self.GenderVar.get()=="Select" or self.AddrVar.get()==""or self.Mob_NoVar.get()==""or self.rbtnVar.get()==""):
               messagebox.showwarning("Warning","All fields are required",parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="ak201020",database="myproject")
                cur = connection.cursor()
                cur.execute("select * from student")
                ans=cur.fetchall()
                id=0
                for x in ans:
                    id+=1
                cur.execute("Update student set `Department`=%s, `Course`=%s,`Session_Year`=%s,`Semester`=%s,`Name`=%s,`Email_Id`=%s,`Mobile_No`=%s,`Gender`=%s,`Address`=%s,`PhotoStatus`=%s where `Student_Id`=%s",(
                                                                                                                                                                                                                            self.DepVar.get(),
                                                                                                                                                                                                                            self.CourVar.get(),
                                                                                                                                                                                                                            self.SessYVar.get(),
                                                                                                                                                                                                                            self.SemVar.get(),
                                                                                                                                                                                                                            self.SNameVar.get(),
                                                                                                                                                                                                                            self.EmailVar.get(),
                                                                                                                                                                                                                            self.Mob_NoVar.get(),
                                                                                                                                                                                                                            self.GenderVar.get(),
                                                                                                                                                                                                                            self.AddrVar.get(),
                                                                                                                                                                                                                            self.rbtnVar.get(),
                                                                                                                                                                                                                            self.IdVar.get()==id+1

                                                                                                                                                                                                                     ))
                connection.commit()
                self.fetchingData()
                self.resData()
                connection.close()

                fClassifier=cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")

                def croppedFace(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = fClassifier.detectMultiScale(gray,1.3,5)
                        #minSize=(30, 30),
                        #flags=cv2.CASCADE_SCALE_IMAGE

                    for(x,y,w,h) in faces:
                        croppedFace=img[y:y+h,x:x+w]
                        return croppedFace

                cap=cv2.VideoCapture(0)
                imgId=0
                while True:
                    ret,frame=cap.read()
                    if croppedFace(frame) is not None:
                        imgId+=1
                        face=cv2.resize(croppedFace(frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        filePath="mydata/user."+str(id)+"."+str(imgId)+".jpg"
                        cv2.imwrite(filePath,face)
                        cv2.putText(face,str(imgId),(50,50),cv2.FONT_HERSHEY_TRIPLEX,1,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(imgId)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed successfully",parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Due To:{str(e)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
