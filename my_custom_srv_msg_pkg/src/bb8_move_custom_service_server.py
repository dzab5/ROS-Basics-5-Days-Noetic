#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    my_response = MyCustomServiceMessageResponse()
    i = request.duration
    while i > 0:
        move.linear.x = 0.4
        move.angular.z = 0.4
        pub.publish(move)
        rate.sleep()
        i-=1

    move.linear.x = 0.0
    move.angular.z = 0.0
    pub.publish(move)
    my_response.success = True
    return my_response.success

rospy.init_node('bb8_custom_circles') 

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move = Twist()
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) 
rospy.wait_for_service('/move_bb8_in_circle_custom')

rate = rospy.Rate(1)

rospy.spin()