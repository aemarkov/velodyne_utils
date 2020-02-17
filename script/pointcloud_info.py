#!/usr/bin/env python2
#coding=utf-8

# Get the list of the channels in the PointCloud2
# I don't know how to easely get this information with a standard utilities, so I create own one

from datetime import datetime
import os
import rospy
import tf
from sensor_msgs.msg import PointCloud2
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Display information about PointCloud2")
    parser.add_argument('topic', type=str, help='Topic name')
    return parser

def cloud_callback(msg):
    print('width:      %d' % msg.width)
    print('height:     %d' % msg.height)
    print('num points: %d' % (msg.width * msg.height))
    print('Channels in:')
    for field in msg.fields:
        print(field.name)
    rospy.signal_shutdown(None)

def main():
    parser = create_parser()
    args = parser.parse_args()

    rospy.init_node('pointcloud_info')
    rospy.Subscriber(args.topic, PointCloud2, cloud_callback)
    rospy.spin()

if __name__ == '__main__':
    main()