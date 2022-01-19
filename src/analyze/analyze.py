import re

from matplotlib import pyplot

date_time_list = []
pool_size_list = []
queue_size_list = []
wait_ms_list = []

with open(file='threads.log', mode='r') as f:
    for (index, line) in enumerate(f):
        if index < 1000:
            date_time_text = line[:23]  # 2021-02-09 05:03:06
            # date_time = datetime.strptime(date_time_text, "%Y-%m-%d %H:%M:%S.%f")
            date_time = date_time_text
            statistics_text = line[-27:]  # {poolSize: 0, queueSize: 0}
            wait_ms = re.findall(f"(\d+)(ms)", line)[0][0]
            pool_size_text, queue_size_text = re.findall(r"\d+", line[-27:])

            if int(queue_size_text) == 0:
                continue

            date_time_list.append(date_time)
            pool_size_list.append(int(pool_size_text))
            queue_size_list.append(int(queue_size_text))
            wait_ms_list.append(wait_ms)

print(queue_size_list)
print(wait_ms_list)
pyplot.plot(date_time_list, wait_ms_list)
pyplot.rcParams["figure.figsize"] = (20, 8)
pyplot.show()

print(zip(queue_size_list, wait_ms_list))
