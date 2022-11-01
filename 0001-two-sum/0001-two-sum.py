class Solution:
    def twoSum(self, num: List[int], target: int) ->List[int]:         
        preMap ={} # val : index
    
        for i, n in enumerate(num):
            diff = target - n 
            if diff in preMap:
               return [preMap[diff], i]
            preMap[n] = i
        return 