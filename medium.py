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
# 		res[r] = pr
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
