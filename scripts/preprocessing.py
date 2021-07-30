import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

chunksize = 100000
stdscaler = StandardScaler()
#Consider only numeric drivers for our example
numeric_drivers = ['hour','banner_pos','C1','device_type','device_conn_type','C14','C15','C16','C17','C18','C19','C20','C21']

df = pd.read_csv('../data/train.csv',chunksize=chunksize)
for chunk in df:
    stdscaler.partial_fit(chunk[numeric_drivers])
    #continue preprocecssing