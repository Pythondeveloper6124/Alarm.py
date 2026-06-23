
from datetime import datetime
import time


print("--- Python Alarm Clock ---")
    
    # 1. Get user input for the alarm time
alarm_hour = int(input("Enter Hour (0-23): "))
alarm_minute = int(input("Enter Minute (0-59): "))
    
print(f"Alarm successfully set for {alarm_hour:02d}:{alarm_minute:02d}.")

    # 2. Start the tracking loop


now = datetime.now()
        
    # 3. Check if current time matches target time
if now.hour == alarm_hour and now.minute == alarm_minute:
            print("\nWAKE UP!")
            
            
            
