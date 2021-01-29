# coding: utf-8
'''
Author: cA7dEm0n
Blog: http://www.a-cat.cn
Since: 2021-01-29 00:26:28
Motto: 欲目千里，更上一层
'''
import os
import logging 
import hashlib
import json
from functools import lru_cache

logging.basicConfig(
        filename='xcopy.log',
        level=logging.DEBUG,
        format='%(asctime)s xcopy: %(message)s'
)

def notify(title, text):
    '''
    description: Mac弹窗
    '''
    os.system("""
    osascript -e 'display notification "{}" with title "{}"'
    """.format(text, title))

@lru_cache(2**6)
def readJsonFromFile(file):
    '''
    description: 从文件读取json
    '''
    _data = {}
    try:
        with open(file) as f:
            _data = json.load(f)
    except Exception as error:
        logging.error("readJsonFromFile Error: %s" % error)
    return _data


def writeJsonToFile(data, file):
    '''
    description: 数据写入json文件
    ''' 
    try:       
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as error:
        logging.error("writeJsonToFile Error: %s" % error)
        return False
    
@lru_cache(2**6)
def md5Calc(file):
    '''
    description: md5计算
    '''
    md5_value=hashlib.md5()
    with open(file,'rb') as file_b:
        while True:
            data_flow = file_b.read(8096)      
            if not data_flow:
                break
            md5_value.update(data_flow)
    file_b.close()
    return md5_value.hexdigest()