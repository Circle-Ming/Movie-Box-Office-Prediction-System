file = "C:/Users\wanghuiming\Desktop\Python\CNN/result of json.csv"
import pandas as pd
df = pd.read_csv(file, header=None)
import numpy as np

import matplotlib.pyplot as plt
y_ctype = df.loc[0:936,9].values
y_ctype = np.where((y_ctype == '国产') | (y_ctype=='国产（合拍）' )| (y_ctype=='国产（上映中……）'),0,1)
#print(y_ctype)
"""
发行类别的初始化
"""

y_score = df.loc[0:936,1].values
y_score = 0.1 * y_score
#print(y_score)
"""
豆瓣评分的初始化
"""

y = df.loc[0:936,7].values
y_max = y.max()
#print(y_max)
y = y/y_max
#print(y)
"""
票房的初始化
"""

y_type = df.loc[0:936,4].values
for i in range(936):
    #print(y_type[i])
    if y_type[i].find("动作")>=0 or y_type[i].find("科幻")>=0 or y_type[i].find("剧情")>=0 or y_type[i].find("喜剧")>=0:
        y_type[i] = 1
    else:
        y_type[i] = 0
#y_type[i] = np.where((y_type[i] == "动作"),1,0)
#print(y_type)
"""
电影类型的初始化
"""

y_con = df.loc[0:936,0].values
for i in range(936):
    #print(y_con[i])
    if y_con[i].find("2")>=0 or y_con[i].find("3")>=0 or y_con[i].find("4")>=0 or y_con[i].find("5")>=0 or y_con[i].find("6")>=0 or y_con[i].find("7")>=0 or y_con[i].find("8")>=0:
        y_con[i] = 1
    else:
        y_con[i] = 0
#y_type[i] = np.where((y_type[i] == "动作"),1,0)
#print(y_con)
"""
续集的初始化
"""

file1 = "C:/Users\wanghuiming\Desktop\Python\CNN/result of doc_China.csv"
import pandas as pd1
df1 = pd1.read_csv(file1, header=None)
y_doctor = df.loc[0:936,2].values
doctor = df1.loc[0:100,1].values
cnt = 0
for i in range(936):
    cnt = 0
    for d in doctor:
        if y_doctor[i].find(d)>=0:
            y_doctor[i] = 1
            cnt = 1
            break
        else:
            continue
    if cnt != 1 :
        y_doctor[i] = 0
#print(y_doctor)
"""
导演的初始化
"""

file2 = "C:/Users\wanghuiming\Desktop\Python\CNN/result of actor_China.csv"
import pandas as pd2
df2 = pd2.read_csv(file2, header=None)
y_actor = df.loc[0:936,3].values
actor = df2.loc[0:100,1].values
cnt = 0
for i in range(936):
    cnt = 0
    for a in actor:
        if y_actor[i].find(a)>=0:
            cnt = cnt+1
        else:
            continue
    y_actor[i] = cnt
#print(y_actor)
"""
演员的初始化
"""

y_time = df.loc[0:936,8].values
for i in range(936):
    #print(y_type[i])
    if y_time[i].find("3月")>=0 or y_time[i].find("9月")>=0 or y_time[i].find("11月")>=0:
        y_time[i] = 0
    elif y_time[i].find("2014年") >= 0 or y_time[i].find("2013年") >= 0 or y_time[i].find("2012年") >= 0 or y_time[i].find("2010年") >= 0 or y_time[i].find("2009年") >= 0:
            y_time[i] = 0
    else:
        y_time[i] = 1
#y_type[i] = np.where((y_type[i] == "动作"),1,0)
print(y_time)
"""
档期的初始化
"""


"""
plt.scatter(y_time,y,color = 'blue',marker='x',label = 'people')
#plt.scatter(y,color = 'blue',marker = 'x',label = 'kind')
plt.xlabel('score')
plt.ylabel('money')
plt.legend(loc = 'upper left')
plt.show()
"""
