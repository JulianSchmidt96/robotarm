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
from robotArm import RobotArm



def calibrate_servos():
    
    PWM_BOARD_RESOLUTION = 4096 # PWM control board resolution
    SERVO_MOTOR_FREQUENCY = 50 #In Hz
    JOINT_0_ANGLE_ADS_VALUE_MAP_PATH = 'data/angle_ads_value_map_joint_0.csv'

    print('Initialize PWM board controller')
    # Initialise the PCA9685 using the default address (0x40).
    pwm = Adafruit_PCA9685.PCA9685()

    print('Set frequency')
    # Set the frequency
    pwm.set_pwm_freq(SERVO_MOTOR_FREQUENCY)

    i2c = busio.I2C(board.SCL, board.SDA)
    ads1 = ADS.ADS1115(i2c)

    servo0 = Servo(pwm,0,PWM_BOARD_RESOLUTION,0,270,ads1,0, None)

    servo0.calibrate(JOINT_0_ANGLE_ADS_VALUE_MAP_PATH)

if __name__ == "__main__":
    
    # robot_arm = RobotArm()
    # robot_arm.move()

    calibrate_servos()