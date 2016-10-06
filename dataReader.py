import serial;



def writeToCSV(filename):
    while (True):
        newfile.write(ser.readline())

if __name__ == "__main__":
    ser = serial.Serial("/dev/ttyACM0" , 9600) #serial Port here
    newfile = open("newfile.csv", "w")
    writeToCSV(newfile)
