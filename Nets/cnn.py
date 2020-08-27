import numpy as np
class AdalineGD(object):
    def _init_(self,eta = 0.00001,n_iter=10000):
        self.eta = eta
        self.n_iter = n_iter
    def fit(self,X,y):
        self.w_ = np.zeros(1+X.shape[1])
        self.cost_ = []
        self._init_()
        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] = self.w_[1:] + self.eta * X.T.dot(errors)
            self.w_[0] = self.w_[0] + self.eta * errors.sum()
            cost = (errors ** 2).sum()/2.0
            self.cost_.append(cost)
        return self
    def net_input(self,X):
        return np.dot(X,self.w_[1:]) + self.w_[0]
    def activation(self,X):
        return self.net_input(X)
    def predict(self,X):
        return np.where(self.activation(X) >= 0,1,0)

file = "C:/Users\wanghuiming\Desktop\Python\CNN/result of json.csv"
import pandas as pd
df = pd.read_csv(file, header=None)
import numpy as np

import numpy as np

X = df.iloc[0:966,[0,1,2,3,4,8,9]].values
y = df.loc[0:966,7].values

y_max = y.max()
y = y/y_max
print(y)

import matplotlib.pyplot as plt
X[:,6] = np.where((X[:,6] == '国产') | (X[:,6]=='国产（合拍）' )| (X[:,6]=='国产（上映中……）'),0,1)
#print(X[5:10])
"""
发行类别的初始化
"""

X[:,1] = 0.1 * X[:,1]
#print(X[:])
"""
豆瓣评分的初始化
"""

#y_max = X[:,0].max()
#print(y_max)
#X[:, 0] = 1
#print(X[:])
"""
票房的初始化
"""

for i in range(936):
    #print(y_type[i])
    if X[:,4][i].find("动作")>=0 or X[:,4][i].find("科幻")>=0 or X[:,4][i].find("剧情")>=0 or X[:,4][i].find("喜剧")>=0:
        X[:, 4][i] = 1
    else:
        X[:, 4][i] = 0
#y_type[i] = np.where((y_type[i] == "动作"),1,0)
#print(y_type)
#print(X[:,4])
"""
电影类型的初始化
"""
#print(X[:, 0])
for i in range(936):
    #print(y_con[i])
    if X[:, 0][i].find("2")>=0 or X[:, 0][i].find("3")>=0 or X[:, 0][i].find("4")>=0 or X[:, 0][i].find("5")>=0 or X[:, 0][i].find("6")>=0 or X[:, 0][i].find("7")>=0 or X[:,0][i].find("8")>=0:
        X[:, 0][i] = 1
    else:
        X[:, 0][i] = 0
#y_type[i] = np.where((y_type[i] == "动作"),1,0)
#print(y_con)
#print(X[:, 0])
"""
续集的初始化
"""

file1 = "C:/Users\wanghuiming\Desktop\Python\CNN/result of doc_China.csv"
import pandas as pd1
df1 = pd1.read_csv(file1, header=None)
doctor = df1.loc[0:100,1].values
cnt = 0
for i in range(936):
    cnt = 0
    for d in doctor:
        if X[:, 2][i].find(d)>=0:
            X[:, 2][i] = 1
            cnt = 1
            break
        else:
            continue
    if cnt != 1 :
        X[:, 2][i] = 0
#print(y_doctor)
#print(X[:, 2])
"""
导演的初始化
"""

file2 = "C:/Users\wanghuiming\Desktop\Python\CNN/result of actor_China.csv"
import pandas as pd2
df2 = pd2.read_csv(file2, header=None)
actor = df2.loc[0:100,1].values
cnt = 0
for i in range(936):
    cnt = 0
    for a in actor:
        if X[:,3][i].find(a)>=0:
            cnt = cnt+1
        else:
            continue
    X[:, 3][i] = cnt
#print(y_actor)
#print(X[:])
"""
演员的初始化
"""

for i in range(936):
    #print(y_type[i])
    if X[:,5][i].find("3月")>=0 or X[:,5][i].find("9月")>=0 or X[:,5][i].find("11月")>=0:
        X[:, 5][i] = 0
    elif X[:,5][i].find("2014年") >= 0 or X[:,5][i].find("2013年") >= 0 or X[:,5][i].find("2012年") >= 0 or X[:,5][i].find("2010年") >= 0 or X[:,5][i].find("2009年") >= 0:
        X[:, 5][i] = 0
    else:
        X[:, 5][i] = 1
#y_type[i] = np.where((y_type[i] == "动作"),1,0)
#print(y_time)
#print(X[0:11])
"""
档期的初始化
"""
#print(X[10:13])

print(X)
"""
plt.scatter(y_time,y,color = 'blue',marker='x',label = 'people')
#plt.scatter(y,color = 'blue',marker = 'x',label = 'kind')
plt.xlabel('score')
plt.ylabel('money')
plt.legend(loc = 'upper left')
plt.show()
"""

ada = AdalineGD()
ada.fit(X,y)
print(ada.w_)
now = X[900]
print(ada.predict(X))
print((now.T.dot(ada.w_[1:])+ada.w_[0]))

