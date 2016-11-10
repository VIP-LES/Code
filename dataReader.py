import serial;
import datetime;
import time;




def writeToCSV(filename):
    while (True):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        line = ser.readline()
        line = (st + " , ") + line
        print(line)
        newfile.write(line)

if __name__ == "__main__":
    ser = serial.Serial("/dev/ttyACM0" , 250000) #serial Port here
    newfile = open("newfile.csv", "w")
    newfile.write("Sensor_1")
    
    writeToCSV(newfile)
