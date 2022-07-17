#!/usr/bin/env python3
"""
Scripts to drive a donkey 2 car

Usage:
    js_drive.py

Options:
    -h --help          Show this screen.
"""
import os
import time

from docopt import docopt
from PS4ControllerPart import PS4ControllerPart
from TankController import TankController
from TankControllerPart import TankControllerPart

import read_config as conf
from vehicle import Vehicle
from joystick_part import LogitechJoystickController
from arduino_part import ArduinoFirmata, PWMSteering, PWMThrottle


def drive():
    '''
    Construct a working robotic vehicle from many parts.
    Each part runs as a job in the Vehicle loop, calling either
    it's run or run_threaded method depending on the constructor flag `threaded`.
    All parts are updated one after another at the framerate given in
    cfg.DRIVE_LOOP_HZ assuming each part finishes processing in a timely manner.
    Parts may have named outputs and inputs. The framework handles passing named outputs
    to parts requesting the same named input.
    '''

    # Initialize car
    V = Vehicle()

    # Add PS4 Controller. Input throttle and steering.
    ps4Controller = PS4ControllerPart(interface="/dev/input/js0",connecting_using_ds4drv=False)
    V.add(
        ps4Controller,
        outputs=['user/throttle_pressed', 'user/reverse_pressed', 'user/steering_left', 'user/steering_right'],
        threaded=True)

    # Drive train setup
    tank_controller = TankController()
    tank_controller.setup()
    tankControllerPart = TankControllerPart(tank_controller)
    V.add(
        tankControllerPart,
        inputs=['user/throttle_pressed', 'user/reverse_pressed', 'user/steering_left', 'user/steering_right']
        )

    # run the vehicle
    V.start(rate_hz=cfg.DRIVE_LOOP_HZ,
            max_loop_count=cfg.MAX_LOOPS)


if __name__ == '__main__':
    args = docopt(__doc__)
    cfg = conf.load_config("config.py")

    drive()
