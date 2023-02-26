ur5-realsense-gazebo-ros
==

![alt gazebo-simul-main](https://github.com/js7089/ur5-realsense-gazebo-ros/blob/main/gazebo-simul-main.png)

ROS packages for integrating UR5 Robot, Robotiq gripper, and Realsense D435 camera on gazebo. The installation guide assumes **Ubuntu 20.04** with **ROS Noetic**.  

## Installation

  1. Install ROS packages *robot-state-publisher*, *controller-manager*.

    sudo apt-get install ros-$ROS_DISTRO-robot-state-publisher ros-$ROS_DISTRO-controller-manager 

  2. Install package [realsense-ros](https://github.com/IntelRealSense/realsense-ros/tree/ros1-legacy).

    sudo apt-get install ros-$ROS_DISTRO-realsense2-camera

  3. Move to your workspace and build packages.

    cd <your_catkin_workspace>
    catkin_make
    source devel/setup.bash


## Running Gazebo Simulation

> Launching the Simulation

* Launch Gazebo Simulation

    roslaunch ur5_gazebo ur5_cubes.launch

Once you succeed launching the Gazebo environment, you will see simulated UR5 robot with a simulated Realsense D435 camera on top. Since the environment is **paused** at all joint configurations set zero, you need to resume by pressing *Space*. The joint configuration will be set normally once you resume the simulator.

> Sending Joint Angle Command to UR5 Robot

  You can send joint angles manually with a GUI-supported node **send_joints_gui.py**.

  ![alt send-joints-gui](https://github.com/js7089/ur5-realsense-gazebo-ros/blob/main/send-joints-gui.png)

    rosrun ur5_gazebo send_joints_gui.py

> Retrieving Depth Images

  ![alt view-image](https://github.com/js7089/ur5-realsense-gazebo-ros/blob/main/view-image.png)
  
  Each pixel in depth image is encoded with 2 bytes. The node **view_image.py** helps visualize depth image with several ground truth data as references. Clicking the *Save* button at the buttom will capture and save the depth map to file *depth.csv*, where each numbers represent depth values in milimeters(mm). 

    rosrun ur5_gazebo view_image.py


