import json
import subprocess
import os

ffmpeg_exe = r"C:\Users\neeri\Desktop\sumerizer\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

with open("snippets.json", "r", encoding="utf-8") as f:
    snippets = json.load(f)

clips = []

for i, s in enumerate(snippets, 1):
    start = s["start"]
    end = s["end"]
    out_file = f"snippet{i}.mp4"
    print(f"⏳ Cutting snippet {i}: {start} → {end} sec")
    
    # Use subprocess.run instead of os.system
    subprocess.run([
        ffmpeg_exe,
        "-i", "input_first10.mp4",
        "-ss", str(start),
        "-to", str(end),
        "-c", "copy",
        out_file
    ], check=True)
    
    clips.append(out_file)

# Create file list for merging
with open("mylist.txt", "w", encoding="utf-8") as f:
    for clip in clips:
        f.write(f"file '{clip}'\n")

# Merge snippets into teaser
subprocess.run([
    ffmpeg_exe,
    "-f", "concat",
    "-safe", "0",
    "-i", "mylist.txt",
    "-c", "copy",
    "teaser.mp4"
], check=True)

print("✅ teaser.mp4 created!")
