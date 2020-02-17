# velodyne_utils
Set of utils and experiments for the Velodyne LiDAR

## Prerequirements
 - [zed-ros-wrapper](https://github.com/stereolabs/zed-ros-wrapper)
 - [velodyne](https://github.com/ros-drivers/velodyne) or [my velodyne fork](https://github.com/Garrus007/velodyne)
 - [loam_velodyne](https://github.com/laboshinl/loam_velodyne)

## logger
One more ROS logger: log position from ZED-camera and loam-velodyne SLAM to the CSV

### Usage
Run from real devices:
```bash
roslaunch velodyne_utils log.launch log_path:=<full path to directory with logs>
```

Run from bag:
```bash
roslaunch velodyne_slam_logger log.launch bag:=<full path to bag-file> log_path:=<full path to directory with logs>
```

## pointcloud_info
Display some information about the pointcloud

### Usage
```
rosrun velodyne_utils pointcloud_info.py <topic name>
```
