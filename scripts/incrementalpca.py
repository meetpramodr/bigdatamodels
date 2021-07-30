import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import IncrementalPCA, PCA
from matplotlib import pyplot as plt

chunksize = 10000
numeric_drivers = ['hour','banner_pos','C1','device_type','device_conn_type','C14','C15','C16','C17','C18','C19','C20','C21']

df = pd.read_csv('../data/train.csv',usecols=numeric_drivers,nrows=1000000)

#Perform scaling
stdscaler = StandardScaler()
df = stdscaler.fit_transform(df)

#fit the Incremental PCA
pcainc = IncrementalPCA(n_components=len(numeric_drivers),batch_size=10000,copy=False,whiten=True)
pcainc.fit(df)

#find components that are explaining more than 85% of the variance
print(np.where(pcainc.explained_variance_ratio_.cumsum()<=0.85)[0].shape)

#plot the explained variance chart
plt.plot(range(0,len(numeric_drivers)),pcainc.explained_variance_ratio_,'bx-')
plt.xlabel('# Principal Components')
plt.ylabel('Explained Variance')
plt.title('Determine the # of PrinComps using explained variance')
plt.show()

#plot the cumulative explained variance chart
plt.plot(range(0,len(numeric_drivers)),pcainc.explained_variance_ratio_.cumsum(),'bx-')
plt.xlabel('# Principal Components')
plt.ylabel('Total Explained Variance')
plt.title('Determine the # of PrinComps using explained variance')
plt.show()


