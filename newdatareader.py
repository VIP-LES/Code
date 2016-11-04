import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

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
GPIO.setup(32, GPIO.IN)


GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



while (1):
    if (GPIO.input(7) == 1):
        print('0')
    elif (GPIO.input(11) == 1):
        print('1')
    elif (GPIO.input(13) == 1):
        print('2')
    elif (GPIO.input(15) == 1):
        print('3')
    elif (GPIO.input(29) == 1):
        print('4')
    elif (GPIO.input(31) == 1):
        print('5')
    elif (GPIO.input(33) == 1):
        print('6')
    elif (GPIO.input(35) == 1):
        print('7')
    elif (GPIO.input(37) == 1):
        print('8')
    elif (GPIO.input(40) == 1):
        print('9')
    elif (GPIO.input(38) == 1):
        print(',')
    elif (GPIO.input(36) == 1):
        print('\n')
