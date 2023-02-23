def get_sum(a, b):
    # Base case: b is 0
    if b == 0:
        return a
    # Calculate the sum without carry using addition
    sum_without_carry = a ^ b
    # Calculate the carry using subtraction and recursion
    carry = (a & b) << 1
    return get_sum(sum_without_carry, carry)


print(get_sum(5, 7))