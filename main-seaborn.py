import seaborn
import pandas as pd
import os
import matplotlib.pyplot as plt

iris = pd.read_csv(os.path.join(os.path.dirname(__file__), "Iris.csv"))

seaborn.pairplot(iris.drop("Id", axis=1), hue="Species", diag_kind="hist")

plt.show()