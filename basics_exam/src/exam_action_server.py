#! /usr/bin/env python

import rospy
import actionlib

rospy.init_node('action_custom_msg_as')
actionobj = actionlib.SimpleActionServer("/rec_odom_as", record_odom, goal_callback)