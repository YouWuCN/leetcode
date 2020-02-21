#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:37:13 2020

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@author: youwu
"""

class Solution1:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False

        def valid(s1, s2): 
            return((s1 =='('and s2==')') or (s1 =='[' and s2==']') or (s1=='{' and s2=='}'))
            
        stack = []
        for char in s:
            if stack == []:
                stack.append(char)
                continue
            if valid(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)

        return (stack == [])
    
class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        valid = {'(':')', '[':']','{':'}'}
        stack = []
        for char in s:
            if char in valid:
                stack.append(char)
            elif stack ==[] or char != valid[stack.pop()]:
                return False
        return (stack == [])