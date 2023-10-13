def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Naive
        - Steps:
            1. Keep a fixed pair of values at a time, then moving another pointer 
            2. Sum the values pair with the pointer's value. If match 0 then append those as a new list to the ans arr
        - Complexitity: O(N^2 * N) =>  O(N^3) 

        Left and Right sides one by one: 
        - Intuition: Since the target of 3sum always be 0, at least 1 val is neg and 1 val is positive. So we assign 1 pointer as left, 1 pinter as rightLow, rightHigh
        - Drafting:
            1. Sorted first [-4,-1,-1, 0, 1, 2, 3]. 
            2. 
                1: First run -4 + 2 + 3 = 1 -> Positive
                2: Move rightLow pointer -4 + 1 + 3 = 0 -> BINBGO | [(-4), -1, -1, 0, (1), 2, (3)]
                3. Move left Pointer -1 + 1 + 3  => 3 -> Positive. Diff = 2 < 3sum => move rightLow. If Diff > 3sum, we can move rightHigh
                4. Move rightLow: -1 + 0 + 3 => 2 -> Positive. Since [rightLow] == 0, we have to move rightHigh
                5. Move rightHigh: -1 + 0 + 2 => 1 -> Positive. move rightLow
                6. Move rightLow: -1 + 0 + 1 => 0 -> BINGO. move left 
                7. move left: -1 + 0 + 1 => 0 -> BINGO, but already exist. move left
                8. left = rightLow -> break
            3. 
                1. First run -4 -1 + 3 = -2 -> Negative 
                2. Move leftHigh pointer -4 -1 + 3 = -2 -> Negative. Diff = -4 - (-1) = -3 => Move leftLow since there's a chance to cover the gap between low and high val (potentially 3, and filling target is 2) => we want to move leftLow as soon as we could
                3. Move leftLow -1 -1 + 3 = 1 -> Positive -> move right
                4. Move right -1 -1 + 2 = 0 -> BINGO -> move right 
                5. move right -1 -1 + 1 = -1 -> negative. index diff = 1 => move leftHigh 
                6. move leftHigh -1 + 0 + 1 = 0 -> BINGO -> move right 
                7. right = leftHigh -> break


        - Algo:
            1. Sorted the array
            2. Run 2 loops for 2 sides of neg and pos val. Each loop will have 2 pair of value for each side
            3. For each loop, we'll have 3 type of pointer: single pointer, low pointer, and high pointer
            4. Calc 3sum and compare to 0
            5. 
                a. If BINGO then check if it's exist in ans, then add to ans, then move oposite direction
                b. If its sign is opposite to the pointers pair sign (e.g negative to positive loop) then move opoosite direction
                c. If it shares the same sign as the pointers pair
                    c1. If rightLow equal to 0 or Diff < 3Sum, then move rightLow 
                    c2. Else move rightHigh 
        
        Fixed value at the left side an iterate the 2 pointers onwards 
        [-4,-1,-1, 0, 1, 2, 3]. -4 -1 +3 = -2 =>left -4 + 0 + 3 => -1 => left -4 + 1 + 3 = 0 =>  left -4 +2 + 3 = 1 => right left == right, so break 
        - Algo:
            1. Sorted the array
            2. Loop thru nums
            3. If num is the same as the preceeding num, then skip
            4. While left < right, then we 
            5. Compare the 3sum to target, if match then we add to ans 
            6. If negative, then increase left
            7. If positive, then decrease right 
            8. If next left is identical to curr left, then increase left until it isn't 
        """

        nums = sorted(nums)
        ans = []


        for i, num in enumerate(nums): 
            if i > 0 and num == nums[i-1]: 
                continue 
            
            left = i + 1 
            right = len(nums) - 1 
            
            while left < right: 
                vals = [nums[i], nums[left], nums[right]]
                s = sum(vals)
                if s == 0:
                    if vals not in ans:
                        ans.append(vals)
                    left += 1 
                
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        
        return ans 