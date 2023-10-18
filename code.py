
# These lines import necessary libraries to run this code
import time
import board
import digitalio
import pwmio

from adafruit_motor import motor # Imports function from adafruit_motor library

right_motor_forward = board.GP12 #initializes variable left_motor_forward and attaches to GP12
right_motor_backward = board.GP13 #initializes variable left_motor_backward and attaches to GP13
left_motor_forward = board.GP15
left_motor_backward = board.GP14

pwm_La = pwmio.PWMOut(right_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(right_motor_backward, frequency=10000)
pwm_Lc = pwmio.PWMOut(left_motor_forward, frequency=10000) #Tells controller thay motor is output
pwm_Ld = pwmio.PWMOut(left_motor_backward, frequency=10000) #Tells controller thay motor is output

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Connfiguration Line(it is required)
Left_Motor_speed = 255 #Initializes variable for the left_motor_speed and starts it
Left_Motor_speed = 255 #Initializes variable for the left_motor_speed and starts it
Right_Motor = motor.DCMotor(pwm_Lc, pwm_Ld)
Right_Motor_speed = 255



while True:
    def forward():
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)

    def backward():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)

    def left():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)

    def right():
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
