#min/max(iterable,[default = obj, key = function])

list_of_nums = [2,5,7,3,9,1,0,4]
min_v = min(list_of_nums)
max_v = max(list_of_nums)
print(min_v, max_v)

print("------------------------")


#sorted(iterable, key = function, reverse = False)
array = [2,5,7,3,9,1,0,4]
x = array.sort()
print(array)

print(sorted(array,reverse=True))

print("------------------------")

#map(function, iterable)
list_of_nums = [2,5,7,3,9,1,0,4]
dict_of_nums = {1:1, 2:2, 3:3, 4:4}
new_dict = {k * v for k, v in dict_of_nums.items()} # dictionary comprehension
print(new_dict)

result = map(lambda x: x**2, list_of_nums)
print(list(result))

print("------------------------")

#filter(function, iterable)

list_of_nums = [2,5,7,3,9,1,0,4]
nums = list(filter(lambda x:x%2 !=0, list_of_nums))
print(nums)

print("------------------------")

#reduce(function, iterable[initializer])

from functools import reduce
list_of_nums = [2,5,7,3,9,1,0,4]
avg = reduce(lambda x, y : x+y, list_of_nums)/len(list_of_nums)
print("Average:", avg)

print("------------------------")