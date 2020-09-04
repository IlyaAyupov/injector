import threading

import serial
port = serial.Serial("/dev/ttyUSB0", baudrate=115200)
import scada
import math
data1=[]
data2=[]
voltage=0
throttle=0
injTime=0
RXX=0
for i in range(50):
    data1.append(0)
    data2.append(0)
a=0
sc=scada.Scada()
throttle_ind=[None, 0, 0, 500, 200, 200, 100, "green", "throttle"]
voltage_ind=[None, 0, 200, 500, 200, 200, 15, "green", "voltage"]
inj_ind=[None, 0, 400, 500, 200, 200, 15, "green", "injection time"]
RXX_ind=[None, 0, 600, 500, 200, 200, 100, "green", "RXX"]
throttle_ind[0]=sc.aMeterC(*throttle_ind)[0]
voltage_ind[0]=sc.aMeterC(*voltage_ind)[0]
inj_ind[0]=sc.aMeterC(*inj_ind)[0]
RXX_ind[0]=sc.aMeterC(*RXX_ind)[0]
ss=sc.hTrendC(0,0,500,200,170,"red","pressure",1)[0]
ss2=sc.hTrendC(500,0,500,200,4000,"red","RPM",1)[0]
def thrStuff():
    while True:
        global data1, data2, voltage,injTime, throttle, RXX
        pressure = float(port.readline().decode('utf-8').strip())
        voltage = float(port.readline().decode('utf-8').strip())
        rpm = int(port.readline().decode('utf-8').strip())
        injTime = int(port.readline().decode('utf-8').strip())
        throttle = float(port.readline().decode('utf-8').strip())
        RXX = int(port.readline().decode('utf-8').strip())
        port.readline()
        data1 = data1[1:]
        data2 = data2[1:]
        data1.append(pressure / 1000)
        data2.append(rpm)
def upd():
    global data1, data2, voltage,injTime, throttle
    throttle_ind[1]=throttle
    voltage_ind[1]=voltage
    inj_ind[1]=injTime/10
    RXX_ind[1]=RXX
    sc.aMeter(*throttle_ind)
    sc.aMeter(*voltage_ind)
    sc.aMeter(*inj_ind)
    sc.aMeter(*RXX_ind)
    sc.hTrend((ss, 0, 0, 500, 500, 200, 170, "red", "pressure", 1),data1)
    sc.hTrend((ss2, 0, 500, 0, 500, 200, 4000, "red", "RPM", 1),data2)
    sc.root.after(100,upd)
s=''
while not 'A' in s:
    s=port.readline().decode('utf-8').strip()
threading.Thread(target=thrStuff).start()
sc.root.after(100, upd)
sc.root.mainloop()


