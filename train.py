from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        self.root.iconbitmap("face_attendance.ico")

        #for title
        titleLabel = Label(self.root, text="TRAIN DATA SET", font=("Rubik", 30, "bold"), bg="#525252",fg="black")
        titleLabel.place(x=0, y=0, width=1300, height=55)

        Back_Button = Button(titleLabel, text="Back", command=self.root.destroy, font=("Rubik", 13, "bold"), width=14,bg="black", fg="white")
        Back_Button.pack(side=RIGHT)

        def time():
            string = strftime("%H:%M:%S %p")
            label.config(text=string)
            label.after(1000, time)

        label = Label(titleLabel, font=("Rubik", 18, "bold"), background="#525252", foreground="#293462")
        label.place(x=5, y=5, width=140, height=40)
        time()

        #for background image
        bngImg = Image.open(r"ImageFolder\train-bng1.jpg")
        bngImg = bngImg.resize((1300, 670), Image.ANTIALIAS)
        self.bngImgPhoto = ImageTk.PhotoImage(bngImg)
        first_label = Label(self.root, image=self.bngImgPhoto)
        first_label.place(x=0, y=55, width=1300, height=670)

        #button for training of data
        btn = Button(first_label, text="START TRAINING", cursor="hand2", command=self.trainClassifier, font=("Rubik", 20, "bold"), bg="#112B3C", fg="white")
        btn.place(x=480, y=460, width=300, height=50)

    def trainClassifier(self):
        dataDirectory=("mydata")
        path=[os.path.join(dataDirectory,file) for file in os.listdir(dataDirectory)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #gray scale image
            NpImg=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(NpImg)
            ids.append(id)
            cv2.imshow("Train Data",NpImg)
            cv2.waitKey(1) == 13
        ids=np.array(ids)

        clsf=cv2.face.LBPHFaceRecognizer_create()   #classifier
        clsf.train(faces,ids)
        clsf.write("classifier.xml")
        messagebox.showinfo("Results", "Training of Data Sets completed sucessfully",parent=self.root)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

