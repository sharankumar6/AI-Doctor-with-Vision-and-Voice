# gradio_app.py

import os
import gradio as gr

from brain_of_the_doctor import analyze_image_with_query, encode_image
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs

# Doctor system prompt
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
What's in this image?. Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
Donot say 'In the image I see' but say 'With what I see, I think you have ....'
Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."""

# Main function that handles the process
def process_input(audio_filepath, image_filepath):
    if not audio_filepath:
        return "No audio input provided.", "Cannot analyze without audio input.", None

    try:
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )
    except Exception as e:
        return "Error during transcription: " + str(e), "Transcription failed.", None

    if image_filepath:
        try:
            encoded_img = encode_image(image_filepath)
            doctor_response = analyze_image_with_query(
                query=system_prompt + speech_to_text_output,
                encoded_image=encoded_img,
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )
        except Exception as e:
            doctor_response = "Error analyzing image: " + str(e)
    else:
        doctor_response = "No image provided for me to analyze."

    try:
        voice_output_path = text_to_speech_with_elevenlabs(doctor_response, "Final.mp3")
    except Exception as e:
        return speech_to_text_output, doctor_response, None

    return speech_to_text_output, doctor_response, voice_output_path

# Gradio interface
interface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Speak your symptoms (required)"),
        gr.Image(type="filepath", label="Upload related medical image (optional)")
    ],
    outputs=[
        gr.Textbox(label="Transcribed Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's Voice Response")
    ],
    title="AI Doctor with Vision and Voice by Sharan Kumar",
    description="Speak your symptoms and upload a medical image. Get a concise medical-style response with voice output."
)

# Launch with sharing enabled
interface.launch(debug=True, share=True)


# #http://127.0.0.1:7860