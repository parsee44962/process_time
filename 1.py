import os
import csv

data = []
with open("gpu_runtime.log","r") as f:
    for line in f.readlines():
        if "Vina-GPU total runtime =" in line:
            break
        else:
            line = line.strip()
            name = os.path.basename(line.split(" ")[6])
            time = line.split(" ")[8]
            data.append({'name':name,'time':time})

f = open('test1.csv','w',encoding='utf8',newline='')  # 指定newline=‘’参数
writer = csv.DictWriter(f,fieldnames=['name','time'])
writer.writeheader() # 将字段写入csv格式文件首行
for line in data:
    writer.writerow(line)