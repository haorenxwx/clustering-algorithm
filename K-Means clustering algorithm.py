#K-Means clustering algorithm

#利用sklearn实现kmeans算法
from sklearn.cluster import KMeans
kms=KMeans(n=cluster=3)
y=kms.fit_predict(x)


#例题，聚类算法分析客户价值
import pandas as pda
import numpy as npy
import matplotlib.pylab as pylab
fname="path of data"
dataf=pda.read_csv(fname,encoding="gbk")
x=dataf.as_matrix()#所有的特征值
from sklearn.cluster import KMeans
kms=KMeans(n_cluster=3)#划分成3类
y=kms.fit_predict(x)
print(y)
#y就是调用后的聚类结果


#画图分析每一类的特征，看各个类别代表的哪一类
#技巧1：如果有多个特征，把特征中相关联的组合
						#(如果不确定关联性可以直接组合)

#根据结合的特征画子图：年龄-消费金额图，消费时间-消费金额图，年龄-消费时间图

for i in range(0,len(y)):
	if(y[i]==0):
		#print(str(i)+"大众客户")
		pyl.subplot(2,3,1)
		#年龄-消费金额图
		pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*r")
		pyl.subplot(2,3,2)
		#消费时间-消费金额图
		pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*r")
		pyl.subplot(2,3,3)
		#年龄-消费时间
		pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"*r")
	elif(y[i]==1):
		#print(str(i)+"超级vip") 黄的
		pyl.subplot(2,3,1)
		#年龄-消费金额图
		pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"sy")
		pyl.subplot(2,3,2)
		#消费时间-消费金额图
		pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"sy")
		pyl.subplot(2,3,3)
		#年龄-消费时间
		pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"sy")
	elif(y[i]==2):
		#print(str(i)+"vip客户") 蓝的
		pyl.subplot(2,3,1)
		#年龄-消费金额图
		pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"pb")
		pyl.subplot(2,3,2)
		#消费时间-消费金额图
		pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"pb")
		pyl.subplot(2,3,3)
		#年龄-消费时间
		pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"pb")

#技巧2：把散乱的子图删掉(表示和统一的分类标准不一置)
		#根据常识进行分析得出初步结论