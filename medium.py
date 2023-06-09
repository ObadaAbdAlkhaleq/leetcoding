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
