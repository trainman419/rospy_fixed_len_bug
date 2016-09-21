#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from rospy_fixed_len_bug.msg import FixedArrayBug

rospy.init_node("pub")

pub = rospy.Publisher("fixed_array", FixedArrayBug, queue_size=10)

rate = rospy.Rate(1)

while True:
    good_msg = FixedArrayBug()
    good_msg.fixed_data = [Int32(i) for i in [0, 1, 2, 3]]
    pub.publish(good_msg)

    bad_msg = FixedArrayBug()
    bad_msg.fixed_data = []
    pub.publish(bad_msg)

    rate.sleep()
