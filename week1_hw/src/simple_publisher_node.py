#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def publisher():
    pub = rospy.Publisher("/Adeeb", Int32, queue_size=10)
    rospy.init_node("hw1_node", anonymous=True)
    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        student_id = 20180855
        pub.publish(student_id)
        rate.sleep()

if __name__ == "__main__":
    publisher()