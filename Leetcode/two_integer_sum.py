from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                return []

nums = [3,4,5,6]
target = 7
solution_instance = Solution()
result = solution_instance.twoSum(nums,target)
print(result)

