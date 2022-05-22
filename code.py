import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics

data = pd.read_csv("StudentsPerformance.csv")
data_list = data["reading score"].to_list()

mean = statistics.mean(data_list)
median = statistics.median(data_list)
mode = statistics.mode(data_list)
std_dev = statistics.stdev(data_list)

first_std_dev_start, first_std_dev_end = mean - std_dev, mean + std_dev
second_std_dev_start, second_std_dev_end = mean - (2*std_dev), mean + (2*std_dev)
third_std_dev_start, third_std_dev_end = mean - (3*std_dev), mean + (3*std_dev)

fig = ff.create_distplot([data_list], ["reading scores"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_dev_start, first_std_dev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [first_std_dev_end, first_std_dev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [second_std_dev_start, second_std_dev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [second_std_dev_end, second_std_dev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.show()

data1 = [result for result in data_list if result > first_std_dev_start and result < first_std_dev_end]
data2 = [result for result in data_list if result > second_std_dev_start and result < second_std_dev_end]
data3 = [result for result in data_list if result > third_std_dev_start and result < third_std_dev_end]

print("mean, median, and mode of the reading score data is: {}, {}, {}".format(mean, median, mode))
print("the standard deviation of the reading score dataset is: {}".format(std_dev))

print("{}% of the data lies within 1st standard deviation".format(len(data1)*100.0/len(data_list)))
print("{}% of the data lies within 2nd standard deviation".format(len(data2)*100.0/len(data_list)))
print("{}% of the data lies within 3rd standard deviation".format(len(data3)*100.0/len(data_list)))