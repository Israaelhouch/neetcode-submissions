class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res= 0
        for i in range(len(nums)):
            csq = 0
            for j in range(i, len(nums)):
                if nums[j] ==1:
                    csq+=1
                else:
                    break
            res = max(res, csq)
        return res


        