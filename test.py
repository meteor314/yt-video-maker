import subprocess

# list all the mp4 files in the folder
input_files = r'/mnt/c/Users/admin/Dev/reddit/videos/compiled/2023-04-04/*.mp4'

# specify the output file name and format
output_file = r'/mnt/c/Users/admin/Dev/reddit/videos/compiled/2023-04-04/output.mp4'

# run FFmpeg command to concatenate the input files
subprocess.call(['ffmpeg', '-i', 'concat:' +
                input_files, '-c', 'copy', output_file])
