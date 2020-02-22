#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:21:48 2020
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary 
until the first non-whitespace character is found. 
Then, starting from this character, 
takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, 
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, 
INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
Example 1:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@author: youwu
"""

#pure TDD, tedious code, too lazy to tide up.
class Solution:
    def myAtoi(self, str: str) -> int:
        string = str.strip()
        valid_start = ['0','1','2','3','4','5','6','7','8','9','+','-']
        if string == '' or string[0] not in valid_start:
            return(0)
        
        INT_MAX =  0x7fffffff
        INT_MIN = -0x80000000
        valid = ['0','1','2','3','4','5','6','7','8','9']

        if string[0] == '-':
            if string == '-' or string[1] not in valid:
                return(0)
            for index, char in enumerate(string[1:]):
                if char not in valid:
                    break
                
                if index == len(string) - 2 and string[-1] in valid:
                    index += 1
            
            try:
                integer = int(string[:index+1])
            except:
                return(INT_MIN)
                
            if integer < INT_MIN:
                return(INT_MIN)
            else:
                return (integer)

        
        if string[0] == '+':
            string = string[1:]
            
        if string == '':
            return(0)
        elif string[0] not in valid:
            return(0)
            
        for index, char in enumerate(string):
            if char not in valid:
                break
        if index == len(string) - 1 and string[-1] in valid:
            index += 1
        try:
            integer = int(string[:index])
        except:
            return(INT_MAX)
                
        if integer > INT_MAX:
            return(INT_MAX)
        else:
            return (integer)
            
            
                    
        
