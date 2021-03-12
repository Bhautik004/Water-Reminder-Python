
#pip install plyer 

import time
from plyer import notification


if __name__ == "__main__":
    while True:
    
        notification.notify(
            title = "Please Drink Water",
            message = "National Academies of Sciences, Engineering, 
            and Medicine determined that an adequate daily fluid 
            intake is: About 15.5 cups (3.7 liters) of fluids a 
            day for men.About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = "D:\WPy64-3830\Water\Water.ico",
            timeout=12   # 12 second show notification
        )
        time.sleep(60*60) # after 1 hour show notification
