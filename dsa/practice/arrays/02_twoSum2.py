'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem statement: Given a 1-indexed array of integers numbers that is already sorted 
in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] 
of length 2. 

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example_1: numbers = [2,7,11,15], target = 9; o/p = [1,2]
Example_2: numbers = [2,3,4], target = 6; o/p = [1,3]
Example_3: numbers = [-1,0], target = -1; o/p = [1,2]
'''

# Approach: Since we know that the list is sorted, we will use 2 pointer approach.
# Left pointer at the start of list, and right pointer at end of list. We will take
# the sum and shift the left and right pointers comparing it with the target.
# Time complexity: O(n), Space complexity: O(1)

def twoSum(numbers: list[int], target: int) -> list[int]:
  left, right = 0, len(numbers) - 1
  
  while left < right:
    cur_sum = numbers[left] + numbers[right]
    if cur_sum == target:
      return [left+1, right+1]
    elif cur_sum > target:
      right -= 1
    elif cur_sum < target:
      left += 1

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))
print(twoSum([1,3,4,5,7,11], 9))
