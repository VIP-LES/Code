import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# set up the GPIO channels - one input and one output
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(29, GPIO.IN)
GPIO.setup(31, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(40, GPIO.IN)
GPIO.setup(38, GPIO.IN)
GPIO.setup(36, GPIO.IN)


while (GPIO.imput(32) == 1):
    if (GPIO.input(7) == 1):
        print('0')
    if else (GPIO.input(11) == 1):
        print('1')
    if else (GPIO.input(13) == 1):
        print('2')
    if else (GPIO.input(15) == 1):
        print('3')
    if else (GPIO.input(29) == 1):
        print('4')
    if else (GPIO.input(31) == 1):
        print('5')
    if else (GPIO.input(33) == 1):
        print('6')
    if else (GPIO.input(35) == 1):
        print('7')
    if else (GPIO.input(37) == 1):
        print('8')
    if else (GPIO.input(40) == 1):
        print('9')
    if else (GPIO.input(38) == 1):
        print(',')
    if else (GPIO.input(36) == 1):
        print('\n')
