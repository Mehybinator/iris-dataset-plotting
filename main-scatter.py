import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

iris = pd.read_csv(os.path.join(os.path.dirname(__file__), "Iris.csv"))

fig, ax = plt.subplots(4, 4, sharex="col", sharey="row", layout='constrained', figsize=(14, 7))

data = [[[], [], []], [[], [], []], [[], [], []], [[], [], []]]
features = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
species = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

for index, flower in iris.iterrows():
    data[features.index("SepalLengthCm")][species.index(flower["Species"])].append(flower["SepalLengthCm"])
    data[features.index("SepalWidthCm")][species.index(flower["Species"])].append(flower["SepalWidthCm"])
    data[features.index("PetalLengthCm")][species.index(flower["Species"])].append(flower["PetalLengthCm"])
    data[features.index("PetalWidthCm")][species.index(flower["Species"])].append(flower["PetalWidthCm"])

ax[0, 0].text(6.15, 6.15, 'SepalLengthCm', ha='center', va='center', size=12, alpha=.5)
ax[1, 1].text(3.2, 3.2, 'SepalWidthCm', ha='center', va='center', size=12, alpha=.5)
ax[2, 2].text(4, 4, 'PetalLengthCm', ha='center', va='center', size=12, alpha=.5)
ax[3, 3].text(1.3, 1.3, 'PetalWidthCm', ha='center', va='center', size=12, alpha=.5)

for i in range(4):
    for j in range(4):
        if i == j:
            continue
        ax[i, j].scatter(data[j][0], data[i][0], marker=".")
        ax[i, j].scatter(data[j][1], data[i][1], marker="+")
        ax[i, j].scatter(data[j][2], data[i][2], marker="v")

legends = [Line2D([0], [0], marker='o', color='w', label='Iris-setosa', markerfacecolor='b', markersize=8),
           Line2D([0], [0], marker='P', color='w', label='Iris-versicolor',markerfacecolor='orange', markersize=8),
           Line2D([0], [0], marker='v', color='w', label='Iris-virginica',markerfacecolor='g', markersize=8)]

ax[0, 0].legend(handles=legends, loc='upper left', frameon=False, ncol=1, labelspacing=0)
plt.show()