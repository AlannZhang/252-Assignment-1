function meanFilterResult = applyMeanFilter(file, windowSize)
    [y,~] = audioread(file);
    meanFilterData = movmean(y, windowSize);
    plot(meanFilterData)
    saveas(gcf, sprintf('meanFilter%f.png', windowSize))
    meanFilterResult = meanFilterData;
end
