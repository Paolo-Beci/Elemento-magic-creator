#!/bin/sh

# Install python3 requirements
pip install --no-cache-dir -r requirements.txt
ls

# Run the main.py
python3 /middleware/src/main.py
