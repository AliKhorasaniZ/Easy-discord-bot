#!/bin/bash

cd ..

# Set up virtual environment
python -m venv bot-env
source "bot-env/Scripts/activate"

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Install Moving the executables to the Scripts folder
cp "ffmpeg\ffmpeg.exe" "bot-env\Scripts"
cp "ffmpeg\ffplay.exe" "bot-env\Scripts"
cp "ffmpeg\ffprobe.exe" "bot-env\Scripts"

# Deactivate virtual environment
source "bot-env\Scripts\deactivate"

# Echo setup completion message
echo "Setup completed."