import speech_recognition as sr
from scipy.io import wavfile
import numpy as np
from scipy.fft import *
from scipy.io import wavfile
import matplotlib.pyplot as plt
from datetime import datetime

# getNumSyllables returns the number of syllables in the speech clip
def getNumSyllables(file):
    with sr.AudioFile(file) as source:
        r = sr.Recognizer()
        count = 0
        vowels = 'aeiouy'

        # load audio to memory
        audioData = r.record(source)

        # convert speech to text using Google API
        text = r.recognize_google(audioData)
        print(text)

        for i in range(0, len(text)-1):
            # if letter is a vowel and previous letter is not a vowel
            # count it as a syllable, ex: ca
            if text[i] in vowels and text[i-1] not in vowels:
                count += 1

            # if no consonants then assume text is one syllable
            if count == 0:
                count += 1

        return count

# getBeatsPerMin returns the bpm of the drum file 
def getBeatsPerMin(file):
    # extract data and sample rate
    sampleRate, data = wavfile.read(file)
    
    # peak count
    count = 0

    # update peak count (drum hits)
    for i, _ in enumerate(data, 1):
        # peak has to be greater then prev and next value
        # peak value has to be greater then 490 as determined from the graph 
        # with the median filter applied
        if i < len(data) - 1 and data[i] > data[i-1] and data[i] > data[i+1] and data[i] > 490:
            count += 1

    # get the duration of the file in seconds then convert to minutes
    # calculate bpm by dividing count of peaks by duration in minutes
    fileDurationSeconds = len(data)/sampleRate
    fileDurationMins = fileDurationSeconds/60
    bpm = count/fileDurationMins

    return bpm

# detectSilentRegions returns the silent regions in the birds file
def detectSilentRegions(file):
    # extract data from wav file, and length of data array
    _, data = wavfile.read(file)

    silentIndexes = []

    # loop through wav file to retrieve indexes where
    # the amplitude is < 25 and > -25, indicating silence
    for i, x in enumerate(data):
        if x < 25 and x > -25:
            silentIndexes.append(i)

    silentRegionIndexes = np.array(silentIndexes, dtype=np.uint32)

    # plot the original signal data, along with the silent region
    plt.plot(data)
    plt.plot(silentRegionIndexes, data[silentRegionIndexes], 'x', markersize=0.5)
    plt.title('Silent Regions of Birds File: ')
    plt.ylabel('Amplitude')
    plt.xlabel('Number of Samples')
    plt.savefig('./waveform_graphs/bird_silent_regions_' + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '_.png' )

    return
