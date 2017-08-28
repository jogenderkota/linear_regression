import numpy as np
import sys
import matplotlib.pyplot as plt
x=[1.5,2.5,3,4,5,6,7]
y=[0.1565656,0.3,0.37,0.45,0.6,0.7,0.9]
plt.scatter(x,y,c='red')
# plt.show()
x_mean=np.mean(x)
y_mean=np.mean(y)
print(x_mean,y_mean)
num=0
for i in range(0,len(x)):
    num=num+((x[i]-x_mean)*(y[i]-y_mean))
print num
deno=0
for i in range(0,len(x)):
    deno=deno+((x[i]-x_mean)**2)
print deno
slope=num/deno
inter=y[0]-slope*x[0]
print(slope,inter)

yt=[]
for i in range(0,len(x)):
    yt.append(slope*x[i]+inter)
print(yt)
plt.plot(x,yt)

print(slope*10+inter)
rs=0
for i in range(0,len(x)):
    rs=rs+((yt[i]-y_mean)**2)/((y[i]-y_mean)**2)
print(rs)
plt.show()
