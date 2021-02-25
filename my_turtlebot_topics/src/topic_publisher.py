#! /usr/bin/env python
import rospy

from laser_subscriber import LaserSub
from odom_subscriber import OdomSub
from geometry_msgs.msg import Twist

class CMDPub(object):

    def __init__(self):
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.linearspeed = 0.5
        self.angularspeed = 0.5

    def shutdownhook(self):
        self.ctrl_c = True

    def move_robot(self, direction):
        if direction == "forwards":
            self.cmd.linear.x = self.linearspeed
            self.cmd.angular.z = 0.0
        elif direction == "right":
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = self.angularspeed
        elif direction == "left":
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = -self.angularspeed
        elif direction == "backwards":
            self.cmd.linear.x = -self.linearspeed
            self.cmd.angular.z = 0.0
        elif direction == "stop":
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 0.0
        else:
            print "Invalid move rec_ in cmd_topic_pub"

        self.vel_pub.publish(self.cmd)


if __name__ == "__main__":
    rospy.init_node('cmd_vel_publisher_node')
    cmd_publisher_object = CMDPub()
    laserobj = LaserSub()
    odomobj = OdomSub()
    rate = rospy.Rate(1)
    while not cmd_publisher_object.ctrl_c:
        #cmd_publisher_object.move_robot(direction="forwards")
        #odomobj.printf()
        #print laserobj.laserdata.ranges[360]
        rate.sleep()
    