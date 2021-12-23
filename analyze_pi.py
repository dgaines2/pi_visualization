import numpy as np
import matplotlib.pyplot as plt

with open("pi-10million.txt") as fr:
    data = fr.readlines()
    digits_of_pi = np.asarray([int(i) for i in data[0].strip()])

common_resolutions = {}
common_resolutions["tiny"] = [320, 180]
common_resolutions["480p"] = [640, 360]
common_resolutions["720p"] = [1280, 720]
common_resolutions["1080p"] = [1920, 1080]
common_resolutions["1440p"] = [2560, 1440]
common_resolutions["4K"] = [3840, 2160]

for mode in common_resolutions:
    n_rows = common_resolutions[mode][0]
    n_columns = common_resolutions[mode][1]
    print(f"{mode}, rows = {n_rows}, columns = {n_columns}")
    print(f"Total values = {n_rows*n_columns}")
    print(f"Aspect ratio = {n_rows/n_columns}")

    selected_digits_of_pi = digits_of_pi[:n_rows*n_columns]
    selected_digits_of_pi_reshaped = selected_digits_of_pi.reshape(n_rows, n_columns)

    figname = f"pi_{mode}.svg"
    plt.figure(figsize=(8,4.5), dpi=300)
    plt.axis("off")
    plt.imshow(
            selected_digits_of_pi_reshaped, 
            cmap="Greens", 
            vmin=0, 
            vmax=9,
            aspect="auto",
    )
    plt.gca().set_position([0, 0, 1, 1])
    plt.savefig(figname)
    print(f"Saved to {figname}")
    print("")
