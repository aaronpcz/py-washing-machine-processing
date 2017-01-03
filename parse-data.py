from parse import *

format="Time: {} X: {}  Y: {}  Z: {}  m/s^2"

# example="Time: 1481669517.93 X: -0.39  Y: 0.39  Z: 8.90  m/s^2"
# single_result=parse(format, example)
# time=single_result[0]
# x=single_result[1]
# y=single_result[2]
# z=single_result[3]
#
# print(time)
# print(x)
# print(y)
# print(z)

file_name="./downloaded_data/data_capture_22:51:56.txt"
data_file_name="./downloaded_data/data_processed_22:51:56.csv"

write_file = open(data_file_name, 'w')
write_file.write("time,x,y,z\n")

f = open(file_name, 'r')
for line in f:
    if not len(line.strip()) == 0 :
        print(line)
        result = parse(format, str(line.strip()))
        time = result[0]
        x = result[1]
        y = result[2]
        z = result[3]
        # print(time)
        # print(x)
        # print(y)
        # print(z)
        write_file.write(str(time) + ",")
        write_file.write(str(x) + ",")
        write_file.write(str(y) + ",")
        write_file.write(str(z) + "\n")
