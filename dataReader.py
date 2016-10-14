import serial;



def writeToCSV(filename):
    while (True):
        line = ser.readline()
        print(line)
        newfile.write(line)

if __name__ == "__main__":
    ser = serial.Serial("/dev/ttyACM0" , 9600) #serial Port here
    newfile = open("newfile.csv", "w")
    newfile.write("Sensor_1, Sensor_2")
    writeToCSV(newfile)
