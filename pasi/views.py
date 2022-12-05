import json
import os
import xlrd, xlwt
import random
import shutil

# 引入redirect重定向模块
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required




web_url = 'http://127.0.0.1:8000/'


def global_params(request):

    global web_url

    return {
        'web_url': web_url,
    }



'''
# Pasi@CDD job
'''


def pasi(request):
    Photo_src = './media/photo/'

    Photo_Dict = {}

    filelist = os.listdir(Photo_src)

    if filelist:

        for i in range(0, len(filelist)):
            # 读入文件名；
            Photo_Name = filelist[i]

            # 读入文件的路径；
            Photo_Dir = filelist[i]


            Photo_Dict.update({Photo_Name: Photo_Dir})

    else:
        print("No files in this folder")

    title = 'Psoriasis Area and Severity Index (PASI) Analysis'

    # 需要传递给模板的对象
    context = {
        'title': title,
        'Photo_Dict': Photo_Dict,
    }

    # 载入模板，并返回context对象
    return render(request, 'pasi.html', context)


def pasi_summary(request):
    # 获取 POST 参数
    all_data = request.body
    pasi_str = all_data.decode()
    # print(pasi_str)
    pasi_list = pasi_str.split("&")
    # print(pasi_list)
    pasi_dict = {}
    for item in pasi_list:
        list_tempt = item.split("=")
        pasi_dict.update({list_tempt[0]: list_tempt[1]})

    pasi_dict.pop("csrfmiddlewaretoken")
    # print(pasi_dict)

    pasi_dict_amended = {}
    for key, value in pasi_dict.items():
        Dict_tempt = {}
        key_list = key.split("_")

        if pasi_dict_amended.__contains__(key_list[0]):
            if key_list[1] == 'erythema':
                pasi_dict_amended[key_list[0]]['erythema'] = value

            if key_list[1] == 'incrassation':
                pasi_dict_amended[key_list[0]]['incrassation'] = value

            if key_list[1] == 'scales':
                pasi_dict_amended[key_list[0]]['scales'] = value

        else:
            if key_list[1] == 'erythema':
                Dict_tempt['erythema'] = value

            if key_list[1] == 'incrassation':
                Dict_tempt['incrassation'] = value

            if key_list[1] == 'scales':
                Dict_tempt['scales'] = value

            pasi_dict_amended.update({key_list[0]: Dict_tempt})

    # print(pasi_dict_amended)

    # 创建Excel文件
    excel_src = r'D:\djangoProject\psoriasis\media\score\pasi.xls'
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet("pasi")
    worksheet.write(0, 0, 'Photo Name')
    worksheet.write(0, 1, 'erythema')
    worksheet.write(0, 2, 'incrassation')
    worksheet.write(0, 3, 'scales')

    Row_number = 1

    for key, value in pasi_dict_amended.items():
        photo_number = int(key.split(".")[0])
        worksheet.write(Row_number, 0, photo_number)

        for index, score in value.items():

            score = int(score)
            if index == 'erythema':
                worksheet.write(Row_number, 1, score)

            if index == 'incrassation':
                worksheet.write(Row_number, 2, score)

            if index == 'scales':
                worksheet.write(Row_number, 3, score)

        # 循环叠加
        Row_number = Row_number + 1

    # 保存Excel文件
    workbook.save(excel_src)

    title = 'Psoriasis Area and Severity Index (PASI) Analysis'

    # 需要传递给模板的对象
    context = {
        'title': title,
        'excel_src': excel_src,
    }

    # 载入模板，并返回context对象
    return render(request, 'pasi_summary.html', context)


'''
# 首页
'''


def index(request):
    greetings = 'Hello'
    context = {
        'greetings': greetings,

        }
    return render(request, 'index.html', context)

