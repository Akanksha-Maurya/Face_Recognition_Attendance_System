from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
import os
import csv
from tkinter import filedialog
from send_email import Email

data=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        self.root.iconbitmap("face_attendance.ico")


        # ========variables=========
        self.AtIdVar=StringVar()
        self.Depvar=StringVar()
        self.NameVar=StringVar()
        self.EmailVar=StringVar()
        self.DateVar=StringVar()
        self.TimeVar=StringVar()
        self.StatusVar=StringVar()

        imge = Image.open(r"ImageFolder\stuattendance.jpg")
        imge = imge.resize((1300, 180), Image.ANTIALIAS)
        self.imgPhoto = ImageTk.PhotoImage(imge)
        first_label = Label(self.root, image=self.imgPhoto)
        first_label.place(x=0, y=0, width=1300, height=180)


        label_title = Label(self.root, text="ATTENDANCE SYSTEM", font=("Rubik", 30, "bold"), bg="#525252",fg="black")
        label_title.place(x=0, y=180, width=1300, height=45)

        Back_Button = Button(label_title, text="Back", command=self.root.destroy, font=("Rubik", 13, "bold"), width=14,bg="black", fg="white")
        Back_Button.pack(side=RIGHT)

        def time():
            string = strftime("%H:%M:%S %p")
            label.config(text=string)
            label.after(1000, time)

        label = Label(label_title, font=("Rubik", 18, "bold"), background="#525252", foreground="#293462")
        label.place(x=5, y=0, width=160, height=50)
        time()

        mainFrame = Frame(self.root, bd=3, bg="#73777B")
        mainFrame.place(x=0, y=225, width=1300, height=425)

        leftFrame = LabelFrame(mainFrame, bd=3, bg="#73777B", relief=GROOVE, text="Student Attendance Details",font=("Rubik", 16, "bold"))
        leftFrame.place(x=5, y=5, width=620, height=400)

        imgeLeft = Image.open(r"ImageFolder\stuattendance2.jpg")
        imgeLeft = imgeLeft.resize((620, 120), Image.ANTIALIAS)
        self.imgPhotoLeft = ImageTk.PhotoImage(imgeLeft)
        imgeLeft_label = Label(leftFrame, image=self.imgPhotoLeft)
        imgeLeft_label.place(x=0, y=0, width=620, height=120)

        lfinsideFrame = Frame(leftFrame, bd=3,relief=GROOVE, bg="#73777B")
        lfinsideFrame.place(x=5, y=125, width=605, height=235)

        #for attendance id
        stIDLabel = Label(lfinsideFrame, bg="#73777B", text="Attendance Id", font=("Rubik", 13, "bold"))
        stIDLabel.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        stIDEntry = ttk.Entry(lfinsideFrame,textvariable=self.AtIdVar, width=18, font=("Rubik", 11, "bold"))
        stIDEntry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #for Name
        stNameLabel = Label(lfinsideFrame, bg="#73777B", text="Name", font=("Rubik", 13, "bold"))
        stNameLabel.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        stNameEntry = ttk.Entry(lfinsideFrame, textvariable=self.NameVar,width=18, font=("Rubik", 11, "bold"))
        stNameEntry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        #for Email Id
        EmailLabel = Label(lfinsideFrame, bg="#73777B", text="Email Id", font=("Rubik", 13, "bold"))
        EmailLabel.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        EmailEntry = ttk.Entry(lfinsideFrame,textvariable=self.EmailVar, width=18, font=("Rubik", 11, "bold"))
        EmailEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #for time
        TimeLabel = Label(lfinsideFrame, bg="#73777B", text="Time", font=("Rubik", 13, "bold"))
        TimeLabel.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        TimeEntry = ttk.Entry(lfinsideFrame,textvariable=self.TimeVar, width=18, font=("Rubik", 11, "bold"))
        TimeEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        #for date
        DateLabel = Label(lfinsideFrame, bg="#73777B", text="Date", font=("Rubik", 13, "bold"))
        DateLabel.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        DateEntry = ttk.Entry(lfinsideFrame, textvariable=self.DateVar,width=18, font=("Rubik", 11, "bold"))
        DateEntry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        #for department
        DepLabel = Label(lfinsideFrame, bg="#73777B", text="Department", font=("Rubik", 13, "bold"))
        DepLabel.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        DepEntry = ttk.Entry(lfinsideFrame, textvariable=self.Depvar,width=18, font=("Rubik", 11, "bold"))
        DepEntry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        #for attendance status
        AttLabel = Label(lfinsideFrame, bg="#73777B", text="Attendance Status", font=("Rubik", 13, "bold"))
        AttLabel.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        AttCombo = ttk.Combobox(lfinsideFrame,textvariable=self.StatusVar, font=("Rubik", 11, "bold"), width=16,state="readonly")
        AttCombo["values"] = ("Status","Present","Absent")
        AttCombo.current(0)
        AttCombo.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        #button frame
        btnFrame=Frame(lfinsideFrame,bd=3,relief=GROOVE, bg="white")
        btnFrame.place(x=5, y=160, width=590, height=60)

        #button for importing csv
        impbtn = Button(btnFrame, width=15, text="Import Csv",command=self.importCsv, font=("Rubik", 11, "bold"),bg="#112B3C", fg="white")
        impbtn.grid(row=0, column=0,pady=9)

        # button for exporting csv
        expbtn = Button(btnFrame, width=15, text="Export Csv",command=self.exportCsv, font=("Rubik", 11, "bold"),bg="#112B3C", fg="white")
        expbtn.grid(row=0, column=1,pady=9)

        #button for sending mail
        sEmailbtn = Button(btnFrame, width=15,command=self.sEmail, text="Send Mail",font=("Rubik", 11, "bold"),bg="#112B3C", fg="white")
        sEmailbtn.grid(row=0, column=2,pady=9)

        #button for reset
        resbtn = Button(btnFrame, width=15, command=self.resData,text="Reset", font=("Rubik", 11, "bold"),bg="#112B3C", fg="white")
        resbtn.grid(row=0, column=3,pady=9)

        rightFrame = LabelFrame(mainFrame, bd=3, bg="#73777B", relief=GROOVE, text="Attendance Details",font=("Rubik", 16, "bold"))
        rightFrame.place(x=660, y=5, width=600, height=400)

        tableFrame = Frame(rightFrame, bd=3, relief=GROOVE, bg="#CDB699")
        tableFrame.place(x=5, y=5, width=583, height=355)

        #scroll bar
        scrX=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scrY = ttk.Scrollbar(tableFrame, orient=VERTICAL)

        #table for attendance report
        self.AttReportTable=ttk.Treeview(tableFrame,column=("Id","Dep","Name","Email","Date","Time","Status"),xscrollcommand=scrX.set,yscrollcommand=scrY.set)
        scrX.pack(side=BOTTOM,fill=X)
        scrY.pack(side=RIGHT,fill=Y)

        scrX.config(command=self.AttReportTable.xview)
        scrY.config(command=self.AttReportTable.yview)

        self.AttReportTable.heading("Id",text="ID")
        self.AttReportTable.heading("Dep", text="Department")
        self.AttReportTable.heading("Name", text="Name")
        self.AttReportTable.heading("Email", text="Email Id")
        self.AttReportTable.heading("Date", text="Date")
        self.AttReportTable.heading("Time", text="Time")
        self.AttReportTable.heading("Status", text="Attendance")

        self.AttReportTable["show"]="headings"

        self.AttReportTable.column("Id",width=50)
        self.AttReportTable.column("Dep", width=200)
        self.AttReportTable.column("Name", width=150)
        self.AttReportTable.column("Email", width=200)
        self.AttReportTable.column("Date", width=100)
        self.AttReportTable.column("Time", width=100)
        self.AttReportTable.column("Status", width=100)

        self.AttReportTable.pack(fill=BOTH,expand=1)

        self.AttReportTable.bind("<ButtonRelease>",self.getCur)

   #for fetchinf the data to the table
    def fetchData(self,rows):
        self.AttReportTable.delete(*self.AttReportTable.get_children())
        for i in rows:
            self.AttReportTable.insert("",END,values=i)

    #for importing csv
    def importCsv(self):
        global data
        data.clear()
        fileName=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fileName) as file:
            csvRead=csv.reader(file,delimiter=",")
            for i in csvRead:
                data.append(i)

            self.fetchData(data)

    #for exporting csv
    def exportCsv(self):
        try:
            if len(data)<1:
                messagebox.showwarning("No Data","No Data Found to export",parent=self.root)
                return False

            fileName = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fileName,mode="w",newline="") as file:
                export=csv.writer(file,delimiter=",")
                for i in data:
                    export.writerow(i)
                messagebox.showinfo("Export","Your data get exported to "+os.path.basename(fileName),parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Due To:{str(e)}", parent=self.root)


    def getCur(self,event=""):
        curRow=self.AttReportTable.focus()
        content=self.AttReportTable.item(curRow)
        rows=content["values"]
        self.AtIdVar.set(rows[0])
        self.Depvar.set(rows[1])
        self.NameVar.set(rows[2])
        self.EmailVar.set(rows[3])
        self.DateVar.set(rows[4])
        self.TimeVar.set(rows[5])
        self.StatusVar.set(rows[6])

    #for resetting
    def resData(self):
        self.AtIdVar.set("")
        self.Depvar.set("")
        self.NameVar.set("")
        self.EmailVar.set("")
        self.DateVar.set("")
        self.TimeVar.set("")
        self.StatusVar.set("Status")

    def sEmail(self):
        self.n_window=Toplevel(self.root)
        self.app=Email(self.n_window)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
