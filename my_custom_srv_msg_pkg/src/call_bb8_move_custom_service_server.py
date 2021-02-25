#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('bb8_custom_circle') 
rospy.wait_for_service('/move_bb8_in_circle_custom')
circle_service = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)
circle_object = MyCustomServiceMessageRequest()
circle_object.duration = 10
# Send through the connection the name of the trajectory to be executed by the robot
result = circle_service(circle_object)
print result