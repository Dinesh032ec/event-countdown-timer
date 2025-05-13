
import time
from datetime import datetime

event = datetime(2026, 1, 1, 0, 0, 0)

while True:
    now = datetime.now()
    remaining = event - now

    if remaining.total_seconds() <= 0:
        print("Happy New Year!")
        break

    days = remaining.days
    hours, minutes, seconds = remaining.seconds // 3600, (remaining.seconds // 60) % 60, remaining.seconds % 60

    print(f"{days}d {hours}h {minutes}m {seconds}s left", end="\r")
    time.sleep(1)
