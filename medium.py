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
