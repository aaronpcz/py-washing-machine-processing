import time


counter=100
while(counter > 0):
    counter -= 1
    data="X: 11 Y: 11 Z: 11"
    data += " Time: " + str(time.time())
    print(time.time())