import numpy as np


def calculate(list):
    # first create an array using numpy
    arr3 = np.array(list)

    # then try if the array can be reshape to 3X3 matrix
    try:
        arr3 = np.array(list).reshape(-1, 3)
    except:
        raise ValueError ("List must contain nine numbers.")

    # lists for every calculation
    mean = []
    variance = []
    standard_deviation = []
    max = []
    min = []
    sum = []

    # mean
    mean1 = arr3.mean(axis=0) # first calculate axis zero(columns) left-right
    mean2 = arr3.mean(axis=1) # then calculate axis one(rows) up-down
    meanAll = arr3.mean() # lastly calculate the whole list
    # then change them into list and append it to each lists above
    mean.append(mean1.tolist())
    mean.append(mean2.tolist())
    mean.append(meanAll)

    # everything below is the same as the above

    # variance
    variance1 = arr3.var(axis=0)
    variance2 = arr3.var(axis=1)
    varianceAll = arr3.var()
    variance.append(variance1.tolist())
    variance.append(variance2.tolist())
    variance.append(varianceAll)

    #standard deviation
    standard_deviation1 = arr3.std(axis=0)
    standard_deviation2 = arr3.std(axis=1)
    standard_deviationAll = arr3.std()
    standard_deviation.append(standard_deviation1.tolist())
    standard_deviation.append(standard_deviation2.tolist())
    standard_deviation.append(standard_deviationAll)

    # max
    max1 = arr3.max(axis=0)
    max2 = arr3.max(axis=1)
    maxAll = arr3.max()
    max.append(max1.tolist())
    max.append(max2.tolist())
    max.append(maxAll)

    # min
    min1 = arr3.min(axis=0)
    min2 = arr3.min(axis=1)
    minAll = arr3.min()
    min.append(min1.tolist())
    min.append(min2.tolist())
    min.append(minAll)

    # sum
    sum1 = arr3.sum(axis=0)
    sum2 = arr3.sum(axis=1)
    sumAll = arr3.sum()
    sum.append(sum1.tolist())
    sum.append(sum2.tolist())
    sum.append(sumAll)

    # make the lists above into values
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max,
        'min': min,
        'sum': sum
    }

    # lastly print it out as a dict
    return calculations
