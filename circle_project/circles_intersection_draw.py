
import matplotlib.pyplot as plt

def draw_data(circle_1, circle_2, circle_3):

    fig, ax = plt.subplots()

    c1 = plt.Circle((circle_1["x"], circle_1["y"]), circle_1["r"],
                    fill=False, color="blue", linewidth=2)
    ax.add_patch(c1)


    c2 = plt.Circle((circle_2["x"], circle_2["y"]), circle_2["r"],
                    fill=False, color="red", linewidth=2)
    ax.add_patch(c2)

    c3 = plt.Circle((circle_3["x"], circle_3["y"]), fill=False, color="green", linewidth=2)
    ax.add_patch(c3)


    all_x = [circle_1["x"], circle_2["x"], circle_3["x"]]
    all_y = [circle_1["y"], circle_2["y"], circle_3["y"]]
    max_r = max(circle_1["r"], circle_2["r"], circle_3["r"])

    ax.set_xlim(min(all_x) - max_r - 1, max(all_x) + max_r + 1)
    ax.set_ylim(min(all_y) - max_r - 1, max(all_y) + max_r + 1)
    ax.set_aspect("equal", adjustable="box")

    plt.title("Prienik dvoch kružnic")
    plt.grid(True)
    plt.show()

circle_1 = {"x": 8, "y": 6, "r": 5}
circle_2 = {"x": 7, "y": 3, "r": 3}
circle_3 = {"x": 5, "y": 4, "r": 2}

draw_data(circle_1, circle_2, circle_3)



# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()  # připravení okna pro vykreslení
#
# circle = plt.Circle((0, 0), 2, fill=False, color="blue")  # vytvoření kružnice
# ax.add_patch(circle)  # přidání kružnice do okna
#
# ax.set_xlim(-5, 5) # nastavení rozsahu os, aby bylo vidět celý graf
# ax.set_ylim(-5, 5)
#
# ax.set_aspect("equal")  # nastavení stejného poměru os, aby kružnice vypadala jako kruh
# plt.show()  # zobrazení okna s kružnicí