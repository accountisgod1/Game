import tkinter as tk
import random
import os

# Create the Tkinter window
window = tk.Tk()

if os.path.isfile("C:/Users/User/Documents/A/Crime_File/ActiveDLC.txt"):
  with open("ActiveDLC.txt", 'r') as f:
    for line in f:
        if "Police: True" in line:

            # Functions
            def Handle_PoliceResponse():
                Police_ResponseInput = Police_Com.get().lower()

                
                if Police_ResponseInput in ["what's the status?", "what is the status of the situation?", "what's the status"," what is the status of the situation"
                                                    "what is the status?","what is the status"]:
                     
                   responses = ["Going Great", "It's a little hard", "We lost multiple", "We are receiving heavy force",
                             "It's not going great. Send backup"]
                   
                   response = random.choice(responses)
                   Police_ComOutput.config(text=response)

                elif Police_ResponseInput in ["do you need airsupport?","do you need airsupport"]:

                    responses = ["No, the plan is working smoothly.","No need. We can deal with this.",
                                 "Maybe, we already lost a few.","Later, we lost 6.", "Yes","We need it, bring it here immediately!",
                                 "We are about to die, please give it all your force!"]
                    
                    response = random.choice(responses)
                    Police_ComOutput.config(text=response)

            def Dispatch(Unit,with_amount):
               Units = ["Swat","FBI","Police","Detective"]
               Units_Sent = 0

               if Unit in Units:
                  if not with_amount:
                     Units_Sent +=1 
                     print(f"Sending 1 {Unit}")
                  else:
                     print("with amount")

                

            # Handling GUI
            Police_ComLabel = tk.Label(window, text="Police Communication Text: ")
            Police_Com = tk.Entry(window)
            Police_ComButton = tk.Button(window, text="Submit Communication", command=Handle_PoliceResponse)
            Police_ComOutput = tk.Label(window, text="Response will be displayed here")
            DispatchLabel = tk.Label(window, text="")


            # Assigning to grids
            Police_ComLabel.grid(column=1, row=1)
            Police_Com.grid(column=2, row=1)
            Police_ComButton.grid(column=3, row=1)
            Police_ComOutput.grid(column=1, row=2, columnspan=3)

        elif "Impossible: True" in line:
            print("Person has Impossible mode")

else:
   print("Critical File Named 'ActiveDLC.txt' does not exist.")
   raise FileNotFoundError("File Named 'ActiveDLC.txt' does not exist, please run the DLC_handler.py or contact support.")

# Start the Tkinter mainloop
window.mainloop()