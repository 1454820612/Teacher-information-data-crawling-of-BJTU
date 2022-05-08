import requests
import pandas
import time

url="http://faculty.bjtu.edu.cn/8822/"

for id in range(10000,20000):
    url = r"http://faculty.bjtu.edu.cn/{0}/".format(id)
    
    wjm='D://download/bjtu/line{0}.txt'.format(id)
    html = requests.get(url)
    html.encoding = 'utf-8'
    A=html.text
    if A.find('Not Found')==-1:
        f = open(wjm,'w',encoding='utf-8')
        f.write(A)
        print(id)
        time.sleep(1)
