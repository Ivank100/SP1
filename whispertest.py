import whisper

def main():
    # use a tiny model just to confirm it works & is fast
    print("Loading model...")
    model = whisper.load_model("tiny")
    print("Model loaded.")

    # point this to any short audio: wav, mp3, m4a, etc.
    audio_path = "testing.mp3"

    print(f"Transcribing {audio_path} ...")
    result = model.transcribe(audio_path)

    print("=== TRANSCRIPTION ===")
    print(result["text"])

if __name__ == "__main__":
    main()
