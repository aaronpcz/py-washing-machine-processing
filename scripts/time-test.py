import time


# time required for file name
time_format = "%H:%M:%S-%d/%m/%y"
time_for_file_name = time.strftime(time_format)
print(time_for_file_name)

counter=100
while(counter > 0):
    counter -= 1
    data="X: 11 Y: 11 Z: 11"
    data += " Time: " + str(time.time())
    print(time.time())