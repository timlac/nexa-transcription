import whisperx
import gc
from dotenv import load_dotenv
import os
import torch

load_dotenv()

YOUR_HF_TOKEN = os.getenv('MY_HF_TOKEN')

device = "cuda"
audio_file = "/home/tim/Work/dsy/data/behavioral_experiments/Deception_Pipeline_Data/Face-to-Face/Dyad 2/B623A/B623A.mp4"
batch_size = 8 # reduce if low on GPU mem
compute_type = "float16" # change to "int8" if low on GPU mem (may reduce accuracy)

# 1. Transcribe with original whisper (batched)
model = whisperx.load_model("large-v2", device, compute_type=compute_type)
print("model loaded")

# save model to local path (optional)
# model_dir = "/path/"
# model = whisperx.load_model("large-v2", device, compute_type=compute_type, download_root=model_dir)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print(result["segments"]) # before alignment

# delete model if low on GPU resources
import gc; gc.collect(); torch.cuda.empty_cache(); del model

# 2. Align whisper output
align_model_name = "KBLab/wav2vec2-large-voxrex-swedish"
model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device, model_name=align_model_name)
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

print(result["segments"]) # after alignment

# delete model if low on GPU resources
import gc; gc.collect(); torch.cuda.empty_cache(); del model_a

# 3. Assign speaker labels
diarize_model = whisperx.DiarizationPipeline(use_auth_token=YOUR_HF_TOKEN, device=device)

# add min/max number of speakers if known
diarize_segments = diarize_model(audio)
# diarize_model(audio, min_speakers=min_speakers, max_speakers=max_speakers)

result = whisperx.assign_word_speakers(diarize_segments, result)
print(diarize_segments)
print(result["segments"]) # segments are now assigned speaker IDs