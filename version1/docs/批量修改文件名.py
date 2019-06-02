# -*- coding:utf-8 -*- 
"""     
:author: young     
:DATE: 2019-05-29 11:36:15     
:copyright: © 2019 young <haochen2932@foxmail.com>     
:license: None, see LICENSE for more details. 
""" 

import os


def rename(file_name):
    # flag = 0
    if '-' in file_name:
        new_name = file_name.replace('-', '_')
        os.rename(file_name, new_name)
        print('has rename file {} -> {}'.format(file_name, new_name))
        # flag = 1


def process():
    for file_name in os.walk('./'):
        # print(file_name[1])
        if len(file_name[0])!=0:
            # print(file_name[0])
            # for item in file_name:
            #     print(item)
            rename(file_name[0])
            # print('-'*5)
    

if __name__ == "__main__":
    process()
