# coding:utf-8

import pandas as pd
import time


def process(chunk, file_name):
    # chunk.to_csv(r'D:\0621\new_records.csv', mode='a', header=False)
    # for _, item in chunk.iterrows():
    #     # print(type(item["banquet_addr"]))
    #     print(item["banquet_addr"], item["banquet_id"])
    # # print(chunk)
    # pass
    chunk.to_csv("./{}.csv".format(file_name))

def split_chunk_read(file_name, usecols=None,chunk_size=100):
    item = 1
    for chunk in pd.read_csv(file_name, usecols=usecols, header=None,chunksize=chunk_size):
        # chunk.columns =['banquet_id', 'banquet_addr'] # banquet_id 宴会单号, banquet_addr 宴会地址
        process(chunk, item)
        item = item + 1
        print('--generate {}.csv file!--'.format(item))
        # time.sleep(0.5)


def go():

    pass


if __name__ == '__main__':
    pass
    
