import serial
import time
import threading

# serial connection
port = '/dev/ttyACM0'
baud = 9600
serial_port = serial.Serial(port, baud)

# time required for file name
time_format = "%H:%M:%S-%d/%m/%y"
time_for_file_name = time.strftime(time_format)

file_name = 'data/data_capture_' + time_for_file_name + '.txt'

# writes a new line to file for data captured
def write_to_file(accelro_data_sample, f):
        accelro_data_sample = " Time: " + str(time.time()) + " " + accelro_data_sample
        f.write(str(accelro_data_sample) + "\n")

def handle_data(data, f):
        print(data)
        write_to_file(data, f)

def read_from_port(ser):
        # file for writing captured data
        f = open(file_name, 'w')
        while True:
                reading = ser.readline()
                handle_data(reading, f)
        f.close()

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()




# example processing
# try:
#         electret_peak_sample = int(data)
#         write_to_file(electret_peak_sample, f)
#         if electret_peak_sample < 50:
#                 print("very quiet")
#         elif electret_peak_sample < 500:
#                 print("medium noise")
#         else:
#                 print("noisy")
# except ValueError:
#         print("error")
#         print(data)
# except:
#         print("generic error")