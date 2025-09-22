import whisper
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Load tiny model for speed
model = whisper.load_model("tiny")

input_file = "input_first10.mp4"
output_file = "transcript_first10.txt"

print("⏳ Transcribing first 10 minutes...")
result = model.transcribe(input_file)

# Save transcript
with open(output_file, "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()
        f.write(f"[{start:.2f} - {end:.2f}] {text}\n")

print(f"✅ Transcription complete. Saved as {output_file}")
