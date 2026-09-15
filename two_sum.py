# 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。

from typing import List

# 写法一，双层循环，时间复杂度O(n²)​
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         """
#         根据给定一个整数数组和一个整数目标值，在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
#         :param nums:整数数组（不能使用两次相同的元素）
#         :param target:整数目标值
#         """
#         for i in range((len(nums)+1)//2):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target :
#                     index = [i,j]
#                     return index
#                 else:
#                     continue

# 写法二，用哈希表，时间复杂度O(n)
class Solution:
    def twoSum(self, nums, target):
        seen = {}                      # 值 -> 下标
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i

                
print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[3,2,4], target=6))
print(Solution().twoSum(nums = [3,3], target = 6))