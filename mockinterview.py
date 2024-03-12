'''
int arr 
longest lenght of subsequent
cond: item with same arthimetic difference 

[2,4,6,8] 
[3,6,9]

[2,4,7,10,-1]
[2,3,3,-11].

store prev_difference
compare cur_difference
if match -> O(1) 
-> longest subsequence with similar item

return length of longest subsequence with (^cond)
nums[i] < 0 < 5000
nums.length >= 2 

- subsequent 
- think of brute-force approach first 
'''
# Create a global_max, local_max
class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        res = 2 
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                first_diff = nums[j] - nums[i]
                minus_item = nums[j]
                local_res = 2 

                for k in range(j+1, len(nums)):
                    second_diff = nums[k] - minus_item
                    if second_diff == first_diff:
                           minus_item = nums[k]
                           local_res += 1 
                res = max(res, local_res)
        
        return res 

from unittest import TestCase
import unittest

class TestSolution(TestCase):
    def setUp(self):
        self.function = Solution().longestArithSeqLength

    def test_case_1(self):
        self.assertEqual(3, self.function([2,4,7,10,-1]))
    
    def test_case_2(self):
        self.assertEqual(2, self.function([2,4,7]))
    
    def test_case_3(self):
        self.assertEqual(2, self.function([2,3]))

    def test_case_4(self):
        self.assertEqual(4, self.function([2,4,6,7,8,9,-1]))
    
    def test_case_5(self):
        self.assertEqual(4, self.function([3,6,9,12]))

    def test_case_6(self):
        self.assertEqual(3, self.function([9,4,7,2,10]))

    def test_case_7(self):
        self.assertEqual(4, self.function([20,10000, 15,3,10,5,8])) 

if __name__ == '__main__':
    unittest.main()