from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)

program = hub_menu("1", "2", "3")

left_wheel = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.F)

# dist_sensor = UltrasonicSensor(Port.C)
color_sensor = ColorSensor(Port.D)

base = DriveBase(left_wheel, right_wheel, 57, 134.5)

if program == "1":
    # print(str(hub.battery.voltage()/1000), " Volts")
    
    base.use_gyro(True)

    base.straight(100, wait=False)

    while base.done() == False:
        if sensor.distance() < 100:
            base.stop()

    wait(1000)

    base.turn(-180)
    base.straight(100)

elif program == "2":
    while(True):
        # print(sensor.distance())
        print(color_sensor.hsv(), " ", color_sensor.reflection())
        wait(100)
    
elif program == "3":
    RED = [356, 93, 95]
    WHITE = [10, 0, 100]
    num_samples_WHITE = 5
    num_samples_RED = 5

    line_detect = False
    
    while True:
        #wait(10)

        if line_detect:
            base.straight(200)
        else:
            base.straight(1000, wait=False)
            
            color = color_sensor.hsv()

            if (color.h > RED[0]-10) and (color.s > RED[1]-10) and color.v > 92:
                base.hold()
                break

            