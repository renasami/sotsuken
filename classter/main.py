
import torch
import numpy as np
from kmeans_pytorch import kmeans


# pip freeze > requirements.txt
print("start")
use_cuda = torch.has_mps
print(use_cuda)

data_size, dims, num_clusters = 1000, 2, 3
x = np.random.randn(data_size, dims) / 6
x = torch.from_numpy(x)

# kmeans
cluster_ids_x, cluster_centers = kmeans(
    X=x, num_clusters=num_clusters, distance='euclidean', device=torch.device("mps")
)
