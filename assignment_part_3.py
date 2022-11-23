import speech_recognition as sr
from scipy.io import wavfile
import numpy as np
from scipy.fft import *
from scipy.io import wavfile
import matplotlib.pyplot as plt

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

# getBearsPerMin returns the bpm of the drum file 
# the drum file has the weighted average filter applied with a window size of 100000
def getBeatsPerMin(file):
    sampleRate, data = wavfile.read(file)
    peakIndexes = []
    dist = 0

    # extract frequencies from data using fourier transform
    frequencies = fftfreq(len(data), 1 / sampleRate)
    freqLen = len(frequencies)

    # cases for when there is one item in array or first or last element is a peak
    if freqLen == 1:
        return 0

    # loop through the wav file data and append the indexes of the peaks into an array
    # increment through the loop by 2 elements to remove more noise
    for i in range(1, freqLen - 1, 4):
        if (i > 0 or i < freqLen - 1) and frequencies[i] >= frequencies[i-1] and frequencies[i] <= frequencies[i+1]:
            peakIndexes.append(i)

    # loop through peak indexes to get mean distance
    for i, _ in enumerate(peakIndexes):
        dist += data[i+1] - data[i]

    meanPeaksDist = dist/len(peakIndexes)

    bpm = (1/meanPeaksDist)*60

    return bpm

# detectSilentRegions returns the silent regions in the birds file
# the birds file has the median weighted average filter applied with a window size of 100000
def detectSilentRegions(file):
    sampleRate, data = wavfile.read(file)
    silentRegions = []

    # Apply fourier transform to extract fequencies
    frequencies = fftfreq(len(data), 1 / sampleRate)

    # extract indices (seconds) where the frequency is 0
    # indicating silence in the wav file
    for i, x in enumerate(frequencies):
        if x == 0:
            silentRegions.append(i)
    
    return silentRegions

# print(getNumSyllables('./audio_files/Speech.wav'))
# print(getBeatsPerMin('./audio_files/weighted_average_filter_drums_100000.wav'))
print(detectSilentRegions('./audio_files/mean_filter_birds.wav'))
