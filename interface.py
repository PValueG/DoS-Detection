from tkinter import *
from dosAttack import runSingleDoS
from dosDetectionmain import dosDetect

window = Tk()
window.configure(background="#0892d0")
window.geometry("720x720")

def runSDoS():  # Subprogram 1. Fires dosAttack.py to emulate a sing IP Spoof
    runSingleDoS()

def runSocketGrab():  # Subprogram 3. Fires DDoS_attack.py to emulate a DDoS Random IP Spoof
    rundosDetect


Label(window, text=" Dos tool ",
      pady=10, font=('Arial', 20, 'bold')).pack()
window.title("DOS tool")

Label(window, text="   choose option", bd=4, pady=10, fg='#00ff66',
      font=('Arial', 14, 'bold')).pack()
Button(window, text="  Begin Single IP DoS  ", bd=4, command=runSDoS).pack()
Button(window, text="  Stop Single IP DoS   ", bd=4, command=window.destroy).pack()
Button(window, text="  Begin DDoS IP Scan ", bd=4, command=runSocketGrab).pack()
Button(window, text="  Stop DDoS IP Scan  ", bd=4, command=window.destroy).pack()
window.mainloop()