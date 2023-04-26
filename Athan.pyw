# A program that gets accurate prayer times online then sends you a notification when the prayer time comes
# Use pyw extension to make it work in the background

from winotify import Notification, audio
from datetime import datetime
import time, requests, json

url = "https://dailyprayer.abdulrcs.repl.co/api/cairo"
response = requests.get(url)
data = response.json()
prayers = []

for i in data["today"]:
    prayers.append(data["today"][i])

Fajr = prayers[0]
Duhr = prayers[2]
Asr = prayers[3]
Maghrib = prayers[4]
Isha = prayers[5]

popup = Notification(app_id= "Athan", title = "Prayer Times", 
msg= f"Fajr ({Fajr}), Duhr ({Duhr}), Asr ({Asr}),\nMaghrib ({Maghrib}), Isha ({Isha})\nThe program will now run in the background an notify you when its time to pray :D",
duration= "short")

popup.set_audio(audio.Reminder, loop= False)
popup.show()

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    prayer = ''

    # Fajr
    if current_time == Fajr:
        prayer = 'Fajr'
    # Duhr
    if current_time == Duhr:
        prayer = 'Duhr'
    # Asr
    if current_time == Asr:
        prayer = 'Asr'
    # Maghrib
    if current_time == Maghrib:
        prayer = 'Maghrib'
    # Isha
    if current_time == Isha:
        prayer = 'Isha'
    
    if current_time == Fajr or current_time == Duhr or current_time == Asr or current_time == Maghrib or current_time == Isha:    
        popup = Notification(app_id = "Athan", title = f"{prayer} Time", msg = "Time to go pray", duration = "short")
        popup.set_audio(audio.Reminder, loop= False)
        popup.show()
    
    time.sleep(59)
