#!/usr/bin/env bash

# Create the directory for the experiment output
mkdir $1 && cd $_

# Introduce the network conditions
echo "Running experiment " $1 > ./result.txt
echo "Delay: " $2 >> ./result.txt
echo "Packet Loss: " $3 >> ./result.txt

# The actual command that would be executed
#tc qdisk add dev lo root netem delay $2 loss $3%