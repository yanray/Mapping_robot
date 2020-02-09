#!/usr/bin/env python

# Author: Yanrui Wang
# email: yw2226@cornell.edu
# copyright to Yanrui Wang

import rospy
from std_msgs.msg import String

def talker():
#	"chatter" topic, message type String (std_msgs.msg.String), queue_size is like a limit
    pub = rospy.Publisher('chatter', String, queue_size=10)

#	init a node name, anonymous adds a random number at the end of node NAME, make it unique. 
    rospy.init_node('talker', anonymous=True)

#	10 times-loop per second
    rate = rospy.Rate(10) # 10hz


    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 
