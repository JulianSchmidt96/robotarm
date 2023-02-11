# ----------------------------
# LIBRARIES

# External libraries
import time
# Import the PCA9685 module.
import Adafruit_PCA9685
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import pandas

from servo import Servo


class RobotArm:

    # PARAMETERS
    PWM_BOARD_RESOLUTION = 4096 # PWM control board resolution
    SERVO_MOTOR_FREQUENCY = 50 #In Hz
    
    JOINT_0_ANGLE_ADS_VALUE_MAP_PATH = 'data/angle_ads_value_map_joint_0.csv'

    def __init__(self):
        
        print('Initialize PWM board controller')
        # Initialise the PCA9685 using the default address (0x40).
        self.__pwm = Adafruit_PCA9685.PCA9685()

        print('Set frequency')
        # Set the frequency
        self.__pwm.set_pwm_freq(self.SERVO_MOTOR_FREQUENCY)

        self.__i2c = busio.I2C(board.SCL, board.SDA)
        self.__ads1 = ADS.ADS1115(self.__i2c)
        # self.__ads2 = ADS.ADS1115(i2c)
        
        self.__joints = []
        self.__joints.append(Servo(self.__pwm,0,self.PWM_BOARD_RESOLUTION,0,270,self.__ads1,0, pandas.read_csv(self.JOINT_0_ANGLE_ADS_VALUE_MAP_PATH)))
        # self.__joints.append(Servo(self.__pwm,1,self.PWM_BOARD_RESOLUTION,0,270,self.__ads1,1))
        # self.__joints.append(Servo(self.__pwm,2,self.PWM_BOARD_RESOLUTION,0,270,self.__ads1,2))
        # self.__joints.append(Servo(self.__pwm,3,self.PWM_BOARD_RESOLUTION,0,270,self.__ads1,3))
        # self.__joints.append(Servo(self.__pwm,4,self.PWM_BOARD_RESOLUTION,0,270,self.__ads2,0))
        # self.__joints.append(Servo(self.__pwm,5,self.PWM_BOARD_RESOLUTION,0,270,self.__ads2,1))

    def move(self):
        
        print('Move the servo')
        self.__joints[0].move(0)
        # self.__joints[1].move(0)
        time.sleep(3)
        
        self.__joints[0].move(180)
        # self.__joints[1].move(90)
        time.sleep(3)
        
        self.__joints[0].move(90)
        # self.__joints[1].move(270)
        time.sleep(3)
        
        self.__joints[0].move(120)
        # self.__joints[1].move(200)
        time.sleep(3)

