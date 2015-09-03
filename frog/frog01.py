import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
#GPIO.setup(24, GPIO.IN )   #
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(24) == GPIO.HIGH:
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)
        sleep(0.01)

except KeyboardInterrupt:
    print "imada!!!"
    pass

#except:    # also work
#    print "imada!!!"
#    pass


#GPIO.cleanup(25)    #only GPIO25
GPIO.cleanup()    #all GPIO


