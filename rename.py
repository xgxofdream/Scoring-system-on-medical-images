# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:23:10 2022

@author: liujie
"""

import os
import xlrd, xlwt
import random
import shutil

Original_folder = r'F:\MYH\Original/'
Renamed_folder = r'F:\MYH\Renamed/'
Excel_of_Names = r'F:\MYH\rename.xlsx'
Initial_number = 1

# 创建Excel文件
workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet("Renaming")

Dict_Name = {}

filelist = os.listdir(Original_folder)

if filelist:

    for i in range(0, len(filelist)):
        # 读入原始文件名；
        Old_Name = filelist[i]

        # 生成随机整数；
        Random_Int = random.randint(0, 10000)

        # 往字典 Dict_Name 中写入原始文件名和配对的随机数字
        # Key = 随机数字，value = 原始文件名
        Dict_Name.update({Random_Int: Old_Name})

        # 按照Key(Random_Int)的大小给字典排序
        # 注意，sorted返回的是列表格式
        Dict_Name_Sorted = sorted(Dict_Name.items(), key=lambda x: x[0])

        # 将列表 Dict_Name_Sorted 转化成字典格式
        Dict_Name_Increasing_Order = dict(Dict_Name_Sorted)

    Row_number = 0
    for key, value in Dict_Name_Increasing_Order.items():
        print(str(key) + "  ->  " + str(value))

        New_Name = str(Row_number + Initial_number) + ".JPG"
        # 往Excel文件中写入老的文件名（value），与之对应的随机数字（key），和通过排序得到的新文件名（New_Name）
        worksheet.write(Row_number, 0, value)
        worksheet.write(Row_number, 1, key)
        worksheet.write(Row_number, 2, New_Name)

        # 重命名和移动到新的文件夹 Renamed_folder
        shutil.copyfile(Original_folder + value, Renamed_folder + New_Name)

        # 循环叠加
        Row_number = Row_number + 1

    # 保存Excel文件
    workbook.save(Excel_of_Names)

else:
    print("No files in this folder")