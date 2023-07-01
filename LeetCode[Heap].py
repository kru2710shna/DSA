#!/usr/bin/env python
# coding: utf-8

# ## LeetCode Problems 

# #### Topic: Heap
# #### The probelms are numbered according to numbering on LeetCode Problems 

# Problem: #973. K Closest Points to Origin
# 
# Level - Medium
# 
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# 
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# 
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
# 
# Example 1:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# 
# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

# In[2]:


class Solution(object):
   def kClosest(self, points, k):
       """
       :type points: List[List[int]]
       :type k: int
       :rtype: List[List[int]]
       """
       minHeap = []
       for x, y in points:
           dist = (x ** 2) + (y ** 2)
           minHeap.append([dist, x, y]) 

       heapq.heapify(minHeap)
       res = []
       while k > 0:
           dist, x, y = heapq.heappop(minHeap)
           res.append([x, y])
           k -= 1
       return res


# Time Complexity: O(nlog k) Runtime: 746ms

# Problem: #215. Kth Largest Element in an Array
# 
# Level - Medium
# 
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
# 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# 
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# In[3]:


import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minheap = []

        for num in nums:
            heapq.heappush(minheap , num)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]


# Time Complexity:O(n logk) Runtime: 1102ms

# Problem: #767. Reorganize String
# 
# Level - Medium
# 
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.
# 
# Example 1:
# Input: s = "aab"
# Output: "aba"
# 
# Example 2:
# Input: s = "aaab"
# Output: ""
# 

# In[4]:


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s) # Hashmap, count each char
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) # 0(n)
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
        # most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char 
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res
        


# Time Complexity: O(nlog n ) Runtime: 20ms

# In[5]:


class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        n = len(heights)
        heap =[]
        for i in range(n-1):
            diff = heights[i] - heights[i+1]
            if diff <=  0 :
                continue 
            heappush(heap, diff)
            if len(heap) > ladders:
                min_h = heappop(heap)
                bricks -= min_h
            if bricks < 0 :
                return i 
        return N-1


# Time Complexity: O(n logn) Runtime: 750ms

# In[ ]:




