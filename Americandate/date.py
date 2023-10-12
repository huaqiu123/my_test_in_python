#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Roc-xb
"""
from datetime import datetime
from xlrd import xldate_as_tuple
 
'''
函数功能：将天数格式化为日期字符串
天数：表示从1990-01-01到某天的天数
'''
def days_to_date_str(days):
    real_date = datetime(*xldate_as_tuple(days, 0)).strftime('%Y-%m-%d')

    print(real_date)
    return real_date
 
# if __name__ == '__main__':
#     days = 111
#     days_to_date_str(days)