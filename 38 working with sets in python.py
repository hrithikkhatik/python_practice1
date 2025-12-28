weekdays = ("mon", "tue", "wed", "thur", "fri")
s1 = set(weekdays)
print(s1)
# sets doesn't allowed duplicate

nums = {1, 3, 2, 0, -1}
print(0 in nums)
print(10 not in nums)
print(10 in nums)
# in is used for check available or not , not in is used

set1 = {2, 0, -1}
set1.add(5)
set1.add(0)
set1.discard(10)
# when we remove anything is not available cause error, discard does not give error

num_1 = {1, 3, 2, 0, -1}
num_2 = {3, 5}
print(num_1 | num_2)
print(num_1 & num_2)
print(num_1 - num_2)
l1 = list(num_1)
print(l1 * 3)

# sets position change every time
