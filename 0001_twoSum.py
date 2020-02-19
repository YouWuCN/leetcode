#Use dictionary to locate an element in O(1) 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num1 in enumerate(nums):
            num2 = target-num1
            if num2 in hashmap:
                return [index, hashmap[num2]]
            hashmap[num1] = index
        return []
