import wave

def getWavFileCharacteristics(file):
    # using wave package to extract sampling rate
    with wave.open(file, 'rb') as wave_file:
        wavFileCharacteristics = {}
        wavFileCharacteristics['samplingRate'] = wave_file.getframerate()
        wavFileCharacteristics['numAudioChannels'] = wave_file.getnchannels()

        return wavFileCharacteristics

print('Birds.wav:', getWavFileCharacteristics('./audio_files/Birds.wav'))
print('Drum.wav:', getWavFileCharacteristics('./audio_files/Drum.wav'))
print('Speech.wav:', getWavFileCharacteristics('./audio_files/Speech.wav'))
