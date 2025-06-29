#!/bin/bash

## PARAMS
# $1 - The sequence number of the video
# $2 - The network delay in ms
# $3 - The packet loss in percentage points
# $4 - The source video filepath
# $5 - The distorted video output filepath


# Output the params that have been provided
echo "[EE_INFO] Sequence_number" "$1"
echo "[EE_INFO] Delay: " "$2"
echo "[EE_INFO] Packet Loss: " "$3"
echo "[EE_INFO] Source file: " "$4"
echo "[EE_INFO] Distorted file path: " "$5"

# Load the required kernel module and validate it has installed correctly
modprobe sch_netem
if [[ -z $(lsmod | grep sch_netem) ]]; then
  echo "[OS_ERROR] module sch_netem unable to be installed"
  exit 1
fi

# Apply the requested disruption to the loopback adapter and validate it has been applied
tc qdisc add dev lo root netem delay "$2"ms loss "$3"%
if [[ -z $(tc qdisc show dev lo | grep 'qdisc netem') ]]; then
  echo "[OS_ERROR] network conditions unable to be applied"
  exit 1
fi

# Delete the previously exported video if it already exists
if [[ -a $5 ]]; then
  rm "$5"
fi

# Generate sdp file for this experiment
ffmpeg -re -i "$4" -c:v copy -an -f rtp -sdp_file /tmp/experiment.sdp "rtp://127.0.0.1:1234" &

sdp_timeout=5

# Wait until the SDP file has been created then start the streaming
# If the sdp file is not created within 5 seconds the script will fail and terminate the test
while [[ -a /tmp/experiment.sdp ]]
do
  if [[ $sdp_sleeptime -ge $sdp_timeout ]]; then
    echo "[STREAMING_ERROR] sdp file not created before timeout"
    exit 1
  fi

  ((sdp_sleeptime++))
  sleep .1
done

# Start the recipient stream and save received video to file
ffmpeg -protocol_whitelist file,rtp,udp -i /tmp/experiment.sdp -strict 2 "$5"

# Stop the stream transmitting once the video has been received
kill %1

# Remove sdp file associated with the stream
rm /tmp/experiment.sdp

# Remove disruption from the adapter
tc qdisc del dev lo root