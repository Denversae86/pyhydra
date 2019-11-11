import pyowm
import sys
owm=pyowm.OWM('88b1c787f6fa8affe78146189071f681')
a1=True
while a1==True:
    place=input("Please enter the location (city, country): ")
    observation=owm.weather_at_place(place)
    w=observation.get_weather()
    print(w)
    temp=w.get_temperature("celsius")["temp"]
    print("current weather in " + str(place) + "is" + w.get_detailed_status())
    print("The temperature is nearly "+str(temp))
    action=input("Do you want to make an another request? (Please enter the command yes|no): ")
if action=="yes":
    print(place)
#"no" condition does not work yet. Program restarts after the grammatically correct command
#
elif action=="no":
    raise SystemExit
else:
     print("please enter the correct command")