#!/bin/bash

## PARAMS
# $1 - The sequence number of the video
# $2 - The network delay in ms
# $3 - The packet loss in percentage points
# $4 - The source video filepath
# $5 - The distorted video output filepath


# Output the params that have been provided
printf "[EE_INFO] Sequence_number %s\n" "$1"
printf "[EE_INFO] Delay: %s\n" "$2"
printf "[EE_INFO] Packet Loss: %s\n" "$3"
printf "[EE_INFO] Source file: %s\n" "$4"
printf "[EE_INFO] Distorted file path: %s\n" "$5"


# Load the required kernel module and validate it has installed correctly
printf "[EE_INFO] Enabling sch_netem\n"
modprobe sch_netem
if [[ -z $(lsmod | grep sch_netem) ]]; then
  printf "[OS_ERROR] module sch_netem unable to be installed\n"
  exit 1
fi

# Apply the requested disruption to the loopback adapter and validate it has been applied
printf "[EE_INFO] Applying network conditions\n"
tc qdisc add dev lo root netem delay "$2"ms loss "$3"%
if [[ -z $(tc qdisc show dev lo | grep 'qdisc netem') ]]; then
  printf "[OS_ERROR] Network conditions unable to be applied\n"
  exit 1
fi

# Delete the previously exported video if it already exists
if [[ -a $5 ]]; then
  printf "[EE_INFO] Deleting previously exported file\n"
  rm "$5"
fi

# Generate sdp file for this experiment TODO: Find a cleaner way to do this
printf "[EE_INFO] Creating sdp file\n"
ffmpeg -re -i "$4" -c:v copy -an -f rtp -sdp_file /tmp/experiment.sdp "rtp://127.0.0.1:1234" -loglevel level+panic &
sleep 10
kill %1

# Start the usable stream
printf "[EE_INFO] Starting stream\n"
ffmpeg -re -i "$4" -c:v copy -an -f rtp -sdp_file /tmp/experiment.sdp "rtp://127.0.0.1:1234" &

# Start the recipient stream and save received video to file
ffmpeg -protocol_whitelist file,rtp,udp -i /tmp/experiment.sdp -strict 2 "$5"

# Stop the stream transmitting once the video has been received
kill %1

# Remove sdp file associated with the stream
rm /tmp/experiment.sdp

# Remove disruption from the adapter
tc qdisc del dev lo root