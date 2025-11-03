from scripts.adam import ADAM
import time
import pybullet as p
import pybullet_data
import scipy.io
import os
import math

if __name__ == '__main__':
    base_path = os.path.dirname(__file__)
    robot_urdf_path = os.path.join(base_path,"..","models","robot", "rb1_base_description", "robots", "robotDummy.urdf")
    
    adam = ADAM(robot_urdf_path, useRealTimeSimulation=True, used_fixed_base=False, use_ros=False)
    adam.wait(0.1)
    
    p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
    initial_right_pose = [2.7354,-1.5973,-1.1237,-1.2453,0.4834,-0.1599]
    initial_left_pose = [-2.0935,-2.0019,-0.8266,-2.6136,4.4560,5.1101]

    time_step = 1./240.
    p.setTimeStep(time_step) # Set the elapsed time per step

    while True:
        adam.teleop.teleoperate_base(debug=True)
        time.sleep(time_step)
    
    