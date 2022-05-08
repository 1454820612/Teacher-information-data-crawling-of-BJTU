import os
import pandas

file_dir='D://download/bjtu/'
num=0

dataList = []
for root, dirs, files in os.walk(file_dir):
    # prefix = prefix + '#'
    print(root)  # 当前目录路径
    # print(dirs) # 当前路径下所有的子目录
    for file in files:
        file_name = file
        #print(file_name)  # 当前路径下所有非目录子文件
        wjm=file_dir+file
        f = open(wjm,'r',encoding='utf-8')
        A=f.read()
        a=A.find('<h1>')
        b=A.find('</h1>')
        teacher_name=A[a+4:b]
        end=file.find('.')
        teacher_id=file[4:end]
        teacher_page="http://faculty.bjtu.edu.cn/{0}/".format(teacher_id)
        
        c=A.find('<p class="border_p">')
        d=A.find('</p>')
        zhicheng=A[c+20:d]
        
        e=A.find('电子邮件')
        f=A.find('@')
        g=f+8
        if A[f+1]=='b':
            g=f+12
        if A[f+2]=='1':
            g=f+8  
        email=A[e+6:g]
        if email=='TY':
            email=''
        
        
        
        
        dataList.append([teacher_name,teacher_id,teacher_page,zhicheng,email])
        dfAll = pandas.DataFrame(dataList, columns=['姓名','工号','主页','职称','电子邮箱'])
result_path = r'D://A2.xlsx'   # 爬取数据文件保存路径
dfAll.to_excel(result_path ) 
        
        