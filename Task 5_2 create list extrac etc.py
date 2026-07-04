nums = [1,2,3,4,5,6,7,8,9,10] # 1.   Creates a list of numbers from 1 to 10.
nums5 = nums[0:5:1] # 2.   Extracts the first five elements from the list.
print(f"Original List: {nums}") # 4.   original list Prints 
print(f"Extracted First Five Elements: {nums5}") # 4 print extracted list
print(f"Reversed Extracted Elements: {nums5[::-1]}") # 4 print reverse list

"""  if we want to use reverse builtin function then it should be run after printing first 5 element
else it will reverse num5 list from start of the code.
""" 