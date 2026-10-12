from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)

program = hub_menu("1", "2", "3")

left_wheel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)

dist_sensor = UltrasonicSensor(Port.C)
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
    WHITE = 95
    BLACK = 15
    setpoint = (BLACK + WHITE) / 2
    k_p = 0.5
    k_d = 0.9

    previous_error = 0

    num_samples_for_line = 5
    line_detect = False
    samples = [setpoint] * num_samples_for_line

    while True:
        if line_detect:
            current_color = color_sensor.reflection()
            error = current_color - setpoint

            p_term = error * k_p
            
            derivative = previous_error - error
            previous_error = error
            d_term = derivative * k_d

            turn = p_term + d_term

            base.drive(50, turn_rate=turn)
            wait(10)
        else:
            base.straight(100, wait=False)
            for i in range(num_samples_for_line):
                samples[i] = color_sensor.reflection()
                wait(10)
            
            sample_avg = sum(samples) / num_samples_for_line
            if sample_avg > WHITE or sample_avg < BLACK:
                line_detect = True
                base.hold()