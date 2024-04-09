# -*- coding: utf-8 -*-
# @Author  : cleo
# @Software: PyCharm


from pathlib import Path
import cdflib
import pandas as pd

# get my current path
dir_p = Path('.')
# Traverse the dir to get all .cdf files
cdf_fs = [f for f in dir_p.glob('*.cdf')]
# print the name of each file line by line
for f in cdf_fs:
    print(f)

def pre_cdf(f):
    """
    print the necessary information
    :return cdf_file
    """
    cdf_file = cdflib.CDF(f)
    variables = cdf_file.cdf_info().zVariables
    data = {}
    for v in variables:
        try:
            data[v] = cdf_file.varget(v)
        except Exception as e:
            print(e)
    print(data.keys())
    return cdf_file, data


def formatted_time(timestamp):
    """
    format the timestamp
    :param timestamp:
    :return:
    """
    from datetime import datetime
    # 使用 datetime.fromtimestamp() 将时间戳转换为 datetime 对象
    dt_object = datetime.fromtimestamp(timestamp)

    # 将 datetime 对象格式化为字符串
    # 这里 "%Y-%m-%d %H:%M:%S" 是一个常见的格式，表示年-月-日 时:分:秒
    # 你可以根据需要调整这个格式
    formatted_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_time)