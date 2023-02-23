def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


num_list = list(map(int, input("Enter a list of prices, separated by commas: ").split(",")))
print(max_subarray_sum(num_list))
