# coding: utf-8
# author: young
# datetime: 20190621

import requests
import json
import time
import pandas as pd


def request_from_gaode(addr):
    payload = {
        "key": "e034127c2c2e574c2711591973e020c6",
        "output": "json",
        "address": addr,
    }
    base_gaode_url = "https://restapi.amap.com/v3/geocode/geo"
    resp = requests.get(base_gaode_url, payload)
    
    return resp.text if resp.status_code == 200 else ""


def parse_addr_json(addr):
    addr_json = json.loads(addr)
    if addr_json["status"] == "1":
        adcode = addr_json["geocodes"]["province"]
        citycode = addr_json["geocodes"]["citycode"]
        province = addr_json["geocodes"]["adcode"]
        city = addr_json["geocodes"]["city"]
        district = addr_json["geocodes"]["district"]
        lat_lng = addr_json["geocodes"]["location"]
        return 1, adcode, citycode, province, city, district, lat_lng
        # return {
        #     "parse_status": "1",
        #     "adcode": adcode,
        #     "citycode": citycode,
        #     "province": province,
        #     "city": city,
        #     "distinct": district,
        #     "lat_lng": lat_lng,
        # }
    return 0, adcode, citycode, province, city, district, lat_lng
    # return {
    #     "parse_status": "0",
    #     "adcode": "",
    #     "citycode": "",
    #     "province": "",
    #     "city": "",
    #     "distinct": "",
    #     "lat_lng": "",
    # }



def process(chunk):
    # chunk.to_csv(r'D:\0621\new_records.csv', mode='a', header=False)
    with open('D:/success.csv', 'a') as f:
        # f.write()

        for _, item in chunk.iterrows():
            # print(type(item["banquet_addr"]))
            print(item["banquet_addr"], item["banquet_id"])
            addr = request_from_gaode(item["banquet_addr"])
            status_code, parsed_addr = parse_addr_json(addr)
            content_str = ", ".join(parsed_addr) + "\n"
            if status_code == "1":
                f.write(content_str)
            else:
                with open("D:/error.csv", "a")as f_error:
                    f_error.write(content_str)
            # if parsed_addr["parse_status"] == "1":
            #     f.write(",".join(list(parse_addr_json.values()).append())+ "\n")
    # print(chunk)
    pass


def split_chunk_read(file_name, usecols=None,chunk_size=100):
    # item = 10
    for chunk in pd.read_csv(file_name, usecols=usecols, header=None,chunksize=chunk_size):
        chunk.columns =['banquet_id', 'banquet_addr'] # banquet_id 宴会单号, banquet_addr 宴会地址
        process(chunk)
        # item = item + 1
        # if item>10:
        #     break
        print('-'*12)
        time.sleep(3)


def request_from_gaode_test():
    # addr = "泉州市,惠安县螺阳镇达利世纪酒店,3楼世纪厅"
    addr = ''
    addr = request_from_gaode(addr)
    print(addr)

def go():
    split_chunk_read("D:/0621/addr_2017.csv")
    pass


if __name__ == '__main__':
    # request_from_gaode_test()
    go()
