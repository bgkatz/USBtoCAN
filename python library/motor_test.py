'''
Motor Module example program.
Ben Katz
'''

import motormodule as mm
import time

mmc = mm.MotorModuleController('COM6')		# Connect to the controller's serial port
mmc.enable_motor(1)							# Enable motor with CAN ID 1
# Send a command:  
# (CAN ID, position setpoint, velocity setpoint, position gain, velocity gain, feed-forward torque)
# Units are:  Radians, Rad/s, N-m/rad, N-m/rad/s, N-m
mmc.send_command(1, 0, 0, 0, 0,  0)
time.sleep(.1)

# This example reads the start position of the motor
# Then sends position commands to ramp the motor position to zero 
# With a 1st-order response
# rx_values are ordered (CAN ID, Position, Velocity, Current)
start_position = mmc.rx_values[1]
print(start_position)
p_des = start_position[0]

while(p_des > .01):
	p_des = .99*p_des
	mmc.send_command(1, p_des , 0, 5, 0, 0)
	print(p_des)
	time.sleep(.02)

mmc.disable_motor(1) # Disable motor with CAN ID 1
	