import pandas as pd
import matplotlib.pyplot as plt
import json


# Function to collect AU 25 values within a time range
def collect_au25_values(start, end, face_df):
    mask = (face_df['timestamp'] >= start) & (face_df['timestamp'] <= end)
    return face_df.loc[mask, 'AU25_r'].tolist()


openface_path = "/home/tim/Work/dsy/data/behavioral_experiments/Deception_Pipeline_Data/openface_files/B623A.csv"

openface_df = pd.read_csv(openface_path)

transcription_path = "data.json"

with open(transcription_path) as f:
    transcription_data = json.load(f)

print(transcription_data["segments"][0])

trans_df = pd.DataFrame(transcription_data["segments"])

# Add AU 25 information to each transcription segment
trans_df['AU25'] = trans_df.apply(lambda row: collect_au25_values(row['start'], row['end'], openface_df), axis=1)

trans_df = trans_df.where(pd.notnull(trans_df), None)

# Convert back to dictionary format
transcription_with_au25 = trans_df.to_dict(orient='records')

with open('transcription_with_au25.json', 'w', encoding='utf-8') as f:
    json.dump(transcription_with_au25, f, indent=4, ensure_ascii=False)

with open('transcription_with_au25.json') as f:
    transcription_load = json.load(f)

print(transcription_load[0])
