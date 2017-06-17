from math import sqrt

def calculate_mean(array):
    return sum(array) / len(array)

def calculate_median(array):
    sorted_array = sorted(array)
    mid = len(sorted_array) // 2
    if len(sorted_array) % 2 == 1:
        return sorted_array[mid]
    else:
        return (sorted_array[mid] + sorted_array[mid - 1]) // 2

def calculate_mode(array):
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
    mu = calculate_mean(array)
    return calculate_mean([(i - mu) ** 2 for i in array])

def alt_variance(array):
    n = len(array)
    return (sum_of_squares(array) / n) - (sum_of_array(array))**2 / (n ** 2)

def calculate_std_deviation(array):
    return alt_variance(array) ** 0.5

def sum_of_squares(array):
    return sum([i**2 for i in array])

def sum_of_array(array):
    return sum([i for i in array])

def find_z(array, n):
    return (n - calculate_mean(array)) / calculate_std_deviation(array)

def sample_error(alist, n):
    return calculate_std_deviation(alist) / sqrt(n)

def sample_std_deviation(alist):
    n = len(alist) - 1
    mu = calculate_mean(alist)
    squared_deviations = [(i - mu) ** 2 for i in alist]
    s_variance = sum_of_array(squared_deviations) / n
    s_std_dev = sqrt(s_variance)
    return s_std_dev

def sample_variance(alist):
    n = len(alist) - 1
    mu = calculate_mean(alist)
    squared_deviations = [(i - mu) ** 2 for i in alist]
    s_variance = sum_of_array(squared_deviations) / n
    return s_variance

sample = [24,
 13,
 26,
 22,
 21,
 13,
 27,
 20,
 26,
 24,
 28,
 19,
 10,
 10,
 17,
 30,
 21,
 14,
 18,
 16,
 16,
 18,
 15,
 23,
 22,
 25,
 18,
 20,
 26,
 18]

print(sample_std_deviation(sample))
print(sample_variance(sample))
