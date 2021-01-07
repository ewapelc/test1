#zadanie 4
import time
import random
import datetime
import math

sec = int(input("Podaj liczbe sekund trwania programu: "))

with open("logs.txt", "w") as file:
    for i in range(sec):
        print(i+1)
        time.sleep(1)
        num = random.random()
        d = datetime.datetime.now()
        file.write(str(i) +" | " + str( d.strftime("%d %b") + " "
            + str(d.year) ) + " | " + str( d.strftime("%H : %M : %S") 
            + " | " + str(int(time.time())) + " | " + str(num)) )
        file.write("\n")

print("Gotowe!")

    
