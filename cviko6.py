
def basic_stats(values):
    return min(values), max(values), round(sum(values) / len(values), 2)


min_v, max_v, avg_v = basic_stats([1200, 980, 1430, 1600, 890])
#print(min_v, max_v, avg_v)


stats = basic_stats([1200, 980, 1430, 1600, 890])
# print(stats)      # (890, 1600, 1220.0)
# print(stats[0])   # min
# print(stats[1])   # max
# print(stats[2])   # avg


from signal_ops import *


print(signal_avg([3,6,12,5]))