#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan

def callback(msg):
    #print msg.ranges[360]

    if msg.ranges[360] > 1:
        move.linear.x = 0.3
        move.angular.z = 0.0

    if msg.ranges[360] < 1:
        move.linear.x = 0.0
        move.angular.z = 0.3

    if msg.ranges[0] < 1:
        move.linear.x = 0.0
        move.angular.z = 0.2

    if msg.ranges[719] < 1:
        move.linear.x = 0
        move.angular.z = -0.2

    pub.publish(move)

if __name__ == "__main__":
    rospy.init_node('topics_quiz_node')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 2)
    move = Twist()
    sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
    #rate = rospy.Rate(2)

    #while not rospy.is_shutdown():
        #pub.publish(move)
        #rate.sleep()
    rospy.spin()