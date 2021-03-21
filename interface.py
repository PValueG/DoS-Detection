from tkinter import *
from dosAttack import runSingleDoS
from dosDetectionmain import dosDetect

window = Tk()
window.configure(background="#6C5B7B")
window.geometry("500x500")

def runSDoS():  
    runSingleDoS()

def runSocketGrab():
    rundosDetect

Label(window, text=" Dos tool ",
      pady=5, font=('Helvetica', 15)).pack()
window.title("DOS tool")
Button(window, text="  Start the DoS test attack", bd=1, command=runSDoS).pack()
Button(window, text="  Stop the DoS test attack", bd=1, command=window.destroy).pack()
Button(window, text="  Start the DoS Scan ", bd=1, command=runSocketGrab).pack()
Button(window, text="  Stop the DoS scan  ", bd=1, command=window.destroy).pack()
window.mainloop()