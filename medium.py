"""
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


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagramlist = {}
    for string in strs:
        sortedstr = ''.join(sorted(string))
        if sortedstr in anagramlist:
            anagramlist[sortedstr].append(string)
        else:
            anagramlist[sortedstr] = [string]
    return anagramlist.values()


print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
