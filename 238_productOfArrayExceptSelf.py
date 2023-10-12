"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]"""
from functools import reduce


def productArray(nums: list[int]) -> list[int]:
    pLeft = 1
    pRight = 1
    pRights = []
    answer = []

    for i, num in enumerate(nums[::-1]):
        pRights.append(pRight)
        pRight *= num
    pRights = pRights[::-1]

    for i, num in enumerate(nums):
        answer.append(pLeft * pRights[i])
        pLeft *= num
    
    return answer

nums = [-1,1,0,-3,3]
print(productArray(nums))