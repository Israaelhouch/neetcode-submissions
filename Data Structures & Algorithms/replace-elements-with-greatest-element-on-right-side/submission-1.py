class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res= []
        for i in range(0,len(arr)-1):
            right_list = arr[i+1:len(arr)]
            res.append(max(right_list))
        res.append(-1)
        return res
