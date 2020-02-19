#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:57:46 2020
Given an array nums of n integers, 
are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

@author: youwu
"""
#sort the list first, fix one number, move two pointers one from the left and one right
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        last = len(nums)-1
        res = []        
        for i in range(last-1):
            if nums[0] > 0:
                break
            if i >= 1 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = last
            while left < right:
                threeSum = nums[i]+nums[left]+nums[right]
                if threeSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while(left < right and nums[left+1] == nums[left]):
                        left += 1
                    left += 1
                    while(left < right and nums[right-1] == nums[right]):
                        right -= 1
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1
        return res