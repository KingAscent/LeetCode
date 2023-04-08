class Solution(object):
    def firstMissingPositive(self, nums):
			length = len(nums)
			i = 0

			while i < length:
				temp = nums[i]
				if 1 <= temp <= length:
					if nums[temp - 1] != temp:
						nums[i] = nums[temp - 1]
						nums[temp - 1] = temp
					else:
						i += 1
				else:
					i += 1
			
			for j in range(length):
				if nums[j] != j + 1:
					return j + 1

			return length + 1
