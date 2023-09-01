#!/usr/bin/env
import rospy
from std_msgs.msg import String
from tutorials.msg import Position

def talk_to_me():
    pub = rospy.Publisher('talking_topic', Position, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher node started. Now publishing messages")
    while not rospy.is_shutdown():
        msg = Position()
        msg.x = "My position is: "
        msg.y = 2.0
        msg.z = 1.5
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass 
