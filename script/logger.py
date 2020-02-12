#!/usr/bin/env python2
#coding=utf-8

from datetime import datetime
import os
import rospy
import tf
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

zed_log = None
lidar_log = None

def ts_to_s(ts):
    return ts.secs + ts.nsecs / 1000000000.0

def write_pose(file, stamp, pose):
    pos = pose.position
    quat = pose.orientation
    euler = tf.transformations.euler_from_quaternion((quat.x, quat.y, quat.z, quat.w))
    file.write("%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n" % (ts_to_s(stamp),
        pos.x, pos.y, pos.z,
        quat.x, quat.y, quat.z, quat.w,
        euler[0], euler[1], euler[2]))

def zed_callback(msg):
    write_pose(zed_log, msg.header.stamp, msg.pose)

def lidar_callback(msg):
    write_pose(lidar_log, msg.header.stamp, msg.pose.pose)

def get_log_filename(path, now, prefix):
    return os.path.join(path, prefix+'_'+now+'.csv')

def write_header(file):
    file.write('Time,X,Y,Z,Q.x,Q.y,Q.z,Q.w,Yaw,Pitch,Roll\n')

def open_logs():
    try:
        log_path = rospy.get_param('~log_path')
    except KeyError:
        rospy.logerr('Parameter ~log_path is not set')
        return None

    now = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    zed_path = get_log_filename(log_path, now, 'zed')
    lidar_path = get_log_filename(log_path, now, 'lidar')

    rospy.loginfo('ZED log file:   %s' % zed_path)
    rospy.loginfo('LiDAR log file: %s' % lidar_path)

    try:
        zed_log = open(zed_path, 'w')
        lidar_log = open(lidar_path, 'w')
        write_header(zed_log)
        write_header(lidar_log)
    except Exception as ex:
        rospy.logerr('Unable to open log file: %s' % ex)
        return None

    return zed_log, lidar_log

def main():
    global zed_log, lidar_log

    rospy.init_node('logger')
    rospy.loginfo('logger node started')

    files = open_logs()
    if not files:
        exit(-1)

    zed_log, lidar_log = files

    rospy.Subscriber('/zed/pose', PoseStamped, zed_callback)
    rospy.Subscriber('/integrated_to_init', Odometry, lidar_callback)

    rospy.spin()

if __name__ == '__main__':
    main()