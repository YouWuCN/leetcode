#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:59:15 2020
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@author: youwu
"""

#Sliding window O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        buffer =[]
        cur_len = 0
        max_len = 0
        for char in s:
            if char in buffer:
                buffer = buffer[buffer.index(char)+1:]
                buffer.append(char)
                cur_len = len(buffer)
            else:
                buffer.append(char)
                cur_len += 1

            max_len = max(max_len, cur_len)

        return(max_len)