#!/bin/bash
# chmod +x main.sh to make runnable

# Set PYTHONPATH to include the project root
export PYTHONPATH=$(pwd)

# Generate the site
python3 src/main.py

# Serve the site
cd public && python3 -m http.server 8888

