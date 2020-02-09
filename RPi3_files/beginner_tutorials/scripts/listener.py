#!/usr/bin/env python

# Author: Yanrui Wang
# email: yw2226@cornell.edu
# copyright to Yanrui Wang

import rospy
from std_msgs.msg import String
import serial
import time  

ser=serial.Serial(port='/dev/ttyUSB1',baudrate=115200)
ser.write('\x80')
ser.write('\x83')

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    # ser.write('\x89\xFF\x38\x01\xF4')  

    if(data.data == 'w'):
        rospy.loginfo('Received w')
        ser.write('\x92\x00\x4F\x00\x4F')
        # ser.write('\x92\x00\x6F\x00\x6F')  
        # time.sleep(0.5)
        # ser.write('\x92\x00\x00\x00\x00')  
    elif(data.data == 'a'):
        rospy.loginfo('Received a')
        ser.write('\x92\x00\x3F\x00\x1F')
        # ser.write('\x92\x00\x6F\x00\x00')  
        # time.sleep(0.5)
        # ser.write('\x92\x00\x00\x00\x00')  
    elif(data.data == 's'):
        rospy.loginfo('Received s')
        ser.write('\x92\x00\x00\x00\x00')
    elif(data.data == 'd'):
        rospy.loginfo('Received d')
        ser.write('\x92\x00\x1F\x00\x3F')
        # ser.write('\x92\x00\x00\x00\x6F')  
        # time.sleep(0.5)
        # ser.write('\x92\x00\x00\x00\x00') 
    elif(data.data == 'x'):
        rospy.loginfo('Received x')
        ser.write('\x92\xFF\xC1\xFF\xC1')


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
