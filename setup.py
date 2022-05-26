import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Akanksha Maurya\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Akanksha Maurya\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="face_attendance.ico")]


cx_Freeze.setup(
    name = "FaceRecoginitionSystemProject",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face_attendance.ico",'tcl86t.dll','tk86t.dll', 'ImageFolder','mydata','database','attendance_Report']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System",
    executables = executables
    )