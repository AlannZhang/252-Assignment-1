import wave
import audioop
import shutil
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# getWavFileCharacteristics uses wave package to extract sampling rate and number of channels
def getWavFileCharacteristics(file):
    with wave.open(file, 'rb') as waveFile:
        wavFileCharacteristics = {}
        wavFileCharacteristics['samplingRate'] = waveFile.getframerate()
        wavFileCharacteristics['numAudioChannels'] = waveFile.getnchannels()

        return wavFileCharacteristics

# convertStereoToMono converts an audio file to stereo if it is mono 
def convertStereoToMono(file):
    with wave.open(file, 'rb') as waveFile:
        # if file is stereo, create a new wav file and write the mono version to it
        # else the data is copied to a new file
        if waveFile.getnchannels() == 2:
            # check the name of the file to create a new file based on that name
            if 'Birds' in file: 
                createMonoFile('Birds', waveFile)
            if 'Drum' in file:
                createMonoFile('Drum', waveFile)
            if 'Speech' in file:
                createMonoFile('Speech', waveFile)
        else:
            if 'Birds' in file: 
                createNewWavFile(file, 'Birds')
            if 'Drum' in file:
                createNewWavFile(file, 'Drum')
            if 'Speech' in file:
                createNewWavFile(file, 'Speech')

# createMonoFile creates a mono file
def createMonoFile(fileName, waveFile):
    newFileName = './audio_files/' + fileName + '_mono_version_' + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '.wav'
    with open(newFileName, 'x'):
        monoFile = wave.open(newFileName, 'wb')
        monoFile.setparams(waveFile.getparams())
        monoFile.setnchannels(1)
        monoFile.writeframes(audioop.tomono(waveFile.readframes(float('inf')), waveFile.getsampwidth(), 1, 1))

# createNewWavFile writes wav file to a new file
def createNewWavFile(originalFile, fileName):
    newFile = './audio_files/' + fileName + '_copy_' + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '.wav'
    shutil.copyfile(originalFile, newFile)

# plotWavFile generates a plot of the waveform
def plotWavFile(fileName):
    with wave.open(fileName, 'rb') as waveFile:
        samplingRate = waveFile.getframerate()
        signal = waveFile.readframes(samplingRate)
        signal = np.frombuffer(signal, dtype='int16')

        if waveFile.getnchannels() == 2:
            return 'Can only plot mono audio files'

        if 'Birds' in fileName: 
            generateWavPlot('Birds', signal)
        if 'Drum' in fileName:
            generateWavPlot('Drum', signal)
        if 'Speech' in fileName:
            generateWavPlot('Speech', signal) 

# generateWavPlot creates a waveform plot
def generateWavPlot(fileName, signal):
    plt.figure(1)
    plt.title('Wave Form: ' + fileName)
    plt.ylabel('Amplitude')
    plt.xlabel('Time (s)')
    plt.plot(signal)
    plt.savefig('./waveform_graphs/' + fileName + '_' + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '_.png' )

# print('Birds.wav:', getWavFileCharacteristics('./audio_files/Birds.wav'))
# print('Drum.wav:', getWavFileCharacteristics('./audio_files/Drum.wav'))
# print('Drum Mono Version:', getWavFileCharacteristics('./audio_files/Drum_mono_version.wav'))
# print('Speech.wav:', getWavFileCharacteristics('./audio_files/Speech.wav'))
# print(convertStereoToMono('./audio_files/Speech.wav'))
# print(convertStereoToMono('./audio_files/Drum.wav'))
# print(convertStereoToMono('./audio_files/Birds.wav'))
# print(plotWavFile('./audio_files/Speech.wav'))
# print(plotWavFile('./audio_files/Drum_mono_version_2022-11-04 17:00:50.wav'))
# print(plotWavFile('./audio_files/Birds.wav'))
