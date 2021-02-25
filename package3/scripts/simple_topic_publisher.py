#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist)
rate = rospy.Rate(2)
count = Twist()
count.linear.x = 0.5
count.angular.z = 0.4

while count.linear.x != 0.7: 
  pub.publish(count)
  count.linear.x += 0.05
  count.angular.z += 0.05
  rate.sleep()