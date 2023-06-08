"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
# def twoSum(nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)-1):
#             # print(len(nums)-1)
#             #     print(len(nums))
#             for j in range(1, len(nums)):
#                 print([i,j])
#                 if nums[i] + nums[j] == target:
#                     print("correct one"+str([i,j]))
#                     return [i,j]
# traget= 9
# twoSum( nums = [8,11,15,2, 4, 7], target = 9)

#################################################################################################

"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:
Input: x = 121
Output: true
"""
# def isPalindrome(x: int) -> bool:
#     # consvert x to string
#     x = str(x)
#     # reverse x
#     r = x[::-1]
#     # return if x is the same as reversed
#     return x == r
# print(isPalindrome(x=121))

#################################################################################################

"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
    12 is written as XII, which is simply X + II. 
    The number 27 is written as XXVII, which is XX + V + II.
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
"""
# def romanToInt(s: str) -> int:
#     rnumrals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
#     resualt = 0
#     for i in range( len(s)) :
#         if i + 1< len(s) and rnumrals[s[i]] < rnumrals[s[i+1]] :
#             resualt+= -(rnumrals[s[i]])
#             # print("s"+str(resualt))
#         else:
#             resualt+= rnumrals[s[i]]
#             # print(resualt)
#     # print(resualt)
#     return resualt

# print(romanToInt(s="CMXCVIII"))

#################################################################################################

"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
# def longestCommonPrefix(strs: list[str]) -> str:
#     # assign the first word of the list as the common prefix
#     lcp = strs[0]
#     # iterate over the rest of the words in the list
#     for i in range(1, len(strs)):
#         # remove characters from the end of the lcp that arent in the strs[i] until the current word is the prefix
#         while strs[i].find(lcp) != 0:
#             lcp = lcp[:-1]
#             # if lcp becomes empty aka there is no common prefix, return an empty string
#             if not lcp:
#                 return ""
#     return lcp

# longestCommonPrefix(strs=["flight","flower","flow"])

#################################################################################################

"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
    Input: s = "()"
    Output: true
Example 2:
    Input: s = "()[]{}"
    Output: true
Example 3:
    Input: s = "(]"
    Output: false
"""

# def isValid(s: str) -> bool:
#     open_brackets = {"}":"{", ")":"(", "]":"["}
#     stack = []
#     for p in s:
#         # print(p)
#         if p in open_brackets.values():
#             stack.append(p)
#             # print(stack)
#         elif stack and open_brackets[p] == stack[-1]:
#             stack.pop()
#             # print("popped", str(stack))
#         else: return False
#     return stack == []
# print(isValid(s="{[()]}"))

#################################################################################################

"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists( list1: ListNode, list2: ListNode) -> ListNode:
#         if not list1: return list2
#         if not list2: return list1
#         dummylist = ListNode(0)
#         current = dummylist

#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next

#         if list1:
#             current.next = list1
#         elif list2:
#             current.next = list2
#         return dummylist.next

#     print(mergeTwoLists( list1=[1,2,4], list2 = [1,3,4]))

#################################################################################################

"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
    The remaining elements of nums are not important as well as the size of nums.

Return k.

NOTE: 
    in-place algorithm is an algorithm which transforms input using no auxiliary data structure. 
    However, a small amount of extra storage space is allowed for auxiliary variables.
"""
# def removeDuplicates(nums):
#     k = 1
#     l = 0
#     r = 1
#     while r < len(nums):
#         if nums[l] > nums[r]:
#             return k
#         elif nums[l] == nums[r]:
#             r += 1
#         else:
#             k += 1
#             l += 1
#             nums[l] = nums[r]
#             r += 1
#     # print("k =", str(k))
#     return k
# print(removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))

#################################################################################################

"""
27. Remove Elements
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
# def removeElement( nums: list[int], val: int) -> int:
#     k = len(nums)
#     r = k - 1
#     while r >= 0:
#         if nums[r] == val:
#             print("current element", str(nums[r]))
#             temp = nums[r]
#             nums.pop(r)
#             nums.append(temp)
#             k-=1
#         print("popped list: ", str(nums))
#         r-=1
#     print("k = ", str(k))
#     return k


# print(removeElement(nums=[0,1,2,2,3,0,4,2], val=2))

#################################################################################################

"""
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""
# def strStr(haystack: str, needle: str) -> int:
#     if needle in haystack:
#         return haystack.index(needle)
#     else: return -1

# print(strStr(haystack = "sadbutsad", needle = "sad"))

#################################################################################################

"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
# def searchInsert(nums: list[int], target: int) -> int:
#     if target in nums:
#         return nums.index(target)
#     elif target not in nums:
#         for i in range(len(nums)):
#             if target < nums[i]: return 0
#             elif target > nums[-1]:
#                 return len(nums)
#             elif nums[i] <= target <= nums[i+1]:
#                 return i+1

# print(searchInsert(nums = [1], target = 2))

#################################################################################################

"""
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""
# def lengthOfLastWord(s: str) -> int:
#     # s = s.rstrip()  # Remove trailing spaces
#     # if ' ' not in s:  # No spaces, return the length of the string
#     #     return len(s)
#     # else:
#     #     last_word = s.split(' ')[-1]  # Split string by spaces and take the last word
#     #     return len(last_word)
# # optimal solution
#     s = s.split()
#     longestLastWord = len(s[-1])
#     return longestLastWord


# print(lengthOfLastWord(s= "a"))

#################################################################################################

"""
66. Plus One
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


# def plusOne(digits: list[int]) -> list[int]:
#     i = len(digits)-1
#     while i >= 0:
#         if digits[i] == 9:
#             digits[i] = 0
#             i -= 1
#             if len(digits) == 1:
#                 digits.insert(0, 1)
#                 return digits
#         elif digits[i] != 9:
#             digits[i] += 1
#             return digits
#     return [1] + digits


# print(plusOne(digits=[4, 3, 2, 1]))

#################################################################################################

"""
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

    1010
        +
    1011
   =10101

"""
# def addBinary(a: str, b: str) -> str:
#     a, b = a[::-1], b[::-1]
#     carry = 0
#     res = ''
#     for num in range(len(a)):
#         if a[num] == "1" and b[num] == "1":
#             carry += 1
#             res += "0"
#         elif a[num] == "1" or b[num] == "1":
#             res += str(carry ^ 1)
#         else:
#             res += str(carry)
#             carry = 0
#     if carry:
#         res += '1'
#     return res[::-1]


# print(addBinary(a="11", b="1"))

# NOTE: this hasnt been fully solved
#################################################################################################

"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


# def containsDuplicate(nums: list[int]) -> bool:
#     # if not nums or len(nums) == 1:
#     #     return False
#     # if nums[0] == nums[1]:
#     #     return True
#     # else:
#     #     stack = []
#     #     for i in range(1, len(nums)):
#     #         r = nums[i]
#     #         stack.append(nums[i-1])
#     #         if nums[i] == r:
#     #             r += 1
#     #         if nums[i] in stack:
#     #             return True
#     #     return False
#         # optimal solution, using set as sets dont allow duplicates so we check if nums
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False


# print(containsDuplicate(nums=[0]))

#################################################################################################
