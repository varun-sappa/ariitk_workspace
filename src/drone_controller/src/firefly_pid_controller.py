#!/usr/bin/env python3


# import rospy
# from mav_msgs.msg import Actuators

# def firefly_goto_point():
#     rospy.init_node('drone_controller', anonymous=True)
#     rate = rospy.Rate(10)  # 10 Hz

#     # Publisher for motor speeds
#     motor_pub = rospy.Publisher('/firefly/command/motor_speed', Actuators, queue_size=10)

#     # Wait for the publisher to connect
#     rospy.sleep(1)

#     # Set desired motor speeds
#     motor_speeds = Actuators()
#     motor_speeds.angular_velocities = [0.0] * 6  # Initialize all speeds to 0

#     # Set desired speed for each motor (change as per your requirements)
#     motor_speeds.angular_velocities[0] = 1000.0  # Motor 1
#     motor_speeds.angular_velocities[1] = 1000.0  # Motor 2
#     motor_speeds.angular_velocities[2] = 1000.0  # Motor 3
#     motor_speeds.angular_velocities[3] = 1000.0  # Motor 4
#     motor_speeds.angular_velocities[4] = 1000.0  # Motor 5
#     motor_speeds.angular_velocities[5] = 1000.0  # Motor 6

#     # Publish motor speeds repeatedly until the node is stopped
#     while not rospy.is_shutdown():
#         motor_pub.publish(motor_speeds)
#         rate.sleep()

# if __name__ == '__main__':
#     try:
#         firefly_goto_point()
#     except rospy.ROSInterruptException:
#         pass


import rospy
from geometry_msgs.msg import PoseStamped
from mav_msgs.msg import Actuators

class FireflyController:
    def __init__(self):
        rospy.init_node('firefly_controller')

        # Desired waypoint
        self.waypoint = PoseStamped()

        # Subscribers
        rospy.Subscriber('/firefly/pose', PoseStamped, self.waypoint_callback)

        # Publishers
        self.actuators_pub = rospy.Publisher('/firefly/command/motor_speed', Actuators, queue_size=1)

    def waypoint_callback(self, msg):
        self.waypoint = msg

    def run(self):
        rate = rospy.Rate(10)  # 10 Hz

        while not rospy.is_shutdown():
            # Calculate desired XYZ error
            error_x = self.waypoint.pose.position.x
            error_y = self.waypoint.pose.position.y
            error_z = self.waypoint.pose.position.z

            # PID gains
            kp = 1.0
            ki = 0.0
            kd = 0.0

            # PID control to calculate required motor speeds
            motor_speeds = Actuators()
            motor_speeds.angular_velocities = [kp * error_x, kp * error_y, kp * error_z,
                                                0.0, 0.0, 0.0]  # Setting last three motor speeds to 0

            # Publish motor speeds
            self.actuators_pub.publish(motor_speeds)

            rate.sleep()

if __name__ == '__main__':
    try:
        controller = FireflyController()

        # Example: Publishing a desired waypoint
        desired_waypoint = PoseStamped()
        desired_waypoint.pose.position.x = 2.0  # Desired X coordinate
        desired_waypoint.pose.position.y = 3.0  # Desired Y coordinate
        desired_waypoint.pose.position.z = 1.5  # Desired Z coordinate

        # Publish the desired waypoint
        controller.waypoint_callback(desired_waypoint)

        controller.run()
    except rospy.ROSInterruptException:
        pass

