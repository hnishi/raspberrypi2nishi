import RPi.GPIO as GPIO
from time import sleep


def my_callback(channel):
    global ledState
    if channel==24:
        ledState = not ledState
        if ledState == GPIO.HIGH:
            GPIO.output(25, GPIO.HIGH)
        else:
            GPIO.output(25, GPIO.LOW )


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback, bouncetime=200) #200ms


ledState = GPIO.LOW


try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    print "imada!!!"
    pass

#except:    # also work
#    print "imada!!!"
#    pass


#GPIO.cleanup(25)    #only GPIO25
GPIO.cleanup()    #all GPIO


