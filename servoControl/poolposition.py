
import time # system 
from board import SCL, SDA # blinka 
from busio import I2C
from adafruit_pca9685 import PCA9685 # PCA Module 

from adafruit_motor import servo # servo library


def pool_position_liftservo():
    lift_servo.angle = 160

def pool_position_groundservo():
    ground_servo.angle = 130

def pool_position_extendservo():
    extend_servo.angle = 10

def pool_position_reachservo():
    reach_servo.angle = 45

def pool_postion():
    pool_position_liftservo()
    pool_position_groundservo()
    pool_position_extendservo()
    pool_position_reachservo()

def move_angle(servo,start, end, delay):
    while start <= end:
        servo.angle = start
        start += 1

        time.sleep(delay)

if __name__ == '__main__':

    FREQ = 50 # for MG996R servo -> operates at 4.8 V    
    
    i2c_bus = I2C(SCL, SDA)
    board = PCA9685(i2c_bus)
    board.frequency = FREQ

    ground_servo = servo.Servo(board.channels[0])
    lift_servo = servo.Servo(board.channels[3])
    extend_servo = servo.Servo(board.channels[4])
    reach_servo = servo.Servo(board.channels[7])
    wrist_servo = servo.Servo(board.channels[8])

    pool_postion()

    

    
    

    

