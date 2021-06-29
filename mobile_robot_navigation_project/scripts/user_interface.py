#! /usr/bin/env python

# import ros stuff
import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from actionlib_msgs.msg import GoalStatusArray
from geometry_msgs.msg import Twist
from time import sleep
from std_srvs.srv import *

target_position=[[-4,-3], [-4,2], [-4,7], [5,-7], [5,-3], [5,1]] #six possible target
target_flag=0 # flag to indicate when move_base reach target



def clbk_status(msg):
    global target_flag
    if(len(msg.status_list)>0):
    	if(msg.status_list[0].status ==3):
		target_flag=1
	elif(msg.status_list[0].status ==4):
		target_flag=2
    


def main():
    
    global target_flag
    rospy.init_node('user_interface')
    goal=rospy.Publisher('/move_base/goal',MoveBaseActionGoal, queue_size=1) #publish movebasegoal
    status=rospy.Subscriber('/move_base/status', GoalStatusArray, clbk_status, queue_size=1) #subscribe goalstatusarray
    vel=rospy.Publisher('/cmd_vel', Twist, queue_size=1) #publish for velocity
    
    	
    print("Hello")
    rate=rospy.Rate(20)
    while not rospy.is_shutdown():
    	print("You can choose one of the options: 1,2")
    	r=float(raw_input('request:  '))
	
	
	if(r==1):
		resp = srv_client_wall_follower(False)
		print("Please choose one target that is below")
		print("1: (-4,-3), 2: (-4,2), 3: (-4,7), 4: (5,-7), 5: (5,-3), 6: (5,1)")
		goaltarget=int(raw_input('target: '))
		print(" x position is: "+ str(target_position[goaltarget-1][0])+" y position is:"+ str(target_position[goaltarget-1][1]))
		MoveBase_msg=MoveBaseActionGoal()
		MoveBase_msg.goal.target_pose.header.frame_id= 'map'
		MoveBase_msg.goal.target_pose.pose.orientation.w = 1
		MoveBase_msg.goal.target_pose.pose.position.x = target_position[goaltarget-1][0]
		MoveBase_msg.goal.target_pose.pose.position.y = target_position[goaltarget-1][0]
		goal.publish(MoveBase_msg)
		print(" Reaching to target")
		sleep(8)
		target_flag=0
		while(target_flag==0):
			sleep(1)
		print("I have reached to target")
		if(target_flag==2):
			print("Unreachable target")
	
		
	if(r==2):
		
		resp=srv_client_wall_follower(False)
		twist_msg= Twist()
		twist_msg.linear.x=0
		twist_msg.angular.z=0
		pub.publish(twist_msg)
		print("Stopped !")
			
		
    	rate.sleep()


if __name__ == '__main__':
