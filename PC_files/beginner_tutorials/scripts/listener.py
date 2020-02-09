#!/usr/bin/env python
# Software License Agreement (BSD License)


import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

    if(data.data == 'w'):
        rospy.loginfo('Received w')
    elif(data.data == 's'):
        rospy.loginfo('Received s')
    elif(data.data == 'a'):
        rospy.loginfo('Received a')
    elif(data.data == 'd'):
        rospy.loginfo('Received d')


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
