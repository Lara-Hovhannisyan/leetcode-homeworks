def hamming_weight(binary_string):
    sum_ = 0
    for i in binary_string:
        if i == '1':
            sum_ += 1
    return sum_


# def hamming_weight(binary_string):
#     return binary_string.count('1')

bin_string = input()
print(hamming_weight(bin_string))