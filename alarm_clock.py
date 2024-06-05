import datetime
import time
from playsound import playsound

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)  # Wait for one second
        if current_time == alarm_time:
            print("Time to wake up!")
            playsound("alarm_sound.mp3")
            break

if __name__ == "__main__":
    # Set the alarm time in HH:MM:SS format
    alarm_time = input("Enter the time to set the alarm (HH:MM:SS): ")
    set_alarm(alarm_time)