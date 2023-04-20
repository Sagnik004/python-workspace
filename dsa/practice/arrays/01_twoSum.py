'''
https://leetcode.com/problems/two-sum/

Problem statement: Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to the target.
We may assume that each input would have exactly one solution, and we may not use 
the same element twice.
We can return the answer in any order.

Example_1: nums = [2,7,11,15], target = 9; o/p = [0,1]
Example_2: nums = [3,2,4], target = 6; o/p = [1,2]
Example_3: nums = [3,3], target = 6; o/p = [0,1]
'''

def twoSum(nums: list[int], target: int) -> list[int]:
  prev_nums = {} # already went through elements
  
  for i, el in enumerate(nums):
    diff = target - el
    if diff in prev_nums:
      return [prev_nums[diff], i]
    else:
      prev_nums[el] = i

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
