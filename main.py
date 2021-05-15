import numpy as np 
import matplotlib.pyplot as plt 


F = 10 
d=25
type = 0
h = 10
Height = 20


OsX=[]
OsY=[]
PredmetX=[]
PredmetY=[]
LensX=[]
LensY=[]

if type == 0:
  f = 1 / (1 / F - 1 / d)

for i in range(100):
  OsX.append(-d+(f+d)*i/100)
  OsY.append(0)
  PredmetX.append(-d)
  PredmetY.append(0+h*i/100)
  LensX.append(0)
  LensY.append(-Height+2*Height*i/100)

k = - h / d
r = - h / F

LX=[]
L1Y=[]
L2Y=[]

for i in range(100):
  x=-d+d*i/100
  LX.append(x)
  L1Y.append(h)
  L2Y.append(k*(x+d)+h)

LX_2=[]
L1Y_2=[]
L2Y_2=[]

for i in range(100):
  x=0+f*i/100
  LX_2.append(x)
  L1Y_2.append(r*x+h)
  L2Y_2.append(k*x)

H=k*f

ImageX=[]
ImageY=[]

for i in range(100):
  ImageX.append(f)
  ImageY.append(H*i/100)


fig=plt.figure(facecolor='white')
plt.plot(PredmetX, PredmetY, color='b', linewidht=5)
plt.plot(OsX, OsY, '--', linewidht=4, color='g')
plt.plot(ImageX, ImageY, color='b', linewidht=5)
plt.plot(LensX, LensY, '--', linewidht=4, color='g')
plt.plot(LX, L1Y, '--', color='y')
plt.plot(LX, L2Y, '--', color='y')
plt.plot(LX_2, L1Y_2, '--', color='y')
plt.plot(LX_2, L2Y_2, '--', color='y')
plt.ylabel("x")
plt.xlabel("y")
plt.grid(True)
plt.show()
