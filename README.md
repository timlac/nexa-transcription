# nexa-transcription

The task of transcription is to convert speech to text. Most libraries also provide time stamps for word and utterances 
which is useful in the context of audio segmentation. Optimally we would also like to segment audio according to speaker. 
Thus, this repository also concerns method for audio segmentation and speaker diarization.

## Models 

### Transcription

[Whisper](https://github.com/openai/whisper) is a renowned model for transcription, however, large models can be slow to run. 
[Insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper) is a model which is optimized for faster performance, 
works good when tested in the repository. 

### Speaker diarization

[pyannote/speaker-diarization](https://huggingface.co/pyannote/speaker-diarization) is easy to use with above package, 
but the segmentation is quite poor. 

In FaceReader documentation, they classify talking using the following heuristic — _Talking is classified by looking at the rate of Action Unit 25
(parting lips) over a typical frequency (e.g. two words per second)._ Some experiments have been performed on this in script:
`openface_analysis.py`