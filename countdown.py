import time
from datetime import datetime

# Set your event details here
event_name = "New Year"
event_date = "2026-01-01 00:00:00"

# Convert event date to datetime object
event_time = datetime.strptime(event_date, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    countdown = event_time - now

    if countdown.total_seconds() <= 0:
        print(f"The event '{event_name}' has started!")
        break

    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Countdown to {event_name}: {days}d {hours}h {minutes}m {seconds}s", end="\r")
    time.sleep(1)
