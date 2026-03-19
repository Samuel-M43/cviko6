import matplotlib.pyplot as plt
from signal_ops import *

def load_signal_from_txt(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(float(line))
    return data
print(load_signal_from_txt("ecg_data.txt"))

def plot_signal(values):
    plt.plot(values)
    plt.show()

if __name__ == "__main__":
   values = load_signal_from_txt("ecg_data.txt")
   print(signal_max(values))
   print(signal_min(values))
   print(signal_avg(values))
   plot_signal(values)
