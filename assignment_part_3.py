import speech_recognition as sr
from scipy.io import wavfile

# getNumSyllables returns the number of syllables in the speech clip
def getNumSyllables(file):
    with sr.AudioFile(file) as source:
        r = sr.Recognizer()
        count = 0
        vowels = 'aeiouy'

        # load audio to memor
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

# 2) Determine the beats per minute in the drum clip. When you play a drum, there is a
# sound of clicks that corresponds to the beat (called metronome). This can usually vary
# from 40 to 210 beats per minute. Beats per minute estimation can be complex and
# requires software to detect it accurately. I only expect you to come out with a small
# and easy algorithm that only focuses on the drum hits as the beats or any combination
# you want. There is no single solution here just make sure you explain your algorithm
# and determine its advantages and limitations while keeping it simple.
def getBeatsPerMin(file):
    _, data = wavfile.read(file)
    peakIndexes = []
    dataLen = len(data)
    dist = 0

    # cases for when there is one item in array or first or last element is a peak
    if dataLen == 1:
        return 0

    # loop through the wav file data and append the indexes of the peaks into an array
    # increment through the loop by 4 elements to remove more noise
    for i in range(1, dataLen - 1, 4):
        if (i > 0 or i < dataLen - 1) and data[i] >= data[i-1] and data[i] <= data[i+1]:
            peakIndexes.append(i)

    # loop through peak indexes to get mean distance
    for i, x in enumerate(peakIndexes):
        dist += data[i+1] - data[i]

    meanPeaksDist = dist/len(peakIndexes)

    bpm = (1/meanPeaksDist)*60

    return bpm

# 3) Detect the silent regions in the birds clip. You need to show at least one plot where
# your algorithm can detect these regions inside the clip.
def detectSilentRegions(file):
    return

# print(getNumSyllables('./audio_files/Speech.wav'))
# print(getBeatsPerMin('./audio_files/weighted_average_filter_drums_100000.wav'))
