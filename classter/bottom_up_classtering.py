# coding: utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram
import pandas as pd
# 生成
# するグループの数
k = 3
# グループ毎の分散
sigma = [[20, 0], [0, 20]]


# データ点の生成
x = np.empty((0,2))
for ell in range(k):
    pc = np.random.uniform(low=-20, high=20, size=(2,)) # グループ毎の代表点
    xs = np.random.multivariate_normal(pc,sigma,30)
    x = np.concatenate([x,xs])
usecols = ["名前","売上","従業員数","上場or非上場","平均年齢","平均勤続年数","特許数","設立からの経過","平均給与", "時間外労働","女の割合"]
df = pd.read_csv('./random.csv',header=0,usecols=usecols).set_index("名前")
filename ="./random.csv"
df = np.loadtxt(filename,skiprows=1,usecols=(1,-1),delimiter=",")
print(df)

# df = df.fillna(0.0)

# クラスタリング

link = linkage(df,'ward')
labels = range(0, k*30)

# 結果のプロット

dendrogram(link,
           orientation='top',
        #    labels=labels,
           distance_sort='descending',
           color_threshold=40.0,
           show_leaf_counts=True)
plt.show()