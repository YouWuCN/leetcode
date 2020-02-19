#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:16:31 2020
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

@author: youwu
"""

#move two pointers from left and right sides to the middle
class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height) - 1
        left = 0
        right = width
        if height[left]>height[right]:
            maxArea = height[right] * width
            right -= 1
        else:
            maxArea = height[left] * width
            left += 1
        width -= 1
        while left < right:
            if height[left] > height[right]:
                local_max = height[right] * width
                if local_max > maxArea:
                    maxArea = local_max
                right -= 1
            else:
                local_max = height[left] * width
                if local_max > maxArea:
                    maxArea = local_max
                left += 1
            width -= 1
        return maxArea