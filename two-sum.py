nums = list(map(int, input("Enter a list of integers, separated by commas: ").split(",")))
target = int(input("Enter the target integer: "))

nums_dict = {}

for i, num in enumerate(nums):
    complement = target - num
    if complement in nums_dict:
        print([nums_dict[complement], i])
        break
    nums_dict[num] = i
