#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:39:39 2020

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

@author: youwu
"""
#DP l(i,j) represents whether s[i:j+1] is palindromic or not.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        l = [[True if i==j else False for i in range(len(s))] for j in range(len(s))]
        max_len = 1
        start = 0
        for j in range(1,len(s)):
            for i in range(0,j):
                if s[i]==s[j]:
                    if j-i < 3:
                        l[i][j] = True
                    else:
                        l[i][j] = l[i+1][j-1]
                else:
                    l[i][j] = False
        
                if l[i][j]:
                    cur_len = j-i+1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        s[start:start+max_len]
                        
        return s[start:start+max_len]
