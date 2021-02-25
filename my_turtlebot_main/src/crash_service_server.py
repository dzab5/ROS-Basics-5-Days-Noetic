import rospy
from std_srvs.srv import Trigger, TriggerResponse
from laser_subscriber import LaserSub

class Crasher(object):
    def __init__(self):
        self.laserobject = LaserSub()
        self.my_service = rospy.Service('/crash_server', Trigger , self.my_callback)
        self.response = TriggerResponse()

    def my_callback(self, request):
        coll_dict = self.laserobject.collition_detection()

        collision_dir = ""
        if coll_dict['left']:
            collision_dir = "right"
        elif coll_dict['right']:
            collision_dir = "left"
        
        if collision_dir != "": #there is no collision
            self.response.success = True
            self.response.message = collision_dir
        else: 
            self.response.success = False
            self.response.message = "stop"
        return self.response

if __name__ == "__main__":
    rospy.init_node('crash_service_server')
    crashobj = Crasher()
    rospy.spin()