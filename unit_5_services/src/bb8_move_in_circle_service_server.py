#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

def my_callback(request):
    move.linear.x = 0.4
    move.angular.z = 0.4
    pub.publish(move)
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 


rospy.init_node('bb8_circle') 
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move = Twist()
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called my_service with the defined callback

rospy.spin() # maintain the service open.