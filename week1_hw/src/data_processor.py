#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


class rosSubscriber():
    def __init__(self):
        rospy.init_node("Hw2Node", anonymous=True)
        self.sub = rospy.Subscriber("/Adeeb", Int32, self.callback)
        self.pub = rospy.Publisher("/Processed_Adeeb", Int32, queue_size=10)
        self.rate = rospy.Rate(30)

    def callback(self, msg):
        self.pub.publish(msg.data)



def main():
    pub_sub_node = rosSubscriber()

    while not rospy.is_shutdown():
        pub_sub_node.rate.sleep()

if __name__ == "__main__":
    main()
