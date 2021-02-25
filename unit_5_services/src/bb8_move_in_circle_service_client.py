#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest
import sys

rospy.init_node('bb8_circles') 
rospy.wait_for_service('/move_bb8_in_circle')
circle_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
circle_object = EmptyRequest()

# Send through the connection the name of the trajectory to be executed by the robot
result = circle_service(circle_object)
print result