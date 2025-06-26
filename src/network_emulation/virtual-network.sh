#!/bin/bash


## PARAMS
# $1 - The sequence number of the video
# $2 - The network delay in ms
# $3 - The packet loss in percentage points
# $4 - The source video filepath
# $5 - The distorted video output filepath

# Introduce the network conditions - substituted for echo commands for testing purposes
echo "Running experiment " $1 > result.txt
echo "Delay: " $2 >> result.txt
echo "Packet Loss: " $3 >> result.txt

# Ensure the netem kernel module is installed
modprobe sch_netem
lsmod | grep sch_netem

# Generate sdp file for this experiment
ffmpeg -sdp_file /tmp/experiment.sdp

# Apply the requested disruption to the loopback adapter
tc qdisc add dev lo root netem delay $2 loss $3

# Start the stream through the network in the background
ffmpeg -re -i $4 -c:v copy -an -f rtp -sdp_file /tmp/experiment.sdp "rtp://127.0.0.1:1234" &

# Start the recipient stream and save received video to file
ffmpeg -protocol_whitelist file,rtp,udp -i /tmp/experiment.sdp -strict 2 $5

# Stop the stream transmitting once the video has been received
kill %1

# Remove sdp file associated with the stream
rm /tmp/experiment.sdp

# Remove disruption from the adapter
tc qdisc del dev lo root