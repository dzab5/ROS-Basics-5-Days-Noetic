#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def service_callback(request):
    my_response = TriggerResponse()

    if pubis == "front":
        my_response.message = "front"
    if pubis == "left":
        my_response.message = "left"
    if pubis == "right":
        my_response.message = "right"
    
    return my_response
    
    

def move():
    if pubis == "front":
        move_straight()
    if pubis == "left":
        move_rotate_left()
    if pubis == "right":
        move_rotate_right
  

def move_straight():
    move.linear.x = 0.3
    move.linear.z = 0
    pub.publish(move)

def move_rotate_left():
    move.linear.x = 0
    move.angular.z = 0.3
    pub.publish(move)

def move_rotate_right():
    move.linear.x = 0
    move.linear.z = -0.3
    pub.publish(move)

def stop():
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)


def laser_callback(msg):
    orientation = ""
    if msg.ranges[240:480] > 1: #no collision
        orientation = "front"
    if msg.ranges[480:] < 1 and msg.ranges[240:480] < 1:
        #collision left and in front
        orientation = "right"
    if msg.ranges[:240] < 1 and ranges[240:480] < 1:
        #collision right and in front
        orientation = "left"
    return orientation
    

rospy.init_node('service_node_exam') 

pub = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=1)
move = Twist()
pubis = rospy.Subscriber('/camera/scan', LaserScan, laser_callback)

my_service = rospy.Service('/crash_direction_service', Trigger , service_callback) 
rospy.wait_for_service('/crash_direction_service')

rospy.spin()