numbers = int(input("how many numbers they want to enter: "))
nums = []
for i in range(numbers):
    num = int(input(f"enter number {i+1}: "))
    nums.append(num)
print(f"The smallest number:{min(nums)}")
print(f"The largest number:{max(nums)}")
print(f"The total sum of all numbers:{sum(nums)}")
print(f"The average of the numbers:{sum(nums) / len(nums)}")
print(f"The complete list of numbers entered:{nums}")
print(f"the numbers in sorted order:{sorted(nums)}")