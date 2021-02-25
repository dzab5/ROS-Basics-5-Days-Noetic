#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('bb8_squares') 
rospy.wait_for_service('/move_bb8_in_square_custom')
square_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
square_object = BB8CustomServiceMessageRequest()
square_object.side = 2
square_object.repetitions = 1
# Send through the connection the name of the trajectory to be executed by the robot
result = square_service(square_object)

square_object2 = BB8CustomServiceMessageRequest()
square_object2.side = 4
square_object2.repetitions = 0

result2 = square_service(square_object2)