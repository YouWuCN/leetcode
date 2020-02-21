#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:05:48 2020
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@author: youwu
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [('0','?')]
        for index, char in enumerate(s):
            '''
            remove valid parentheses, leave invalid char and their index
            '''
            if char == ')' and stack[-1][1]== '(':
                stack.pop()
            else:
                stack.append((index, char))
        stack.append((len(s),'?'))
        
        length = []
        for i in range(1,len(stack)):
            '''
            compute the max length gap
            '''
            length.append(int(stack[i][0])-int(stack[i-1][0]) )
            
        return (max(length) // 2) *2
            
            
            
            
            
            