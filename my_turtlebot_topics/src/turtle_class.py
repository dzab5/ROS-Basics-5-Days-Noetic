#! /usr/bin/env python
import rospy
import time

from geometry_msgs import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

class TurtleClass(object):

    def __init__(self):
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.odom_sub = rospy.Subscriber('/odom',)
        self.las_sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.las_callback)
        self.cmd = Twist()
        self.laser = LaserScan()
        self.ctrl_c = False
        self.rate = rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuos publishing systems there is no big deal but in systems that publish only
        once it IS very important.
        """
        while not self.ctrl_c:
            connections = self.vel_pub.get_num_connections()
            if connections > 0:
                self.vel_pub.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        self.ctrl_c = True

    def las_callback(self):
        


if __name__ == '__main__':
  rospy.init_node('')
  TurtleClass()
  rospy.spin()