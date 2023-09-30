#1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        soln={}
        for i, n in enumerate(nums):
            diff=target-n
            if diff in soln:
                return(i,soln[diff])
            soln[n]=i