#! /usr/bin/env python
import rospy

from sensor_msgs.msg import LaserScan

class LaserSub(object):

    def __init__(self):
        self.las_sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.las_callback)
        self.laserdata = LaserScan()
    
    def las_callback(self, msg):
        self.laserdata = msg
    
    def get_laser_data(self):
        return self.laserdata
    
    def collition_detection(self):
        coll_direction = ""

        if self.laserdata.ranges[360] > 1:
            pass
            #no collision
        if self.laserdata.ranges[719] < 1 and self.laserdata.ranges[360] < 1:
            coll_direction = "left"
            #collision to the left and in front
        if self.laserdata.ranges[0] < 1 and self.laserdata.ranges[360] < 1:
            coll_direction = "right"
            #collision to the right and in front

        coll_dir_dict = {
            "left": coll_direction == "left",
            "right": coll_direction == "right",
        }

        return coll_dir_dict

    '''def printf(self):
        print self.laserdata.ranges[360]'''

if __name__ == "__main__":
    rospy.init_node('laser_subscriber_node')
    laser_object = LaserSub()
    rate = rospy.Rate(0.5)
    ctrl_c = False
    def shutdownhook():
        # works better than the rospy.is_shut_down()
        global ctrl_c
        #print "shutdown time!"
        ctrl_c = True

    rospy.on_shutdown(shutdownhook)

    while not ctrl_c:
        data = laser_object.get_laser_data()
        rospy.loginfo(data)
        rate.sleep()