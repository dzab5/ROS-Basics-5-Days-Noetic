#! /usr/bin/env python
import rospy

from nav_msgs.msg import Odometry

class OdomSub(object):

    def __init__(self):
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.odomdata = Odometry()
    
    def odom_callback(self, msg):
        self.odomdata = msg
    
    def get_odomdata(self):
        return self.odomdata


if __name__ == "__main__":
    rospy.init_node('odom_subscriber_node')
    odom_object = OdomSub()
    rate = rospy.Rate(1)
    odom_object.printf()
    