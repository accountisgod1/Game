import tkinter as tk
from tkinter import messagebox
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess
from Crash_Handler import Crash

window = tk.Tk()
window.title('Crime Filer Game')

subprocess.run(["python","C:/Users/User/Documents/A/Language/__init__.py"])


crime_data = {"Theft": 5, "Assault": 3, "Vandalism": 2, "Murder": 9}
map_crime_data = {"Lauza": 4, "Mew Bork": 6, "Berm": 2}

def show_notification(message):
    messagebox.showinfo("Notification", message)

def PersonTargeted():
    Person = PersonTargetedBy_Crime.get()
    if Person != "":
        show_notification(f"{Person} has been targeted by a criminal")

def SubmitCrime():
    Crime = TypeOfCrime.get()
    if Crime != "":
        show_notification(f"A person has committed {Crime}")

        # Update the crime_data for the chart
        crime_data[Crime] = crime_data.get(Crime, 0) + 1
        update_chart()

def SubmitMap():
    Map = Location.get()
    if Map != "":
        show_notification(f"A crime has been commited in {Map}")

        # Update the crime_data for the chart
        map_crime_data[Map] = map_crime_data.get(Map, 0) + 1
        update_chartmap()

def SubmitTime():
    time_format = re.compile(r'^\d{1,2}:\d{2}:\d{2} [apmAPM]{2}$')
    Time = DateOfCrime.get()
    
    if Time != "" and time_format.match(Time):
        show_notification(f"The time when the crime was commited is: {Time}")

def SubmitEvidence():
    EvidenceF = Evidence.get()
    if EvidenceF != "":
        show_notification(f"The evidence found in crime scene is: {EvidenceF}")

def SummarizeInfo():
    Person = PersonTargetedBy_Crime.get()
    Crime = TypeOfCrime.get()
    Time = DateOfCrime.get()

    if (Person, Crime, Time) != "":
        show_notification(f"The person targeted is: {Person}, The crime committed is: {Crime}, Time of Crime is {Time}")

def update_chart():
    # Clear existing chart
    for widget in chart_frame.winfo_children():
        widget.destroy()

    # Create a bar chart
    fig, ax = plt.subplots()
    crimes = list(crime_data.keys())
    counts = list(crime_data.values())
    ax.bar(crimes, counts)
    ax.set_ylabel('Number of Crimes')
    ax.set_title('Crime Statistics')

    # Embed the chart in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def update_chartmap():
    # Clear existing chart
    for widget in chart_frame1.winfo_children():
        widget.destroy()

    # Create a bar chart
    fig, ax = plt.subplots()
    crimes = list(map_crime_data.keys())
    counts = list(map_crime_data.values())
    ax.bar(crimes, counts)
    ax.set_ylabel('Number of Crimes Commited In Location')
    ax.set_title('Map Crime Statistics')

    # Embed the chart in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=chart_frame1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Filing of crime

PersonTargetedBy_CrimeLabel = tk.Label(text="Person Targeted: ")
PersonTargetedBy_CrimeLabel.grid(column=1, row=2)

PersonTargetedBy_Crime = tk.Entry(window)
PersonTargetedBy_Crime.grid(column=2, row=2)

PersonTargetedBy_CrimeButton = tk.Button(window, text="Submit Targeted Person", command=PersonTargeted)
PersonTargetedBy_CrimeButton.grid(column=3, row=2)

TypeOfCrimeLabel = tk.Label(window, text="Type Of Crime: ")
TypeOfCrimeLabel.grid(column=1, row=3)

TypeOfCrime = tk.Entry(window)
TypeOfCrime.grid(column=2, row=3)

TypeOfCrimeButton = tk.Button(window, text="Submit Crime", command=SubmitCrime)
TypeOfCrimeButton.grid(column=3, row=3)

DateOfCrimeLabel = tk.Label(window, text="Date Of Crime: ")
DateOfCrimeLabel.grid(column=1, row=4)

DateOfCrime = tk.Entry(window)
DateOfCrime.grid(column=2, row=4)

DateOfCrimeButton = tk.Button(window, text="Submit Time", command=SubmitTime)
DateOfCrimeButton.grid(column=3, row=4)

DateOfCrimeNote = tk.Label(window, text="Format: HH:MM:SS am/pm")
DateOfCrimeNote.grid(column=4, row=4)

LocationLabel = tk.Label(text="Location: ")
LocationLabel.grid(column=1,row=5)

Location = tk.Entry(window)
Location.grid(column=2,row=5)

LocationButton = tk.Button(window,text="Submit Location",command=SubmitMap)
LocationButton.grid(column=3,row=5)

EvidenceLabel = tk.Label(window,text="Evidence: ")
EvidenceLabel.grid(column=1,row=6)

Evidence = tk.Entry(window)
Evidence.grid(column=2,row=6)

EvidenceButton = tk.Button(window,text="Submit Evidence",command=SubmitEvidence)
EvidenceButton.grid(column=3,row=6)

CrimeDescriptionLabel = tk.Label(text="Crime Description or Conclusion")
CrimeDescriptionLabel.grid(column=1,row=8)

CrimeDescription = tk.Entry(window)
CrimeDescription.grid(column=2,row=8)

# Create frames for the charts
chart_frame = tk.Frame(window)
chart_frame.grid(column=1, row=9, columnspan=4)

chart_frame1 = tk.Frame(window)
chart_frame1.grid(column=5, row=9, columnspan=4)


window.mainloop()