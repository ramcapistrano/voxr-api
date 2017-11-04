# measure_wav.py
# Paul Boersma 2017-01-03
#
# A sample script that uses the Vokaturi library to extract the emotions from
# a wav file on disk. The file can contain a mono or stereo recording.
#
# Call syntax:
#   python3 measure_wav.py path_to_sound_file.wav

import sys
import scipy.io.wavfile
import soundfile as sf
from utils import get_vokaturi_lib

from app.OpenVokaturi import Vokaturi
# sys.path.append("app/OpenVokaturi/api")
# import Vokaturi


def extract_emotions(file_path):

    Vokaturi.load(get_vokaturi_lib())

    sf_data, sf_sample_rate = sf.read(file_path, dtype='int16')
    sf.write(file_path, sf_data, 44100, 'PCM_16')

    (sample_rate, samples) = scipy.io.wavfile.read(file_path)

    buffer_length = len(samples)

    c_buffer = Vokaturi.SampleArrayC(buffer_length)
    if samples.ndim == 1:
        c_buffer[:] = samples[:] / 32768.0  # mono
    else:
        c_buffer[:] = 0.5*(samples[:,0]+0.0+samples[:,1]) / 32768.0  # stereo

    voice = Vokaturi.Voice(sample_rate, buffer_length)

    voice.fill(buffer_length, c_buffer)

    quality = Vokaturi.Quality()
    emotionProbabilities = Vokaturi.EmotionProbabilities()
    voice.extract(quality, emotionProbabilities)

    # if quality.valid:
    print("Neutral: %.3f" % emotionProbabilities.neutrality)
    print("Happy: %.3f" % emotionProbabilities.happiness)
    print("Sad: %.3f" % emotionProbabilities.sadness)
    print("Angry: %.3f" % emotionProbabilities.anger)
    print("Fear: %.3f" % emotionProbabilities.fear)

    emotions = {
        'neutrality': "%.3f" % emotionProbabilities.neutrality,
        'happiness': "%.3f" % emotionProbabilities.happiness,
        'sadness': "%.3f" % emotionProbabilities.sadness,
        'anger': "%.3f" % emotionProbabilities.anger,
        'fear': "%.3f" % emotionProbabilities.fear
    }

    voice.destroy()

    return emotions
