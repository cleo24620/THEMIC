# -*- coding: utf-8 -*-
# @Author  : cleo
# @Software: PyCharm


from pathlib import Path
import cdflib
import pandas as pd
import numpy as np

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
    :return cdf_file:
    :return data: remove empty data
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
    return formatted_time


def get_con_subs(time_series, diff=60):
    # 计算相邻时间点之间的差异（单位为天）
    diffs = np.diff(time_series)

    # 识别连续性断点（这里假设连续的定义是每天一个数据点，断点大于1天）
    breaks = np.where(diffs > diff)[0] + 1

    # 分割时间序列
    continuous_subsequences = np.split(time_series, breaks)

    return continuous_subsequences


def split_array(arr, chunk_size=20):
    """将列表分割成指定大小的多个子列表"""
    # 计算应保留的元素总数（剔除最后不满20个元素的部分）
    num_elements_to_keep = (arr.size // chunk_size) * chunk_size

    # 截取数组以保留完整的子数组部分
    trimmed_arr = arr[:num_elements_to_keep]

    # 分割数组为每20个元素一个子数组
    subarrays = np.split(trimmed_arr, num_elements_to_keep // 20)

    return subarrays


def check_same_sign(arr):
    # 检查是否全为正数
    all_positive = np.all(arr > 0)
    # 检查是否全为负数
    all_negative = np.all(arr < 0)

    # 如果全为正或全为负，则不含异号元素
    return all_positive or all_negative
