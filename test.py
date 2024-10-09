import whisper

model = whisper.load_model("small")

# load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("./audio/2681-1723340332.mp3")
# audio = whisper.pad_or_trim(audio)

result = model.transcribe("./audio/2681-1723340332.mp3")
print(result["text"])