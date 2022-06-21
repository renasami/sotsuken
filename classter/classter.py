import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
import pandas as pd
# usecols=["name",'capital','employees','listed','averageAge',
#  'femaleRate','averageAnnualIncome','paidHolidayDigestibility',
#  'turnoverRate','femaleManagerRate','handicappedEmployeeRate',
#  'averageDuration','sales','currentEarnings',
# ]
usecols = ["名前","売上","従業員数","上場or非上場","平均年齢","平均勤続年数","特許数","設立からの経過","平均給与", "時間外労働","女の割合"]

# usecols = ["名前","売上","従業員数","上場or非上場","平均給与", ]


df = pd.read_csv('./random.csv',header=0,usecols=usecols).set_index("名前")

df = df.fillna(0.0)
# df['name'] = df['name'].apply(lambda x: str(x.strip())).astype(str)
# df.set_index('name', inplace=True)

arr = df.values

X = arr[:,1:]
Y = arr[:,1]

# # ワインデータ
# wine = datasets.load_wine()
# X = wine.data[:,[9,12]]
# y = wine.target

#　特徴量の標準化
sc = StandardScaler()
X_std = sc.fit_transform(arr)

print(X_std)
# K-meansモデルの作成・訓練
model = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=300,
                       tol=0.0001, verbose=0,
                       random_state=None, copy_x=True)
model.fit(X_std)

print(model.labels_)
# K-means散布図
plt.figure(figsize=(24,8))
plt.subplot(1,2,1)
plt.scatter(X_std[:,0], X_std[:,1], c=model.labels_)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], s=250, marker='*')
plt.grid(True)
plt.title('K-Means')

# 正解データ散布図
plt.subplot(1,2,2)
plt.scatter(X_std[:,0], X_std[:,1], c=Y)
plt.title('Target data')

plt.show()