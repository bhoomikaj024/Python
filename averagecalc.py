sum = 0
flag = 0
nums = input("Enter the nums to be averaged: \n").split( )
for i in range(0, len(nums)):
    int_num = int(nums[i])
    sum += int_num
    flag += 1
avg = sum / flag
# avgr = round(avg)
print(f"The average of the given numbers is {avg}.")

