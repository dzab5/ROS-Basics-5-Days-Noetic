#! /usr/bin/env python
import rospy
import actionlib
import time

from actions_quiz.msg import CustomActionMsgFeedback, CustomActionMsgAction, CustomActionMsgActionResult
from std_msgs.msg import Empty

class QuizClass(object):
    
  # create messages that are used to publish feedback/result
  _feedback = CustomActionMsgFeedback()
  _result = CustomActionMsgActionResult()

  def __init__(self):
    # creates the action server
    self.quizobject = actionlib.SimpleActionServer("action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
    self.quizobject.start()
    
  def goal_callback(self, goal):
    r = rospy.Rate(1)
    success = True

    if goal.goal == 'TAKEOFF':
        self._feedback.feedback = "TAKEOFF"
        self.quizobject.publish_feedback(self._feedback)
        self.take_off()
        if self.quizobject.is_preempt_requested():
            rospy.loginfo('The goal has been cancelled/preempted')
            self.quizobject.set_preempted()
            success = False
    
    elif goal.goal == 'LAND':
        self._feedback.feedback = "LAND"
        self.quizobject.publish_feedback(self._feedback)
        self.land()
        if self.quizobject.is_preempt_requested():
            rospy.loginfo('The goal has been cancelled/preempted')
            self.quizobject.set_preempted()
            success = False
    
    else:
        self._feedback.feedback = "BAD INPUT"
        rospy.loginfo('Bad input')
    
    r.sleep()
    if success:
        self.quizobject.set_succeeded(self._result)
        rospy.loginfo('Succeeded')
       
  def take_off(self):
        pubis = rospy.Publisher('/drone/takeoff', Empty, queue_size = 1)
        mover = Empty()
        i=0
        while not i == 3:
            pubis.publish(mover)
            rospy.loginfo('Taking off...')
            time.sleep(1)
            i += 1

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
  rospy.init_node('action_custom_msg_as')
  QuizClass()
  rospy.spin()