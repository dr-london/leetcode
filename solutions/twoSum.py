from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complete_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complete_dict:
                return [complete_dict[complement], i]
            complete_dict[num] = i
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