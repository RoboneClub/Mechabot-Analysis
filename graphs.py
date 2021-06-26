import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
"""importing data from CSV files"""
data = pd.read_csv('data01.csv')
time = data.iloc[:,1].values
tilt = data.iloc[:,4:7].values
gyro = data.iloc[:,7:10].values
magn = data.iloc[:,10:13].values
acc = data.iloc[:,13:].values
img = data.iloc[:,-1]
"""importing time, tilt, gyroscope, magnetometer, acceleration, and img values"""
"""
t = []
for i in time:
    t.append(i.split(":"))

start_time = float(t[0][0])*3600 + float(t[0][1])*60 + float(t[0][2]) -1
rate = []

for index in range(len(img)):
    delta_time = float(t[index][0])*3600 + float(t[index][1])*60 + float(t[index][2]) - start_time
    rate.append(img[index]/delta_time)
plt.title("img rate")
plt.plot(time[10:],rate[10:],color = 'blue')
plt.scatter(time[10:],rate[10:],color = "red")
plt.xlabel("Time")
plt.ylabel("Rate of taking images")
plt.show()

delay = []
i = 1
img_no = 1
time_of_img = start_time
while(i<len(img)-1):
    while(img[i]==img_no and i <len(img)-1):
        i+=1
    delay.append(float(t[i][0])*3600 + float(t[i][1])*60 + float(t[i][2])-time_of_img)
    time_of_img = float(t[i][0])*3600 + float(t[i][1])*60 + float(t[i][2])
    img_no +=1
plt.plot(range(1,img_no),delay)
plt.show()
fig, (ax1, ax2,ax3) = plt.subplots(3)
fig.suptitle('Magnometer')
l1, = ax1.plot(time,magn[:,0],color='r',label="dsads")
l2, = ax2.plot(time,magn[:,1],color='b')
l3, = ax3.plot(time,magn[:,2],color='g')
plt.legend([l1, l2, l3],["MagnX", "MagnY", "MagnZ"])
plt.show()

fig, (ax1, ax2,ax3) = plt.subplots(3)
fig.suptitle('Tilting')
l1, = ax1.plot(time,tilt[:,0],color='r',label="dsads")
l2, = ax2.plot(time,tilt[:,1],color='b')
l3, = ax3.plot(time,tilt[:,2],color='g')
plt.legend([l1, l2, l3],["Pitch", "Roll", "Yaw"])
plt.show()

fig, (ax1, ax2,ax3) = plt.subplots(3)
fig.suptitle('Accel')
l1, = ax1.plot(time,acc[:,0],color='r',label="dsads")
l2, = ax2.plot(time,acc[:,1],color='b')
l3, = ax3.plot(time,acc[:,2],color='g')
plt.legend([l1, l2, l3],["AccX", "AccY", "AccZ"])
plt.show()

fig, (ax1, ax2,ax3) = plt.subplots(3)
fig.suptitle('Gyro')
l1, = ax1.plot(time,gyro[:,0],color='r',label="dsads")
l2, = ax2.plot(time,gyro[:,1],color='b')
l3, = ax3.plot(time,gyro[:,2],color='g')
plt.legend([l1, l2, l3],["GyroX", "GyroY", "GyroZ"])
plt.show()


"""

"""plotting the graphs"""
plt.title("Magn")
plt.plot(time,magn[:,0],color = 'blue',label="x-Magnometer")
plt.plot(time,magn[:,1],color = 'red',label="y-Magnometer")
plt.plot(time,magn[:,2],color = 'green',label="z-Magnometer")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Magnetic Field")
plt.show()

plt.title("Gyro")
plt.plot(time,gyro[:,0],color = 'blue',label="x-Gyro")
plt.plot(time,gyro[:,1],color = 'red',label="y-Gyro")
plt.plot(time,gyro[:,2],color = 'green',label="z-Gyro")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Gyro")
plt.show()
