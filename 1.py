import os
import csv

data = []
with open("runtime.log","r") as f:
    for line in f.readlines():
        line = line.strip()
        soup = line.split('.')[1]
        name = soup.split("=")[0].strip()
        time = soup.split('=')[1].strip()
        data.append({'name':name,'time':time})

f = open('test1.csv','a',encoding='utf8',newline='')  # 指定newline=‘’参数
writer = csv.DictWriter(f,fieldnames=['name','time'])
writer.writeheader() # 将字段写入csv格式文件首行
for line in data:
    writer.writerow(line)