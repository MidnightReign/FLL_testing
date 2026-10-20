from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ColorLightMatrix,UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#define left and right motor variable
left_motor = Motor(Port.B,Direction.CLOCKWISE)
right_motor = Motor(Port.F,Direction.COUNTERCLOCKWISE)

#define the robot with wheel and axle track
robot= DriveBase (left_motor,right_motor,wheel_diameter=60,axle_track=133)
#robot.use_gyro(True)

#monkey.staight = (robot.straight)

#mission one

'''
robot.straight(670)
robot.turn(101)
robot.turn(-80)
robot.straight(-200)
robot.turn(120)
robot.straight(900)
''' 