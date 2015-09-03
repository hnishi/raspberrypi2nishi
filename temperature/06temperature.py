# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

# MCP3002からSPI通信で8ビットのデジタル値を取得。0から1の2チャンネル使用可
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if adcnum > 1 or adcnum < 0:
        return -1
    GPIO.output(cspin, GPIO.HIGH)
    GPIO.output(clockpin, GPIO.LOW)
    GPIO.output(cspin, GPIO.LOW)

    commandout = adcnum
    commandout |= 0x18  # スタートビット＋シングルエンドビット
    commandout <<= 3    # LSBから8ビット目を送信するようにする
    for i in range(5):
        # LSBから数えて8ビット目から4ビット目までを送信
        if commandout & 0x80:
            GPIO.output(mosipin, GPIO.HIGH)
        else:
            GPIO.output(mosipin, GPIO.LOW)
        commandout <<= 1
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
    adcout = 0
    #  9ビット読む（ヌルビット＋ 8ビットデータ）
    for i in range( 9):
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
        adcout <<= 1
        if i>0 and GPIO.input(misopin)==GPIO.HIGH:
            adcout |= 0x1
    GPIO.output(cspin, GPIO.HIGH)
    return adcout

GPIO.setmode(GPIO.BCM)
# ピンの名前を変数として定義
SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8
# SPI通信用の入出力を定義
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)

try:
    while True:
        inputVal0 = 0.0
        inputVal0 = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
        volt = (inputVal0 * 3300.0)/1024  # 1024(10bit)
        degree = (volt - 500.0)/10  # 0 degree -> 500 mV
        print("%3.2f"%degree)
        #print("{0:.2f}".format(degree))
        #sleep(0.2)
        sleep(1)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
