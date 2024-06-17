import pandas as pd
import os
import matplotlib.pyplot as plt

iris = pd.read_csv(os.path.join(os.path.dirname(__file__), "Iris.csv"))

fig, ax = plt.subplots(2, 2, sharex=True, sharey=False, layout='constrained', figsize=(9, 5))
fig.subplots_adjust(hspace=0.4, wspace=0.4)
fig.supxlabel("Species")

data = []
labels = []
ax[0, 0].set_title('Sepal Length')
for index, flower in iris.iterrows():

    if flower["Species"] not in labels:
        labels.append(flower["Species"])
        data.append([])

    data[labels.index(flower["Species"])].append(flower["SepalLengthCm"])
ax[0, 0].boxplot(data, labels=labels)

data = []
labels = []
ax[0, 1].set_title('Sepal Width')
for index, flower in iris.iterrows():

    if flower["Species"] not in labels:
        labels.append(flower["Species"])
        data.append([])

    data[labels.index(flower["Species"])].append(flower["SepalWidthCm"])
ax[0, 1].boxplot(data, labels=labels)

data = []
labels = []
ax[1, 0].set_title('Petal Length')
for index, flower in iris.iterrows():

    if flower["Species"] not in labels:
        labels.append(flower["Species"])
        data.append([])

    data[labels.index(flower["Species"])].append(flower["PetalLengthCm"])
ax[1, 0].boxplot(data, labels=labels)

data = []
labels = []
ax[1, 1].set_title('Petal Width')
for index, flower in iris.iterrows():

    if flower["Species"] not in labels:
        labels.append(flower["Species"])
        data.append([])

    data[labels.index(flower["Species"])].append(flower["PetalWidthCm"])
ax[1, 1].boxplot(data, labels=labels)

plt.show()
