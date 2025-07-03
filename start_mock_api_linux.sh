#! /bin/bash

# Open the root directory of the Experiment Engine
cd /root/ExperimentEngine-Group6/ || exit
source ./.venv/bin/activate

echo "Starting Mock APIs"

# Start each of the mock APIs and set them to background tasks
python ./src/_development/MockExperimentApi.py &
python ./src/_development/MockInfrastructureApi.py &
python ./src/_development/MockResultApi.py &
python ./src/_development/StaticMockData.py &
