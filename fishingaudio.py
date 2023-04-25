import keyboard
import time
import pyautogui
import numpy as np
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment

# define audio file path
audio_file_path = 'splash.wav'

# load audio file and convert to numpy array
audio = AudioSegment.from_wav(audio_file_path)
audio_data = np.array(audio.get_array_of_samples())
fs = audio.frame_rate

# set up audio detection parameters
audio_threshold = 0.01  # adjust this value to suit your needs
audio_duration = 1   # duration of audio segment to analyze (in seconds)
audio_step = int(fs * audio_duration)

# play and record reference audio
print('Playing reference audio...')
sd.play(audio_data, fs)
recording = sd.rec(int(fs * audio.duration_seconds), samplerate=fs, channels=1)
sd.wait()
print('Reference audio recorded.')

# main loop
while True:
    # cast line
    pyautogui.click(button='left')

    # wait for catch
    while True:
        # record audio segment
        recording = sd.rec(int(fs * audio_duration), samplerate=fs, channels=1)

        # wait for recording to finish
        sd.wait()

        # calculate energy of audio segment
        energy = np.sum(np.abs(recording)**2)

        # check if energy exceeds threshold
        if energy > audio_threshold:
            # load audio segment and convert to numpy array
            audio_segment = np.array(recording.flatten())
            # compare audio segment to target audio
            if np.sum(np.abs(audio_segment - audio_data[:len(audio_segment)])**2) < audio_threshold:
                reel_in()
                break
