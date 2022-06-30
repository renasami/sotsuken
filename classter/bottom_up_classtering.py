# coding: utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram
import pandas as pd

import japanize_matplotlib
from IPython.display import set_matplotlib_formats
# set_matplotlib_formats('retina')

# 生成
# するグループの数
# グループ毎の分散
sigma = [[10, 0], [0, 10]]


# # データ点の生成
# x = np.empty((0,2))
# for ell in range(k):
#     pc = np.random.uniform(low=-20, high=20, size=(2,)) # グループ毎の代表点
#     xs = np.random.multivariate_normal(pc,sigma,30)
#     x = np.concatenate([x,xs])
usecols = ["name","employee_number","company_size_male","company_size_female","average_age","month_average_predetermined_overtime_hours","average_continuous_service_years_Male","average_continuous_service_years_Female","shohyo","tokkyo","others"]
# usecols = ["名前","売上","従業員数","上場or非上場","平均年齢","平均勤続年数","特許数","設立からの経過","平均給与", "時間外労働","女の割合"]
df = pd.read_csv('./test_result.csv',header=0,usecols=usecols,encoding="utf-8_sig").set_index("name")
# filename ="./random.csv"
# df = np.loadtxt(filename,skiprows=1,usecols=(1,-1),delimiter=",")
# plt.figure(figsize=[10,10])

df = df.fillna(1)
# df.dropna(how='all')

# クラスタリング

link = linkage(df,
method = 'average', 
# matrix= "mergings"
)


n = dendrogram(link,
           orientation='top',
           labels=df.index,
           distance_sort='descending',
           color_threshold=1000,
           show_leaf_counts=True)

# plt.show()

plt.title('IT企業?')
# 結果のプロット
n_clusters = len(df)
n_samples = len(df)
print(n_samples,n_clusters)
print(type(df))
print("******************************************************************************")
print(n.keys())
for l in n.keys():
   print(len(n[l]))
print("******************************************************************************")
# df1 = pd.DataFrame(n)
df1 = df
print(df1)
print("******************************************************************************")
# print(df1["icoord"]["クルーズ株式会社"])
print("******************************************************************************")

df1.fillna("NaN")
x1 = []
y1 = []
x2 = []
y2 = []




for i in df1.index:

    n1 = round(df1.loc[i]["employee_number"])
    n2 = round(df1.loc[i]["company_size_male"])
    if n_samples == 0 : 
      n_samples = 1
    elif n_clusters == 0 :
      n_clusters = 1
    val = df1.loc[i]["shohyo"]
    n_clusters -= 1
    x1.append(val)
    x2.append(val)
    y1.append(n_clusters)
    y2.append(float(n_samples) / float(n_clusters))

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('Threshold dependency of hierarchical clustering')
plt.ylabel('Num of clusters')
plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'ro-')
plt.xlabel('Threshold')
plt.ylabel('Ave cluster size')
plt.show()

