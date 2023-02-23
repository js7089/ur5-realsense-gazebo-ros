#!/usr/bin/python3
#
# Send joint values to UR5 using messages
#

from trajectory_msgs.msg import JointTrajectory
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectoryPoint
import rospy
import tkinter as tk

def send_trajectory():
    x = textbox.get("1.0", 'end')    
    x_split = x.split(",")

    for y in range(len(x_split)):
        x_split[y] = float(x_split[y])

    # Create the topic message
    traj = JointTrajectory()
    traj.header = Header()
    # Joint names for UR5
    traj.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint',
                         'elbow_joint', 'wrist_1_joint', 'wrist_2_joint',
                         'wrist_3_joint']

    traj.header.stamp = rospy.Time.now()
    pts = JointTrajectoryPoint()
    pts.positions = x_split
    pts.time_from_start = rospy.Duration(1.0)

    # Set the points to the trajectory
    traj.points = []
    traj.points.append(pts)
    # Publish the message
    pub.publish(traj)

window = tk.Tk()
window.title("Joint Angle Command")
label = tk.Label(window, pady=6, text="Joint Angles (split by commas)")
textbox = tk.Text(window, height=1, width=50)
button = tk.Button(window, text="Send", command=send_trajectory)
label.pack()
textbox.pack()
button.pack()
window.wm_attributes("-topmost",1)

if __name__ == '__main__':
    rospy.init_node('send_joints_gui')
    pub = rospy.Publisher('/trajectory_controller/command',
                          JointTrajectory,
                          queue_size=10)


    window.mainloop()
    rate = rospy.Rate(10)
 
    try:
        while not rospy.is_shutdown():
            rospy.spin()

    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
