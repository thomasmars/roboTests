#!/bin/sh
# Set up camera stream
# Set display and start cvlc
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin DAEMON_BIN=/usr/bin/vlc DISPLAY=:0 cvlc v4l2:///dev/video0:width=480:height=640 --sout '#transcode{vcodec=mp4v}:udp{mux=ts,dst=192.168.1.142:5004}' --ttl 12