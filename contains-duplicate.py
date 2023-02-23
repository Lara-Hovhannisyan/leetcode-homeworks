numbers = list(map(int, input("Enter a list of integers, separated by commas: ").split(",")))

seen = set()
for num in numbers:
    if num in seen:
        print(True)
        break
    seen.add(num)
else:
    print(False)
