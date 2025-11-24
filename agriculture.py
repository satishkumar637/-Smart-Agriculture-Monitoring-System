import random 
import time

"""Set limits for soil, temperature, and humidity levels."""
soil_limit = 40
temp_limit = 35
humidity_limit = 30

"""Notify the user and start the sensor check."""
print("Welcome to the farm sensor check!")
print("Let's see if everything is okay with the soil and the weather today.")

"""Start the iteration check."""
round_num = 1
while round_num <= 5:
    print("Check number:", round_num)

    soil = random.randint(20, 60)
    temperature = random.randint(25, 40)
    humidity = random.randint(20, 50)

    print("Soil moisture level is", soil, "percent")
    print("Temperature is around", temperature, "degree Celsius")
    print("Humidity level is", humidity, "percent")

    if soil < soil_limit:
        print("Oh no! Soil looks dry, turning on the water pump for 30 seconds.")
        time.sleep(30)
        print("Water pump is now off.")
    else:
        print("Soil moisture looks good, no need to water now.")

    if temperature > temp_limit:
        print("It's pretty hot today! Be sure that plants are safe from heat.")

    if humidity < humidity_limit:
        print("Humidity is low, opportunity to water your plants carefully.")

    print("---------------------------")
    round_num += 1
    time.sleep(2)

print("That is all for the checks, best wishes your farm stays healthy!")
