# 1. Two Sum
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
# since we have to find the indexes of two numbers in the array which the sum of them is equal to target，
# It's better to use the value of the elements in array as key in hash tables
def twoSum(nums, target):
    nums_hashTable = {}
    for index, value in enumerate(nums):
        num1_value = target - value
        if num1_value in nums_hashTable:
            return [nums_hashTable[num1_value],index]
        nums_hashTable[value] = index
    return []

nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1)) 


#这个方法要考虑到原始数组的索引，排序后索引会发生改变
# def twoSum(nums, target):
#     sorted_nums = sorted(nums)
#     left, right = 0, len(sorted_nums) - 1
#     while left < right:
#         current_sum = sorted_nums[left] + sorted_nums[right]
#         if current_sum == target:
#             index1 = nums.index(sorted_nums[left])
#             # 遍历剩余部分的数组，查找第二个数值的索引
#             for i in range(index1 + 1, len(nums)):
#                 if nums[i] == sorted_nums[right]:
#                     return [index1, i]
#         # 如果和小于目标值，则将左指针向右移动一位
#         elif current_sum < target:
#             left += 1
#         # 如果和大于目标值，则将右指针向左移动一位
#         else:
#             right -= 1

#传统方法,注意遍历的范围，外层从左开始，内层从右开始
# def twoSum(nums, target):
#     for i in range(0,len(nums)):
#         for j in range(len(nums) - 1, i, -1):
#             if nums[i] + nums[j] == target:
#                 return [i,j] 
#         return []

nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1)) 