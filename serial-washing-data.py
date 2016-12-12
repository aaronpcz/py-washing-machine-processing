import serial
import time
import threading

# serial connection
port = '/dev/ttyACM0'
baud = 9600
serial_port = serial.Serial(port, baud)

# time required for file name
time_format = "%H:%M:%S"
time_for_file_name = time.strftime(time_format)

file_name = 'data/data_capture_' + time_for_file_name + '.txt'


def handle_data(data, f):
        print(data)
        try:
                print("try");
                # electret_peak_sample = int(data)
                # write_to_file(electret_peak_sample, f)
                # if electret_peak_sample < 50:
                #         print("very quiet")
                # elif electret_peak_sample < 500:
                #         print("medium noise")
                # else:
                #         print("noisy")
        except ValueError:
                print("error")
                print(data)
        except:
                print("generic error")

def read_from_port(ser):
        # file for writing captured data
        f = open(file_name, 'w')
        while True:
                reading = ser.readline()
                handle_data(reading, f)
        f.close()

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()