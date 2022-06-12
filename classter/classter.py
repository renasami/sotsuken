import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
import pandas as pd

df = pd.read_csv('./winequality-white.csv',sep=";")
arr = df.values
X = arr[:,:-1]
Y = arr[:,-1]

# # ワインデータ
# wine = datasets.load_wine()
# X = wine.data[:,[9,12]]
# y = wine.target

#　特徴量の標準化
sc = StandardScaler()
X_std = sc.fit_transform(X)

# K-meansモデルの作成・訓練
model = KMeans(n_clusters=3)
model.fit(X_std)

# K-means散布図
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(X_std[:,0], X_std[:,1], c=model.labels_)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], s=250, marker='*',c='red')
plt.title('K-Means')

# 正解データ散布図
plt.subplot(1,2,2)
plt.scatter(X_std[:,0], X_std[:,1], c=Y)
plt.title('Target data')

plt.show()