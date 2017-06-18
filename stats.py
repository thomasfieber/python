from math import sqrt

def calculate_mean(array):
    # Calculate the nean of a list
    return sum(array) / len(array)

def calculate_median(array):
    # Calculate the median value of a list
    sorted_array = sorted(array)
    mid = len(sorted_array) // 2
    if len(sorted_array) % 2 == 1:
        return sorted_array[mid]
    else:
        return (sorted_array[mid] + sorted_array[mid - 1]) // 2

def calculate_mode(array):
    # Find the mode, or most frequently occuring
    # value in a list
    freq = {}
    max_val = 0
    mode = 0
    for i in array:
        freq[i] = freq.get(i, 0) + 1
    for k, v in freq.items():
        if v > max_val:
            max_val = v
            mode = k
    return mode

def calculate_variance(array):
    # Calculate the variance, or the average of the
    # sum of squared deviations from the mean
    mu = calculate_mean(array)
    return calculate_mean([(i - mu) ** 2 for i in array])

def alt_variance(array):
    # Another way to calculate variance
    n = len(array)
    return (sum_of_squares(array) / n) - (sum_of_array(array))**2 / (n ** 2)

def calculate_std_deviation(array):
    # Square root of the variance
    return alt_variance(array) ** 0.5

def sum_of_squares(array):
    # Find the sum of squares for an array
    return sum([i**2 for i in array])

def sum_of_array(array):
    # Calculate the sum of values in an array
    return sum([i for i in array])

def find_z(array, n):
    # Calculate Z scores for each element in
    # an array
    return (n - calculate_mean(array)) / calculate_std_deviation(array)

def sample_error(alist, n):
    # Find sample error
    return calculate_std_deviation(alist) / sqrt(n)

def sample_std_deviation(alist):
    # Calculate the sample standard deviation
    n = len(alist) - 1
    mu = calculate_mean(alist)
    squared_deviations = [(i - mu) ** 2 for i in alist]
    s_variance = sum_of_array(squared_deviations) / n
    s_std_dev = sqrt(s_variance)
    return s_std_dev

def sample_variance(alist):
    # Calculate sample variance
    n = len(alist) - 1
    mu = calculate_mean(alist)
    squared_deviations = [(i - mu) ** 2 for i in alist]
    s_variance = sum_of_array(squared_deviations) / n
    return s_variance
