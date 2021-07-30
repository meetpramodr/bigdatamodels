import time
import pandas as pd
import dask.dataframe as dd

class read_data:
    
    def __init__(self, file_path:str):
        self.file_path = file_path
    
    def process_data_linebyline(self):
        start_time = time.time()
        with open(self.file_path,'r') as f:
            for n,line in enumerate(f):
                if n > 0: #ignore the header
                    data = line.rstrip().split(',')
                    #further process data
        print(" -- %s seconds --" % (time.time() - start_time))

    def process_data_dataframechunks(self,chunksize : int):
        start_time = time.time()
        df = pd.read_csv(self.file_path,chunksize=chunksize)
        for chunk in df:
            pass
            #further process chunks
        print(" -- %s seconds --" % (time.time() - start_time))
    
    def process_data_dask(self):
        dtype_dict = {
            'id':'uint64',
            'click':'int64',
            'hour':'int64',
            'C1':'int64',
            'banner_pos':'int64',
            'site_id':'object',
            'site_domain':'object',
            'site_category':'object',
            'app_id':'object',
            'app_domain':'object',
            'app_category':'object',
            'device_id':'object',
            'device_ip':'object',
            'device_model':'object',
            'device_type':'int64',
            'device_conn_type':'int64',
            'C14':'int64',
            'C15':'int64',
            'C16':'int64',
            'C17':'int64',
            'C18':'int64',
            'C19':'int64',
            'C20':'int64',
            'C21':'int64'
        }
        start_time = time.time()
        df = dd.read_csv(self.file_path, dtype=dtype_dict)
        print(" -- %s seconds --" % (time.time() - start_time))
        print(df.head())
        

if __name__ == "__main__":
    readObj = read_data('../data/train.csv')
    #readObj.process_data_linebyline()
    #readObj.process_data_dataframechunks(chunksize=500000)
    readObj.process_data_dask()