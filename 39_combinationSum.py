# class Solution:
"""https://leetcode.com/problems/combination-sum"""
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """
            []
            / | \
            (2) 3  5
        / | \
        (2)  3  5
        / | \
    (2)  3  5
    / | \
(2)  3  5
    """

    results = []
    def helper(
        candidates: list[int] = candidates, 
        startIndex: int = 0,
        currentSum: int = 0, 
        combination: list[int] = [], 
        target: int = target
    ):
        if currentSum > target:
            return
        
        elif currentSum == target:
            results.append(combination)
            return
        
        else:
            for idx, candidate in enumerate(candidates):
                helper(
                    candidates=candidates[idx:], 
                    startIndex=idx,
                    currentSum=(currentSum + candidate), 
                    combination=combination + [candidate],
                    target=target
                )
    
    helper(candidates, 0, 0, [], target)

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            loop thru each item 
            recursive call the array start from the current idx 
            base case: 
                if sum(arr) > target: cook, 
                if == target, add to ans, then also cook
        """


        ans = []

        def helper(arr, idx):
            if sum(arr) > target:
                return 
            elif sum(arr) == target:
                nonlocal ans
                ans.append(arr[:])
                return
            
            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                helper(arr, i)
                arr.pop()
        
        helper([], 0)
        return ans