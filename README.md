# zed-lidar-logger
One more ROS logger: log position from ZED-camera and loam-velodyne SLAM to the CSV

# Prerequirements
 - [zed-ros-wrapper](https://github.com/stereolabs/zed-ros-wrapper)
 - [velodyne](https://github.com/ros-drivers/velodyne)
 - [loam_velodyne](https://github.com/laboshinl/loam_velodyne)
 
 # Run
 Run from real devices:
 ```bash
 roslaunch velodyne_slam_logger log.launch log_path:=<full path to directory with logs> 
 ```
 
 Run from bag:
 ```bash
 roslaunch velodyne_slam_logger log.launch bag:=<full path to bag-file> log_path:=<full path to directory with logs> 
 ```
