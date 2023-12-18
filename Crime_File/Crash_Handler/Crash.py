### CRASH HANDLER DO NOT DELETE UNLESS YOU KNOW WHAT YOU ARE DOING

# Imports

from tkinter import Tk, messagebox


class Crash:
    def Crash():
        error_message = 'Crime Filer has crashed due to an issue, please contact support.'


        try:
            with open("C:/Users/User/Documents/A/Crime_File/Settings/Data/Errors.txt", "r") as fl:
                errors = int(fl.read())
        except FileNotFoundError:

            errors = 0


        errors += 1


        messagebox.showerror("ERROR", f"{error_message}")


        with open("C:/Users/User/Documents/A/Crime_File/Settings/Data/Crashlog.txt", "a") as f:
            f.write(f"{errors}. {error_message}\n")


        with open("C:/Users/User/Documents/A/Crime_File/Settings/Data/Errors.txt", "w") as fl:
            fl.write(str(errors))
            
# Check if CRASH.DLL exists and Check Information from CRASH.dll

try:
    with open("C:/Users/User/Documents/A/Crime_File/Crash_Handler/CRASH.dll", "r") as f:
        for line in f:
            if """Active = TRUE""" in line:
                Crash.Crash()
        
except FileNotFoundError:
    print("Critical file missing, please contact support or download it from github.")