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

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    combinationSum(candidates, target)