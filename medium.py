"""
Arrays && Hashes
49. Group Anagrams
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
# def groupAnagrams(strs: list[str]) -> list[list[str]]:
# 	dict_anagrams = {}
# 	for string in strs:
# 		# sort the string with sorted, but sorted converts the string into
# 		# ordered chars of the string in a list, so we join these chars and
# 		# gives us the string ordered not as a list
# 		# ['a', 'e', 't'] -> "aet"
# 		sortedstring = ''.join(sorted(string))
# 		# if the sortedstring already exists as a key in the dictionary,
# 		if sortedstring in dict_anagrams:
# 			# we append the string to that array of the key
# 			# {"aet": ["eat"]} -> {"aet": ["eat", "tea"]}
# 			dict_anagrams[sortedstring].append(string)
# 		else:
# 			# if the key doesnt exist in the dictionary we create the new key
# 			# and insert the value as a list of the string
# 			# {} -> {'aet': ["eat"]}
# 			dict_anagrams[sortedstring] = [string]
# 	return dict_anagrams.values()

# print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))

#################################################################################################

"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""
# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     count = {}
#     freq = [[] for i in range(len(nums)+1)]
#     for num in nums:
#         count[num] = 1+count.get(num, 0)
#     for num, idx in count.items():
#         freq[idx].append(num)
#     res = []
#     i = len(freq)-1
#     while i > 0:
#         for num in freq[i]:
#             res.append(num)
#             if len(res) == k:
#                 return res
#         i -= 1


# print(topKFrequent(nums=[1, 1, 1, 2, 2, 4, 5, 5, 8, 8, 8, 8, 3, 7, 7, 7], k=2))

#################################################################################################

"""
238. Product of Array Except Self
Given an integer array nums, return an array answer 
such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
# def productExceptSelf(nums: list[int]) -> list[int]:
    # O(n^2)
	# res = []
	# pr, pl, product = 1, 1, 1
	# for i in range(len(nums)):
	# 	for l in range(0, i):
	# 		pl *= nums[l]
	# 	for r in range(len(nums)-1, i, -1):
	# 		pr *= nums[r]
	# 	product = pr * pl
	# 	res.append(product)
	# 	product, pl, pr = 1, 1, 1
	# return res
	# # O(n)
# 	res = [1] * len(nums)
# 	pr, pl = 1, 1
# 	for l in range(len(nums)):
# 		res[l] = pl
# 		pl *= nums[l]
# 	for r in range(len(nums)-1, -1, -1):
# 		res[r] *= pr
# 		pr *= nums[r]
# 	return res

# print(productExceptSelf(nums=[1, 2, 3, 4]))

#################################################################################################

"""
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
# def longestConsecutive( nums: list[int]) -> int:
# 	numSet = set(nums)
# 	longest = 0
# 	for n in nums:
# 		if n - 1 not in numSet:
# 			length = 0
# 			while (n+length)in numSet:
# 				length+=1
# 			longest = max(length, longest)
# 	return longest

# print(longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))

#################################################################################################

"""
167. Two Sum II
**Input array is sorted**
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""
# def twoSum(nums: list[int], target: int) -> list[int]:
# 	i,j=0,len(nums)-1
# 	while i < j:
# 		curSum = nums[i] + nums[j]
# 		if curSum> target:
# 			nums.pop(j)
# 			j-=1
# 		if curSum< target:
# 			i+=1
# 		elif curSum and j == i:
# 			pass
# 		elif curSum == target:
# 			return [i+1,j+1]

# print(twoSum(nums = [1,3,4,5,7,10,11], target = 9))

#################################################################################################

"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
# def threeSum(nums: list[int]) -> list[list[int]]:
#     nums = sorted(nums)
#     res= []
#     for i in range(len(nums)):
#         j,k=i+1,len(nums)-1 
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#         while j < k:
#             threeSum = nums[i] + nums[j] + nums [k]
#             if threeSum > 0:
#                 k-=1
#             elif threeSum< 0:
#                 j+=1
#             else:
#                 res.append([nums[i],nums[j],nums[k]])
#                 j+=1
#                 while nums[j] == nums[j-1] and j < k:
#                     j+=1
#     return res

# print(threeSum(nums = [-1,0,1,2,-1,-4]))

#################################################################################################
"""
11. Container With Most Water
You are given an integer array height of length n. 
There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Example 1:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
Input: height = [1,1]
Output: 1
"""
# O(n) solution | optimal 
# area = height * width
# width = the distance between the two elements
# height = the lower bound of the two elements ex [5,6] the height would be 5 not 6
# def maxArea( height: list[int]) -> int:
# 	i, j = 0, len(height) - 1
# 	area = 0
# 	resArea = 0
# 	while i < j:
# 		area = (min(height[i], height[j])) * (j - i)
# 		if height[i] < height[j]:
# 			i+=1
# 		else:
# 			j -= 1
# 		resArea = max(resArea, area)
# 	return resArea

# print(maxArea(height= [1,3,2,5,25,24,5]))

#################################################################################################