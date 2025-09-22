import json

input_file = "transcript_first10.txt"
output_file = "snippets.json"

# Read transcript
segments = []
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        try:
            time_part, text = line.split("]", 1)
            start, end = map(float, time_part.strip("[ ]").split("-"))
            text = text.strip()
            segments.append({"start": start, "end": end, "text": text})
        except:
            continue

# Simple heuristic: pick longest segments first
segments.sort(key=lambda x: len(x["text"]), reverse=True)

# Select enough to make ~2-3 min teaser (~180 sec)
selected_segments = []
total_time = 0
for seg in segments:
    duration = seg["end"] - seg["start"]
    if total_time + duration > 180:  # max 3 min
        break
    selected_segments.append(seg)
    total_time += duration

# Save
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(selected_segments, f, indent=2)

print(f"✅ Snippets selected ({len(selected_segments)} segments, total {int(total_time)} sec)")
