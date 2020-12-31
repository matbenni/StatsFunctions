def calculateMean(data):
    n = len(data)
    if n < 1:
        raise ValueError('ERROR - Series not of length 1 or greater')
        
    return sum(data) / n
    
def calculateSS(data):
    c = calculateMean(data)
    ss = sum((x-c)**2 for x in data)
    return ss
    
def calculateStandardDeviation(data, ddof=0):
    n = len(data)
    if n < 1:
        raise ValueError('ERROR - Series not of length 1 or greater')
    ss = calculateSS(data)
    pvar = ss / (n-ddof)
    return pvar**.5

def calculateBiasedSkewness(data):
    sumDiff = 0
    n = len(data)
    m = calculateMean(data)
    for i in data:
        diff = (i - m) ** 3
        sumDiff = diff + sumDiff
    return sumDiff / (n * calculateStandardDeviation(data) ** 3)
def calculateUnbiasedSkewness(data):
    sumDiff = 0
    n = len(data) - 1
    m = calculateMean(data)
    for i in data:
        diff = (i - m) ** 3
        sumDiff = diff + sumDiff
    return sumDiff / (n * calculateStandardDeviation(data) ** 3)