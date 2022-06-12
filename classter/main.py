
import torch
import numpy as np
from kmeans_pytorch import kmeans, kmeans_predict
from matplotlib import pyplot as plt
import csv

# pip freeze > requirements.txt
print("start")
use_cuda = torch.has_mps
print(use_cuda)

data_size, dims, num_clusters = 1000, 2, 3
x = np.random.randn(data_size, dims) / 6
x = torch.from_numpy(x)

list_csv = []
with open("./test.csv","r") as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for item in csvreader:
        line = [0 if i == "" or i.isnumeric() == False  else float(i.strip()) for i in item ]
        list_csv.append(line)
print(list_csv[0])

# f =  np.loadtxt("./test.csv", delimiter=',', encoding="utf-8", skiprows=1,usecols=[8,9,12,13,14,15,16,17,18,19,20,21,22])
f = np.array(list_csv)
file_as_np = torch.from_numpy(f)
# kmeans
cluster_ids_x, cluster_centers = kmeans(
    X=file_as_np, num_clusters=num_clusters, distance='euclidean', device=torch.device("cpu")
)


cluster_ids_y = kmeans_predict(
    file_as_np, cluster_centers, 'euclidean', device=torch.device("cpu")
)

plt.figure(figsize=(4, 3), dpi=160)
plt.scatter(x[:, 0], x[:, 1], c=cluster_ids_x, cmap='cool')
# plt.scatter(y[:, 0], y[:, 1], c=cluster_ids_y, cmap='cool', marker='X')
plt.scatter(
    cluster_centers[:, 0], cluster_centers[:, 1],
    c='white',
    alpha=0.6,
    edgecolors='black',
    linewidths=2
)
plt.axis([-1, 1, -1, 1])
plt.tight_layout()
plt.show()
