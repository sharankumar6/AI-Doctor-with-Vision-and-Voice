# 🧠 AI Doctor with Vision and Voice

An intelligent multimodal AI assistant that mimics a virtual doctor, allowing patients to interact via voice and image input. The system interprets user speech, analyzes uploaded medical images, and generates a voice response — all powered by advanced AI models.

---

## 📸 Project Overview

This project is a proof of concept for a virtual AI doctor that combines:

- **Speech-to-Text (STT)** to understand patient queries
- **Vision + LLM** to interpret uploaded medical images and generate responses
- **Text-to-Speech (TTS)** to respond with a human-like doctor’s voice
- **Gradio UI** to bring it all together in an interactive web app

---

## 🛠️ Tech Stack

| Feature | Tool / API |
|--------|-------------|
| LLM + Vision | [`meta-llama/llama-4-scout-17b-16e-instruct`](https://huggingface.co/meta-llama/llama-4-scout-17b-16e-instruct) via [Groq API](https://console.groq.com/) |
| Speech-to-Text (STT) | `whisper-large-v3` via [Groq Whisper API](https://console.groq.com/) |
| Text-to-Speech (TTS) | `eleven_turbo_v2` via [ElevenLabs API](https://www.elevenlabs.io/) |
| UI Interface | [Gradio](https://gradio.app/) |

---
