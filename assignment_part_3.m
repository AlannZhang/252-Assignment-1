% getBeatsPerMinute
function beatsPerMinute = getBeatsPerMinute(file)
    
end

% detectSilentRegions returns the silent regions in the birds file
% by breaking down the signal into frames of 0.1s then identifying peaks < 0.03
% which is considered as silence
function silentRegions = detectSilentRegions(file)
    % calculate the length of the frames by multiplying
    % sample frequency and frame duration
    sampleFreq = 16000;
    frameDuration = 0.1;
    frameLen = frameDuration*sampleFreq;

    [data, sampleRate] = audioread(file);
    dataLen = size(data);
    numFrames = floor(dataLen)/frameLen;
    newSignal = zeros(dataLen, 1);
    count = 0;

    % moving windows
    % frameOne = data(1 : frameLen);
    % frameTwo = data(frameLen+1 : fameLen*2)
    % frameTwo = data(frameLen*2+1 : fameLen*3)

    for i = 1 : numFrames
        % extract a frame
        frame = data((i-1)*frameLen+1 : frameLen*i);
        
        % identify frames that are not silent
        maxPeak = max(frame);

        if (maxPeak > 0.03)
            count = count + 1;
            newSignal((count - 1)*frameLen+1 : frameLen*count) = frame;
        end
    end
    
end