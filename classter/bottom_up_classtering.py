# coding: utf-8
from asyncore import write
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram,fcluster
# from scipy.cluster import AgglomerativeClustering/
import pandas as pd
from sklearn.decomposition import PCA
import japanize_matplotlib
from IPython.display import set_matplotlib_formats
# set_matplotlib_formats('retina')
import csv
# 生成
# するグループの数
# グループ毎の分散
sigma = [[10, 0], [0, 10]]


print("start")
usecols = ["name","employee_number","company_size_male","company_size_female","average_age","month_average_predetermined_overtime_hours","average_continuous_service_years_Male","average_continuous_service_years_Female","shohyo","tokkyo","others"]
# usecols = ["名前","売上","従業員数","上場or非上場","平均年齢","平均勤続年数","特許数","設立からの経過","平均給与", "時間外労働","女の割合"]
df = pd.read_csv('./test_result.csv',header=0,usecols=usecols,encoding="utf-8_sig").set_index("name")

# filename ="./random.csv"
# df = np.loadtxt(filename,skiprows=1,usecols=(1,-1),delimiter=",")
# plt.figure(figsize=[10,10])

df = df.fillna(1)
# df.dropna(how='all')
model_pca = PCA(n_components=2)
vecs_list = model_pca.fit_transform(df)
#0.73052856 0.24106279で寄与率97.1%
# print(model_pca.explained_variance_ratio_)

# クラスタリング

link = linkage(vecs_list,
method = 'complete', 
# matrix= "mergings"
)

# model = linkage()
n = dendrogram(link,
           orientation='top',
           labels=df.index,
           distance_sort='descending',
           color_threshold=200,
           show_leaf_counts=True)
print(link[0])
t = 0.005*max(link[:,2])
c = fcluster(link, t, criterion="distance")
print(c.max())
print(len(c))

with open("with_classter.csv","w") as w:
   fieldnames = ["name","employee_number","company_size_male","company_size_female","average_age","month_average_predetermined_overtime_hours","average_continuous_service_years_Male","average_continuous_service_years_Female","shohyo","tokkyo","others","class"]
   writer = csv.DictWriter(w, fieldnames=fieldnames)
   writer.writeheader()
   result = []

   use_df = df.drop(df.index[0])
   for index,(i,data) in enumerate(df.iterrows()):
      print(data)
      dic = {}
      for ind,s in enumerate(fieldnames):
         # print(data[ind],ind)
         if ind >9:
            dic[s] = c[index] 
         elif ind == 0:
            dic[s] = i
         else:
            dic[s] = data[ind]
      result.append(dic)
      
   for res in result:
      writer.writerow(res)


# plt.show()

plt.title('IT企業?')
# 結果のプロット
n_clusters = len(df)
n_samples = len(df)
# plt.show()


# # print(n_samples,n_clusters)
# print(type(df))
# print("******************************************************************************")
# print(n.keys())
# for l in n.keys():
#    print(len(n[l]))
# print("******************************************************************************")
# # df1 = pd.DataFrame(n)
df1 = df
# print(df1)
# print("******************************************************************************")


# df1.fillna("NaN")
x1 = []
y1 = []
x2 = []
y2 = []




for i in df1.index:
   try:
      n1 = round(df1.loc[i]["employee_number"])
      n2 = round(df1.loc[i]["company_size_male"])
      
      val = df1.loc[i]["shohyo"]
      n_clusters -= 1
      x1.append(val)
      x2.append(val)
      y1.append(n_clusters)
      y2.append(float(n_samples) / float(n_clusters))
   except ZeroDivisionError:
       y2.append(540.0)



# plt.subplot(2, 1, 1)

# ?plt.show()

