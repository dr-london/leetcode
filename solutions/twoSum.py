from typing import List

class Solution:
    # not used to this syntax, took a while to understand it
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        # finding the enumerate fucntion took forever, but was what i was looking for
        for i, num in enumerate(nums):
            numList = target - num
            if numList in num_dict:
                return [num_dict[numList], i]
            num_dict[num] = i
        return []


question1 = Solution()
nums = [2, 7, 11, 15]
target = 9
result = question1.twoSum(nums, target)
print(result)

question2 = Solution()
nums = [3, 2, 4]
target = 6
result = question2.twoSum(nums, target)
print(result)

question3 = Solution()
nums = [3,3]
target = 6
result = question3.twoSum(nums, target)
print(result)