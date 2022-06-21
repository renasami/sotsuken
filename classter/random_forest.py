import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pylab as plt
import seaborn as sns
from matplotlib.pylab import rcParams
import matplotlib as mpl



rcParams['figure.figsize'] = 15, 6
mpl.rcParams['font.family'] = ['serif']
usecols=["name",'capital','employees','listed','averageAge',
 'femaleRate','averageAnnualIncome','paidHolidayDigestibility',
 'turnoverRate','femaleManagerRate','handicappedEmployeeRate',
 'averageDuration','sales','salesDate','currentEarnings',
 ]

existing_df = pd.read_csv('./analyze.csv',header=0,usecols=usecols).set_index("name")
existing_df = existing_df.fillna(0.0)
existing_df.index.names = ['name']
print(len(existing_df))
dhead = existing_df.head()

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(existing_df)
existing_2d = pca.transform(existing_df)
existing_df_2d = pd.DataFrame(existing_2d)
existing_df_2d.index = existing_df.index
existing_df_2d.columns = ['PC1','PC2']
existing_df_2d.head()

ax = existing_df_2d.plot(kind='scatter', x='PC2', y='PC1', figsize=(16,8))
for i, country in enumerate(existing_df.index):
    ax.annotate(  
        country,
       (existing_df_2d.iloc[i].PC2, existing_df_2d.iloc[i].PC1)
    )
existing_df_2d.plot(kind='scatter',
    x='PC2', y='PC1',
    figsize=(16,8))

plt.show()

