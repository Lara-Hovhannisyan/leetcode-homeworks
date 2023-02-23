def reverse_bits(binary_string):
    sum_ = 0
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            sum_ += int(binary_string[i]) * pow(2, i)
    return f'{str(sum_)} ({binary_string[::-1]})'


bin_string = input()
print(reverse_bits(bin_string))
