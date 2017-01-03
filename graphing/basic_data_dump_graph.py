import plotly as py
import plotly.graph_objs as go
from datetime import datetime

# csv data imports
from parse import *

# time_stamp_1 = int(1481669517.93)
# time_stamp_2 = int(1482692517.93)
# time_stamp_3 = int(1484969517.93)

# x = [datetime.fromtimestamp(time_stamp_1),
#      datetime.fromtimestamp(time_stamp_2),
#      datetime.fromtimestamp(time_stamp_3)]

# data = [go.Scatter(x=x,y=[1, 3, 6]), go.Scatter(x=x,y=[7, 9, 11]), go.Scatter(x=x,y=[1, 9, 17])]
# py.offline.plot(data, filename = 'basic-data-dump-graph-plotly')


data_dump_csv_file_name = "../downloaded_data/test.csv"

f = open(data_dump_csv_file_name, 'r')
format="{},{},{},{}"


time_results = []
x_results = []
y_results = []
z_results = []

for line in f:
    if not len(line.strip()) == 0 :
        result = parse(format, str(line.strip()))
        time = result[0]
        print time
        time_results.append(int(float(time)))
        x = result[1]
        x_results.append(x)
        y = result[2]
        y_results.append(y)
        z = result[3]
        z_results.append(z)

data = [go.Scatter(x=time_results,y=x_results), go.Scatter(x=time_results, y=y_results), go.Scatter(x=time_results ,y=z_results)]
py.offline.plot(data, filename = 'basic-data-dump-graph-plotly')