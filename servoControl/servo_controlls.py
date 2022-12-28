
import time # system 


from adafruit_motor import servo # servo library




def move_angle(servo,start, end, delay):
    while start <= end:
        servo.angle = start
        start += 1
        time.sleep(delay)