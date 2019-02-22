#project1: microbit pendulum by Mo and Alyssa

print("Part I: Simulation")

import numpy as np
import math

def update_pendulum(ang_pos, ang_vel, ang_acc, time1, time2):
    dt = time2-time1
    ang_vel_new = ang_vel+ang_acc*dt
    ang_pos_new = ang_pos+ang_vel*dt
    ang_acc_new = 9.8*(math.pi/2-ang_pos_new)
    return ang_pos_new, ang_vel_new, ang_acc_new

def print_pendulum(time, ang_pos, ang_vel, ang_acc):
    print("TIME:     ", time)
    print("ANGULAR POSITION: ", ang_pos)
    print("ANGULAR VELOCITY: ", ang_vel)
    print("ANGULAR ACCELERATION: ", ang_acc, "\n")

ang_pos = [0]
ang_vel = [0]
ang_acc = 9.8*(math.pi/2-ang_pos[0])
time = np.linspace(0,20,201)
print_pendulum(time[0], ang_pos[0], ang_vel[0], ang_acc)

i = 1
while i < len(time):
    ang_pos_new, ang_vel_new, ang_acc_new = update_pendulum(ang_pos[i-1], ang_vel[i-1], ang_acc, time[i-1], time[i])
    ang_pos.append(ang_pos_new)
    ang_vel.append(ang_vel_new)
    print_pendulum(time[i],ang_pos[i],ang_vel[i], ang_acc)
    i += 1