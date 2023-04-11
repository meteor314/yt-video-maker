# This script compiles videos of videos/current_date_folder into videos/compiled/current_date_folder

# Get current date
current_date=$(date +%Y-%m-%d)

# Get current date folder
current_date_folder="videos/$current_date"

# Get compiled date folder
compiled_date_folder="videos/compiled/$current_date"

# Create compiled date folder if it doesn't exist
mkdir -p $compiled_date_folder

# Merge each *.mp4 file with *.mp3 file with ffmpeg where the *.mp3 file has the same name as the *.mp4 file
for f in $current_date_folder/*.mp4; do
    filename=$(basename -- "$f")
    filename="${filename%.*}"
    ffmpeg -y -i $f -i $current_date_folder/$filename.mp3 -c:v copy -c:a aac -strict experimental $compiled_date_folder/$filename.mp4
done

# Create a list of video files in the compiled folder
ls -1 "$compiled_date_folder"/*.mp4 > "$compiled_date_folder.txt"

# Compile all *.mp4 files into one video using the concat demuxer
ffmpeg -f concat -safe 0 -i "$compiled_date_folder.txt" -c copy "$compiled_date_folder.mp4"
