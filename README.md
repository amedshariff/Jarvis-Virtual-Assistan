# J.A.R.V.I.S. Voice Assistant

A lightweight, Python-based voice assistant that listens for a wake word and performs basic tasks like opening specific websites, playing music from YouTube, or answering questions.

## Features

- **Wake Word Activation**: Listens for the wake word `"Jarvis"`.
- **Single-Step Execution**: Say `"Jarvis open YouTube"` or `"Jarvis play safar"` in one breath, and it will execute immediately.
- **Two-Step Interaction**: Say `"Jarvis"`, wait for the assistant to respond with `"yes"`, and then say your command.
- **Ambient Noise Calibration**: Automatically calibrates for background noise on startup to prevent false triggers and improve speech recognition accuracy.
- **Robust Browser Fallback**: Detects if Google Chrome is installed at the default location. If not, it gracefully falls back to using the system's default browser.
- **Interactive Vocal Feedback**: Explains what it's doing (e.g. *"Opening YouTube"*, *"Playing safar"*) and provides guidance if a command isn't recognized.

---

## Dependencies & Installation

To run the assistant, you need to install the following dependencies:

```bash
pip install speechrecognition pyttsx3 pyaudio comtypes
```

### Windows Prerequisites
* **PyAudio**: Required for microphone input. If standard installation fails, you can install it via pip or conda.
* **comtypes**: Required by `pyttsx3` to communicate with the Windows SAPI5 Text-To-Speech engine.

---

## File Structure

```
├── main.py        # Core logic, speech recognition, and command executor
└── musicLib.py    # Local music library with song names mapped to URLs
```

---

## Supported Commands

| Command | Action |
| --- | --- |
| **"open chrome"** | Opens Google Chrome to Google.com |
| **"open youtube"** | Opens YouTube in the browser |
| **"open chatgpt"** | Opens ChatGPT in the browser |
| **"play [song_name]"** | Looks up `song_name` in `musicLib.py` and opens it in the browser |
| **"what can you do"** | Explains the assistant's capabilities |

### Music Library (`musicLib.py`)
You can add your favorite songs by editing the dictionary in [musicLib.py](file:///c:/Users/Ahmed%20Shariff/OneDrive/Desktop/jarvis/musicLib.py):
```python
music = {
    "safar": "https://www.youtube.com/watch?v=...",
    "sunn raha hai": "https://www.youtube.com/watch?v=..."
}
```

---

## How to Run

Run the assistant from your terminal using python's unbuffered mode:

```bash
python -u main.py
```

### How to use:
1. Speak `"Jarvis"` to wake up the assistant. It will reply `"yes"`.
2. Speak your command (e.g., `"open youtube"`).
3. Alternatively, trigger it directly with a single phrase like: `"Jarvis play safar"`.
