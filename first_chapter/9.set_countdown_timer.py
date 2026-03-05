
import time

while True:
    try:
        seconds = int(input("Enter the countdown time in seconds: "))
        if seconds < 1:
            print("Please enter a non-negative number.")
            continue
        break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = '{:02d}:{:02d}'.format(mins, secs)
    print(f"Time remaining: {time_format}", end='\r')
    time.sleep(1)
print("Time's up! Countdown finished.")
