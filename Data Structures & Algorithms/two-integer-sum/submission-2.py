"""class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
                    return res
        return []
        """


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in map:
                return [map[complement], i]
            else:
                map[nums[i]] = i

        