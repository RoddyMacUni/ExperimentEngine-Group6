#!/usr/bin/env bash


## PARAMS
# $1 - Experiment id
# $2 - The required delay in ms
# $3 - The required packet loss in percentage points
# $4 - The input video name
# Any params after this last param is to be used to pass the metric collection configuration to the driver script

# Create the directory for the experiment output
mkdir $1 && cd $_

# Introduce the network conditions - substituted for echo commands for testing purposes
echo "Running experiment " $1 > result.txt
echo "Delay: " $2 >> result.txt
echo "Packet Loss: " $3 >> result.txt

# Apply the requested disruption to the loopback adapter
tc qdisk add dev lo root netem delay $2 loss $3%

# Start the stream through the network in the background
ffmpeg -i $4 -c:v copy -an -f rtp rtp://127.0.0.1:1234 &

# Start the recipient stream and save received video to file
ffmpeg -protocol_whitelist file,rtp,udp -i test-vid.sdp -strict 2 disrupted-vid.mp4

# Remove disruption from the adapter
tc qdisc del dev lo root