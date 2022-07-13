# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@project: Excel-打开中文乱码解决方案
@auther: Lijunyan 
@file: Image.py
@date: 2022/7/11 14:59
@email: li_junyan_12345@163.com
'''
import os, sys

# 打开文件
path = os.getcwd()
dirs = os.listdir( path )

# 输出所有文件和文件夹
for file in dirs:
   print (file)