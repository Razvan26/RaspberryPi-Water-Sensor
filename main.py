import RPi.GPIO as GPIO
import time
import smtplib

def sendemail(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    fromMy = "emailFrom"
    toMy   = "emailTo"
    server.login(fromMy, "password")
    try:
        server.sendmail(fromMy, toMy, message)
        print("Message has been sended")
    finally:
        server.quit()
        print("Server down!")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
prev = 0
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.IN)
print("Initialization...")
watherSensor = GPIO.input(19)

sendemail("Raspberry pi is on")
time.sleep(1)
print("Raspberry pi is ready")
while True:

    if(watherSensor== 1):
        GPIO.output(26, GPIO.HIGH)
        prev = 1
        print("Apa")
    else:
        GPIO.output(26, GPIO.LOW)
        #prev = 0
    if prev != watherSensor:
        prev = watherSensor
        if prev == 1:
            sendemail("wather found!")
        else:
            sendemail("wather was eliminated!")
