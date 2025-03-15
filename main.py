import requests
import datetime
from openpyxl import load_workbook
import os
import time
import json
from outprint import *
import random
import re


def put_request(timestamp, time, objectCode, elderAge, elderName, elderSex):
    # 生成随机的 sbp、dbp、hr、thermometer 和 bloodGlucose 值
    sbp = str(random.randint(90, 140))
    dbp = str(random.randint(60, 90))
    hr = str(random.randint(60, 100))
    thermometer_ori = str(random.uniform(36.0, 36.8))
    thermometer = str(round(float(thermometer_ori), 1))
    bloodGlucose_ori = str(random.uniform(3.9, 6.1))
    bloodGlucose = str(round(float(bloodGlucose_ori), 1))


    url = "https://xn--l6qy95a.fun/baseData/signs/general/add?time="+timestamp

    payload = "{\r\n    \"branchId\": \"23\",\r\n    \"dataTime\": \""+ time +"\",\r\n    \"bmi\": \"\",\r\n    \"sbp\": "+ sbp +",\r\n    \"dbp\": "+ dbp +",\r\n    \"objectCode\": \""+ objectCode + "\",\r\n    \"elderAge\": \""+ elderAge +"\",\r\n    \"elderName\": \""+elderName+"\",\r\n    \"elderSex\": \""+elderSex+"\",\r\n    \"hr\": "+ hr +",\r\n    \"measureNo\": \"\",\r\n    \"thermometer\": "+thermometer+",\r\n    \"remark\": \"\",\r\n    \"bloodGlucose\": "+bloodGlucose+"\r\n}"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://xn--l6qy95a.fun',
        'Referer': 'https://xn--l6qy95a.fun/tenantSide/index.html?time='+timestamp+'/',
        'sec-ch-ua-platform': '"Windows"',
        'organId': '23',
        'branchId': '23',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
        'sec-ch-ua-mobile': '?0',
        'Authorization': 'Bearer sunjiangzhou_23_d288268ed37846c09d649b365325fa24'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    info(response.text)
    
    if response.status_code == 200:
        success("数据上传成功")
    else:
        error("数据上传失败")

def get_start_date(objectCode, timestamp):
    url = "https://xn--l6qy95a.fun/baseData/signs/general/page?objectCode="+objectCode+"&branchId=23&current=1&size=1&time=" + timestamp

    payload = {}
    headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Referer': 'https://xn--l6qy95a.fun/tenantSide/index.html?time='+timestamp+'/',
  'branchId': '23',
  'organId': '23',
  'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'Authorization': 'Bearer sunjiangzhou_23_d288268ed37846c09d649b365325fa24'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    info(response.text)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        try:
            start_date = response_json['data']['data']['records'][0]['dataTime']
            success("目标人员开始时间为"+start_date)
        except IndexError:
            error("目标人员开始时间获取失败")
            start_date = '2024-08-01 10:00:00'
    else:
        error("获取目标人员开始时间失败")
    return start_date
    

def get_stuff_ID(elderNameAndNo, timestamp):
    url = "https://xn--l6qy95a.fun/baseData/data/elderList?elderNameAndNo="+elderNameAndNo+"&size=1&type=all&time="+timestamp

    payload = {}
    headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Referer': 'https://xn--l6qy95a.fun/tenantSide/index.html?time='+timestamp+'/',
  'branchId': '23',
  'organId': '23',
  'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'Authorization': 'Bearer sunjiangzhou_23_d288268ed37846c09d649b365325fa24'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    if response.status_code == 200:
        ID = response_json.get('data')['records'][0]['elderId']
        name = response_json.get('data')['records'][0]['elderName']
        sex = response_json.get('data')['records'][0]['sex']
        age = response_json.get('data')['records'][0]['age']
        info(response.text)
        success("目标人员id为"+ID)
        success("目标人员姓名为"+name)
        success("目标人员性别为"+sex)
        success("目标人员年龄为"+age)
    else:
        error("获取目标人员ID等信息失败")
    return ID, name, sex, age

def get_data_from_excel(file_path):
    if os.path.exists(file_path):
        # 加载 Excel 文件
        workbook = load_workbook(file_path)
        # 选择第一个工作表
        sheet = workbook.active
        # 初始化一个列表来存储读取的数据
        data = []
        # 遍历每一行，并将其添加到列表中
        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        success("读取数据成功！")
        return data
    else:
        error("文件不存在，请检查路径是否正确。")
        return []

if __name__ == '__main__':
    file_path = 'eee.xlsx'
    data = get_data_from_excel(file_path)
    for stuff_ori in data:
        # 正则表达式模式，匹配一个或多个中文字符
        pattern = r'[\u4e00-\u9fff]+'
        # 使用findall方法找到所有匹配的中文字符
        stuff = re.findall(pattern, str(stuff_ori))[0]
        info("当前输入用户："+ str(stuff))
        current_timestamp = str(int(time.time())) #这是post请求中发生的当前时间戳
        info("当前时间戳为:"+ current_timestamp)
        ID, name, sex, age = get_stuff_ID(str(stuff), current_timestamp)
        start_date = get_start_date(ID, current_timestamp) #这是get请求中发生的最近时间戳
        # 首先，将 startTimeDate 转换为 datetime 对象
        startTimeDate = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
        # 然后，将 datetime 对象转换为时间戳
        startTimeStamp = int(time.mktime(startTimeDate.timetuple()))

        while startTimeStamp <= 1740672000:
            startTimeStamp += 604800
            date_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTimeStamp))
            put_request(current_timestamp, date_str, ID, age, name, sex)
            