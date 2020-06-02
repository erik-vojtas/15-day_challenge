# Arithmetic mean: absolute performance with limited variation;
# Mju = all values divided by number of values

numbers = [10, 12.5, 30]
def arithmeticMean(list_of_num):
    sum = 0
    for n in list_of_num:
        sum += n
    return round(sum/len(list_of_num), 2)

print("AM", arithmeticMean(numbers))

# Weighted arithmetic mean: absolute performance with known frequencies;  
# WM = value1 * frequency1 + value2 * frequency2 * …. valueN * frequencyN  
speed_in_sec = [10, 12.5, 30]
frequencies = [0.45, 0.35, 0.2]

def weightedArithmeticMean(list_of_num, list_of_freq):
    G = 0
    for x in range(0, len(list_of_num)):
        G += list_of_num[x] * list_of_freq[x]
    return G

print("WAM", weightedArithmeticMean(speed_in_sec, frequencies))

# Geometric mean: varied performance relative to reference machine 
# G = n root of  all values 


def geometricMean(list_of_num):
    sum = 1
    for x in list_of_num:
        sum *= x
    result = sum ** (1/len(list_of_num))
    return result

print("GM", geometricMean(speed_in_sec))


# Harmonic mean: performance rates (operations/seconds) 
# H = n / (1/value1 + 1/value2 +…. 1/valueN)
calculations_per_sec = [10, 20,5]
def harmonicMean(list_of_num):
    sum = 0
    for x in list_of_num:
        sum += 1/x
    HM = len(list_of_num)/ (sum)
    return round(HM, 2)

print("HM", harmonicMean(calculations_per_sec))