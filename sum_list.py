number_list = [36,93,55,42,12,24,100]
total =0 
biggest_num = 0
smallest_num = number_list[0]
even_num = []
positive_num = []
for num in number_list:
    if num >= 0:
        positive_num.append(num)
    if num % 2 == 0:
        even_num.append(num)
    if num < smallest_num:
        smallest_num = num
    total = total + num
    if num > biggest_num:
        biggest_num = num

print("%s is the total"% total)
print("%s is the biggest number "%biggest_num)
print("%s is the smallest number " % smallest_num)
print("Even numbers")

print(even_num)
print("Positive numbers")
print(positive_num)