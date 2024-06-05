import datetime  # Import the datetime module to work with date and time
import time  # Import the time module to add delays in the code
from playsound import playsound  # Import the playsound module to play sound files

# Function to set the alarm
def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")  # Inform the user that the alarm is set

    # Infinite loop to keep checking the current time
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
        time.sleep(1)  # Wait for one second before checking the time again

        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            print("Time to wake up!")  # Print a message to wake up
            playsound("alarm_sound.mp3")  # Play the alarm sound
            break  # Exit the loop when the alarm time is reached

# Main part of the program
if __name__ == "__main__":
    # Ask the user to enter the alarm time in HH:MM:SS format
    alarm_time = input("Enter the time to set the alarm (HH:MM:SS): ")
    set_alarm(alarm_time)  # Call the set_alarm function with the user's input
