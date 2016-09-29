#!/bin/sh
# Set up camera stream
# Set display and start cvlc
DISPLAY=:0 cvlc -v v4l2:///dev/video0:width=480:height=640 --sout '#transcode{vcodec=mp4v,vb=800,acodec=none}:udp{mux=ts,dst=192.168.1.142:5004}' --ttl 12