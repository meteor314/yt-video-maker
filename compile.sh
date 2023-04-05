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


# merge each *.mp4 file with *.mp3 file with ffmpeg where the *.mp3 file has the same name as the *.mp4 file
#for f in $current_date_folder/*.mp4; do
#    filename=$(basename -- "$f")
#    filename="${filename%.*}"
#    ffmpeg -y -i $f -i $current_date_folder/$filename.mp3 -c:v copy -c:a aac -strict experimental $compiled_date_folder/$filename.mp4
#done

# Compile all *.mp4 files into one video
for f in $current_date_folder/*.mp4; do
  if ffmpeg -i "$f" 2>&1 | grep -q "Non-monotonous DTS in output stream"; then
    echo "Skipping $f due to warning"
  else
    echo "Processing $f"
    ffmpeg -itsoffset 2 -i "$f" -c copy -map 0:v:0 -map 0:a:0 -r 24 -vsync 0 -flags +global_header -movflags faststart -avoid_negative_ts make_zero -fflags +genpts -y "$compiled_date_folder/$(basename "$f")"
  fi
done
