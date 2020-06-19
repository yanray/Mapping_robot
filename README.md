# Mapping_robot
 A robot to do mapping in an environment. 

## Preview 

Install ROS (Robert Operating System) on both Raspberry Pi 3b+ and PC (laptop) of ubuntu 16.04. 

Follow the *reference of Yanrui Wang.pdf* step by step. 

## Usage

### On PC (laptop) 

Download files in ***PC_files*** and put them in your *src* folder. 

### On Raspberry Pi 3b+

Download files in ***RPi3_files*** and put them in your *src* folder. 

### laser cutting

Download files in ***laser_cut*** and build your robot to test. 

**Laser Cutting Size:** (in Width)

1. 1_bottom_layer: 291mm
2. 2_middle_layer: 291mm
3. 3_top_layer:    291mm 
4. 4_battery_layer: top one (94mm), bottom left (56mm), bottom right (56mm)


### package for ssh service 

sudo apt-get purge openssh-server
sudo apt-get install openssh-server

