#! /usr/bin/env python
import rospy
import time
import actionlib

from actionlib.msg import TestFeedback, TestResult, TestAction
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class SquareClass(object):
    
  # create messages that are used to publish feedback/result
  fidback = TestFeedback()
  risult   = TestResult()

  def __init__(self):
    # creates the action server
    self.squareobj = actionlib.SimpleActionServer("square", TestAction, self.goal_callback, False)
    self.squareobj.start()
    
  def goal_callback(self, goal):
        # this callback is called when the action server is called.
        # this is the function that computes the Fibonacci sequence
        # and returns the sequence to the node that called the action server
        
        # helper variables
        r = rospy.Rate(1)
        success = True
        
        side_time = goal.goal
        self.up()

        for i in range(0, side_time):   
            self.move_square()
            rospy.sleep(1)
            self.fidback.feedback = i
            self.squareobj.publish_feedback(self.fidback)
        self.land()
        
        if self.squareobj.is_preempt_requested():
            rospy.loginfo('The goal has been cancelled/preempted')
            # the following line, sets the client in preempted state (goal cancelled)
            self.squareobj.set_preempted()
            success = False
            # we end the calculation of the Fibonacci sequence
            #break
        r.sleep()
        # at this point, either the goal has been achieved (success==true)
        # or the client preempted the goal (success==false)
        # If success, then we publish the final result
        # If not success, we do not publish anything in the result
        if success:
            self.risult.result = 1
            rospy.loginfo('Succeeded')
            self.squareobj.set_succeeded(self.risult)

  def up(self):
        pubis = rospy.Publisher('/drone/takeoff', Empty, queue_size = 1)
        mover = Empty()
        i=0
        while not i == 3:
            pubis.publish(mover)
            rospy.loginfo('Taking off...')
            time.sleep(1)
            i += 1
  def move_square(self):
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
        move = Twist()
        move.linear.x = 1
        move.angular.z = 1
        pub.publish(move)
  def land(self):
        pubises = rospy.Publisher('/drone/land', Empty, queue_size = 1)
        moverer = Empty()
        i=0
        while not i == 3:
            pubises.publish(moverer)
            rospy.loginfo('Landing...')
            time.sleep(1)
            i += 1

if __name__ == '__main__':
  rospy.init_node('squares')
  SquareClass()
  rospy.spin()