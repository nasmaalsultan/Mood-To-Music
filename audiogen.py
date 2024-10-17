from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import uuid

def user_prompt_to_internal(text_prompt):
    template = """Music lyric: \"♪ {line} ♪\""""
    music_prompt = []
    for line in text_prompt:
        music_prompt.append(template.replace("{line}", line))
    return "\n".join(music_prompt)

def generate_audio_array(text_prompt):
    preload_models()
    music_prompt = user_prompt_to_internal(text_prompt)
    audio_array = generate_audio(music_prompt)
    return audio_array