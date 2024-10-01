import whisper

# Load the Whisper model
model = whisper.load_model("large")

file_path = "/home/tim/.sensitive_data/kosmos/snippets/KOSMOS004_EH_BAS_SNIPPET.mp4"

# Transcribe the audio directly from the video file
result = model.transcribe(file_path, language="sv")

# Print the transcription with timestamps
for segment in result["segments"]:
    start = segment["start"]
    end = segment["end"]
    text = segment["text"]
    print(f"[{start:.2f} - {end:.2f}] {text}")

# Save the transcription with timestamps to a file
with open("transcription_with_timestamps.txt", "w") as file:
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        file.write(f"[{start:.2f} - {end:.2f}] {text}\n")