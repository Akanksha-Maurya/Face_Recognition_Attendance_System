# Face_Recognition_Attendance_System
This project is a Desktop based application and it is a Attendance System using Face Recognition in Python OpenCV with Tkinter GUI. It uses MySQL as its database.

### Tech Stack Used
Python, OpenCV, Tkinter GUI, MySQL

### Installation required
 i) Python 3.10.4
 
 ii)Pip 22.0.4
 
 iii)Pillow 9.1.1
 
 iv)numpy 1.22.4
 
 v)opencv-python 4.5.5.64
 
 vi)opencv-contrib-python 4.5.5.64
 
 vii)MySQL Installer 8.0.29
 
      Products to be installed in it
      
      i)MySQL Server 8.0.29 -X64
      
      ii)MySQL Workbench 8.0.29 -X64
      
      iii)MySQL Shell 8.0.29 -X64
      
      iv)MYSQL Router 8.0.29 -X64
      
      v)Connector/Python 8.0.29 -X64
      
      vi)MySQL Documentation 8.0.29 -X86
      
  viii)cx-Freeze 6.10    
      
### Special Instructions
Project start with login.py
 
For installation of pip after installing Python 3.10.4, you have to change the path that is in environment variables in advanced system settings of your computer.You have to click the path and after that if you see anything related to python there then delete it. After then click on New button,and then add the path of the folder where you have installed the Python. Now again click on New button and add the path where your pip.exe file is present. Then after that you have to restart your terminal or code editor.

Create the schema, tables and rows  exactly like me that I have provided in the database folder and change the username and password according to you in connector.py.
After creating your own database just delete all the photosamples and list of students in attendance.csv that are provided already.
 
### Look of the App
### Login Page
![Login](https://user-images.githubusercontent.com/97236755/170465402-4fa7053b-4fd4-41a4-8019-f495da2fec9d.png)
### To Reset Password
![Forgot Password](https://user-images.githubusercontent.com/97236755/170465441-cd467232-ffb9-4ab3-8951-4f5a33acd9af.png)
### To Create New Account
![Register](https://user-images.githubusercontent.com/97236755/170465470-cba6b0ff-0a6d-4692-b4a7-022477075ac4.png)
### Homepage
![Homepage](https://user-images.githubusercontent.com/97236755/170465493-a906eb12-a3cd-4409-950c-d374ef44605a.png)
### For saving details and taking photo samples of students
![Student Management System](https://user-images.githubusercontent.com/97236755/170465526-f0e1bebd-8a27-4f06-96f4-15468f0da7de.png)
### Photosamples
![Photos](https://user-images.githubusercontent.com/97236755/170465567-5abacace-dca8-40a5-86a8-0da54d090f57.png)
### While Training Data
![Training Data1](https://user-images.githubusercontent.com/97236755/170547357-5d55aab6-d455-4095-b4cb-48c035dba9ad.png)
### While Face Recognition
![Face Recognition](https://user-images.githubusercontent.com/97236755/170465670-f2c2134c-d4d1-4a41-b5ec-8fa4293f1b56.png)
### Attendance 
![Attendance](https://user-images.githubusercontent.com/97236755/170467276-42216f50-27a6-4c33-b7c2-d33a13e88b56.png)
### For sending mail to late entries
![Attendance-1](https://user-images.githubusercontent.com/97236755/170467299-0a00e4de-6ea5-4903-b975-37b09cde20fd.png)
### Exit
![Exit](https://user-images.githubusercontent.com/97236755/170465698-ae0ef893-172f-422b-b5a8-e20465d66396.png)

### Project Overview
This Project is basically a desktop based application. Whenever you open the app, it will ask for log in, and if you don't have an account then you can register yourself by clicking on signup and then back to login page and login it, there is also option of forgot password. To store all the student details, I have used My SQL as a database. After login, you come across with homepage that has six buttons. First button is all about the management of students, when you click on the button, student managemnet page gets open on screen where you can save the details of student with the help of MySQL database and take the photo samples for attendance.For taking the photo samples, I have used Haar Cascade algorithm for face detection that has objective of finding the faces(location and size) in an image and extract them to be used by the face recognition algorithm. You have to take the photosamples of a student before saving the details of other students otherwise it will get wrong prediction in face recognition. Student Id must be in this sequence 1,2,3,4... .After taking the photo samples of students, when you click on the photos button(2nd button) on the homepage, you get to see photo samples of students in mydata folder. Now click the 3rd button on the homepage that is for tarining of data sets. After training of data sets you have to go to Face Recogniser button(4th button) that recognises student's face when they come across infront of the camera and attendance get stored in the excel sheet.If that person comes again in front of the camera whose attendance is already marked , the face get again recognised but this time his/her attendance will not marked. Student have to neither too close to the camera nor very far from the camera. They have to be at that distance where their face is clearly seen by the camera.For face recognition I have used LBPH algorithm.Now when you go to Attendance button(5th button) and import the attendance report to the table ,you will get to see that whoseever face is recognised by the face recogniser button ,their attendnace is marked as present with details. You can also send mail to the late entries by looking thier time record of presence. After then you can exit from app by click on exit button(6th button) and come back to the login page. 


