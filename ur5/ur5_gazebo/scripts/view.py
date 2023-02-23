#!/usr/bin/python3
#
# Send joint values to UR5 using messages
#

from std_msgs.msg import Header
import rospy
from gazebo_msgs.msg import LinkStates


def callback(msg):
    # cube1::link ~ cube3::link
    # robot::wrist_3_link
    links = ["cube1::link", "cube2::link", "cube3::link",
            "robot::wrist_3_link"]
        
    for link_ in links:
        x = msg.name.index(link_)
        pos = msg.pose[x].position
        print("{} / x:{:.3f}, y:{:.3f}, z:{:.3f}".format(link_, pos.x, pos.y, pos.z))


#    print(msg)
    
if __name__ == '__main__':
    rospy.init_node('joint_state_viewer')
    sub = rospy.Subscriber('/gazebo/link_states/',
                          LinkStates,
                          callback)

    try:
        while not rospy.is_shutdown():
            rospy.spin()

    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
