import psutil
import re
import time
import webbrowser
import datetime
while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    if plugged:
        pluggedstr = 'Plugged In'
    else:
        pluggedstr = 'Not Plugged'
    percent = str(battery.percent)
    percent = float(percent)
    percent = round(percent)
    percentstr = str(percent)
    print(percentstr+'% '+'avaliable '+'and '+pluggedstr)
    if percent<=25 and not plugged:
        webbrowser.open("file:///home/laxman/Downloads/Programs/BatteryProgram/batterylow.html")
        now = datetime.datetime.now()
        print ("Current date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
    elif percent>=60 and plugged:
        webbrowser.open("file:///home/laxman/Downloads/Programs/BatteryProgram/batteryhigh.html")
        now = datetime.datetime.now()
        print ("Current date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1*60)
    

