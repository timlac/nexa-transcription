import json

# Load the JSON data from the file
with open('output.json', 'r') as file:
    data = json.load(file)

# Print the speaker and transcription
for segment in data["speakers"]:
    speaker = segment["speaker"]
    text = segment["text"]
    print(f"{speaker}: {text}")
