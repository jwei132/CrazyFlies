import logging
import sys
import time
from threading import Event

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper


URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

DEFAULT_HEIGHT = 0.5
BOX_LIMIT = 0.5

def take_off_simple(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        time.sleep(3)
        mc.stop()

if __name__ == '__main__':

    cflib.crtp.init_drivers()
    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./.cache')) as scf:
        # Arm the Crazyflie
        print("Arming...")
        scf.cf.platform.send_arming_request(True)
        time.sleep(1.0)

        print("Begin Takeoff...")
        with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
            time.sleep(3)

            print("Hover....")
            mc.stop()
            time.sleep(3)
        # if not deck_attached_event.wait(timeout=5):
        #     print('No flow deck detected!')
        #     sys.exit(1)

        # take_off_simple(scf)