#!/usr/bin/env bash


## PARAMS
# -n - Any params following this are related to network emulation
# $1 - The sequence number of the video
# $2 - The network delay in ms
# $3 - The packet loss in percentage points
# $4 - The source video filepath
# $5 - The distorted video output filepath

# Introduce the network conditions - substituted for echo commands for testing purposes
echo "Running experiment " $1 > result.txt
echo "Delay: " $2 >> result.txt
echo "Packet Loss: " $3 >> result.txt

# Apply the requested disruption to the loopback adapter
tc qdisk add dev lo root netem delay $2 loss $3%

# Start the stream through the network in the background
ffmpeg -i $4 -c:v copy -an -f rtp rtp://127.0.0.1:1234 &

# Start the recipient stream and save received video to file
ffmpeg -protocol_whitelist file,rtp,udp -i test-vid.sdp -strict 2 $5

# Remove disruption from the adapter
tc qdisc del dev lo root