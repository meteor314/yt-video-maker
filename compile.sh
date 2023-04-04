#!/bin/bash

# This script compiles videos of videos/current_date_folder indo videos/compiled/current_date_folder

# Get current date
current_date=$(date +%Y-%m-%d)

# Get current date folder
current_date_folder="videos/$current_date"

# Get compiled date folder
compiled_date_folder="videos/compiled/$current_date"

# Create compiled date folder if it doesn't exist
mkdir -p $compiled_date_folder

# Compile all video from current_date_folder with ffmpeg in one single video file on compiled_date_folder with sound 
ffmpeg -f concat -safe 0 -i <(for f in $current_date_folder/*.mp4; do echo "file '$PWD/$f'"; done) -c:v copy -c:a aac $compiled_date_folder/compiled.mp4
