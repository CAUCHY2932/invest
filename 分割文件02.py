# coding:utf-8

import pandas as pd
import time


def process(chunk, file_name):
    chunk.to_csv("./{}.csv".format(file_name))

def split_chunk_read(file_name, usecols=None,chunk_size=100):
    item = 1
    for chunk in pd.read_excel(file_name, usecols=usecols,chunksize=chunk_size):
        # chunk.columns =['banquet_id', 'banquet_addr'] # banquet_id 宴会单号, banquet_addr 宴会地址
        new_file_name = '{}_{}'.format(file_name, item)
        process(chunk, new_file_name)
        item = item + 1
        print('--generate {}.xls file!--'.format(new_file_name))
        # time.sleep(0.5)


def go():

    pass


if __name__ == '__main__':
    pass
    
