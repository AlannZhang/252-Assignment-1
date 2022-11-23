% applyMeanFilter creates a plot and wav file based on the filter and returns the filter result
function meanFilterResult = applyMeanFilter(file, windowSize)
    [y,~] = audioread(file);
    meanFilterData = movmean(y, windowSize);
    plot(meanFilterData)
    saveas(gcf, sprintf('meanFilter%f.png', windowSize))
    audiowrite('meanFilter.wav', meanFilterData, 16000);
    meanFilterResult = meanFilterData;
end

% applyWeightedAverageFilter creates a plot and wav file based on the filter and returns the filter result
function weightedAverageFilterResult = applyWeightedAverageFilter(file, windowSize)
    [y,~] = audioread(file);
    b = gausswin(windowSize);
    weightedAverageFilterData = filter(b, 1, y);
    plot(weightedAverageFilterData)
    saveas(gcf, sprintf('weightedAverageFilter%f.png', windowSize))
    audiowrite('weightedAverageFilter.wav', weightedAverageFilterData, 16000);
    weightedAverageFilterResult = weightedAverageFilterData;
end

% applyMedianAverageFilter creates a plot and wav file based on the filter and returns the filter result
function medianAverageFilter = applyMedianAverageFilter(file, windowSize)
    [y,~] = audioread(file);
    medianFilterData = medfilt1(y);
    plot(medianFilterData)
    saveas(gcf, sprintf('medianAverageFilter%f.png', windowSize))
    audiowrite('medianAverageFilter.wav', medianFilterData, 16000);
    medianAverageFilterResult = medianFilterData;
end
