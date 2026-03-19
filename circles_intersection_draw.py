
import matplotlib.pyplot as plt

def draw_data(circle_1, circle_2):

    fig, ax = plt.subplots()

    c1 = plt.Circle((circle_1["x"], circle_1["y"]), circle_1["r"],
                    fill=False, color="blue", linewidth=2)
    ax.add_patch(c1)


    c2 = plt.Circle((circle_2["x"], circle_2["y"]), circle_2["r"],
                    fill=False, color="red", linewidth=2)
    ax.add_patch(c2)


    all_x = [circle_1["x"], circle_2["x"]]
    all_y = [circle_1["y"], circle_2["y"]]
    max_r = max(circle_1["r"], circle_2["r"])

    ax.set_xlim(min(all_x) - max_r - 1, max(all_x) + max_r + 1)
    ax.set_ylim(min(all_y) - max_r - 1, max(all_y) + max_r + 1)
    ax.set_aspect("equal", adjustable="box")

    plt.title("Průnik dvou kružnic")
    plt.grid(True)
    plt.show()