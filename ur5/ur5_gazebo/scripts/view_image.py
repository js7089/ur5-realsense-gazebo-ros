#!/usr/bin/python3
#
# Send joint values to UR5 using messages
#

from std_msgs.msg import Header
import rospy
from sensor_msgs.msg import Image as ImageMsg
from gazebo_msgs.msg import LinkStates
import numpy as np
from PIL import ImageTk, Image
import tkinter as tk


# GUI
window = tk.Tk()
window.title("UR5 state viewer")
#window.geometry("350x300+100+100")
window.resizable(True, True)

var = tk.StringVar()
textbox1 = tk.Label(window, pady=5, textvariable=var)
textbox1.pack()
#imagebox1 = tk.Canvas(window, width=320, height=180)
imagebox1 = tk.Label(window)
imagebox1.pack()


np_arr_glb = np.zeros(1)
def save_image():
    np.savetxt("depth.csv", np_arr_glb*0.001, fmt='%.3f', delimiter=",")

button = tk.Button(window, text="Save", command=save_image)
button.pack()
window.wm_attributes("-topmost",1)

def callback(msg):
    # cube1::link ~ cube3::link
    # robot::wrist_3_link
    links = ["cube1::link", "cube2::link", "cube3::link",
            "robot::wrist_3_link"]
    
    res = ""

    for link_ in links:
        x = msg.name.index(link_)
        pos = msg.pose[x].position

        res += ("{} / x:{:.3f}, y:{:.3f}, z:{:.3f}\n".format(link_, pos.x, pos.y, pos.z))
        #var.set("{} / x:{:.3f}, y:{:.3f}, z:{:.3f}".format(link_, pos.x, pos.y, pos.z))

    var.set(res)


def callback_depth(msg):
    global np_arr_glb

    np_arr = np.frombuffer(msg.data, dtype=np.uint16).reshape(720,1280)
    np_arr_glb = np_arr.copy()

    min_val = np.min(np_arr)
    max_val = np.max(np_arr)

    np_arr = (np_arr - min_val) / (max_val - min_val) * 255

    
    im = Image.fromarray(np_arr[::2, ::2])
    imgtk = ImageTk.PhotoImage(image=im)
    imagebox1.configure(image=imgtk)
    imagebox1.image = imgtk


   
if __name__ == '__main__':
    rospy.init_node('joint_state_viewer')
    sub = rospy.Subscriber('/gazebo/link_states/',
                          LinkStates,
                          callback)
    sub_camera = rospy.Subscriber('/camera/depth/image_raw', ImageMsg, callback_depth)


    window.mainloop()

    try:
        while not rospy.is_shutdown():
            rospy.spin()

    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
