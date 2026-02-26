import random
import time

min_limit = float(input("Enter minimum temperature limit: "))

max_limit = float(input("Enter maximum temperature limit: "))


while True:
    temperature = round(random.uniform(-10, 60), 2)    #generates random temperature
    
    print("Current Temperature: ", temperature, "°C")
    
    # Comparing temperature with limits


    if temperature < min_limit:
        print("Temperature is Below minimum limit")

    elif temperature > max_limit:
        print("Temperature is Above maximum limit")
    else:
        print("Temperature is within the safe limit")
    
    time.sleep(2)     # 2 second delay