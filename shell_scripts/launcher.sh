#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home
cd /
cd home/bananapi/pyProjects/bluetooth
sudo PYTHONPATH=/home/bananapi/pyProjects python bluetooth_multiple_connections.py
cd /