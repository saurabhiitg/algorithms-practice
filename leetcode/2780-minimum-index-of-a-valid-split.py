# Problem: 2780. Minimum Index of a Valid Split
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-index-of-a-valid-split/
# Tags: Prefix, Greedy, Frequency Count, Majority Element (Boyer-Moore)
# Date: 2025-03-27

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #find majority element
        #then  return the index when hits first majority
        #i.e. till index i , if count[x]>(i+1)/2  and leftover[x]>(n-i-1)/2) then return i

        #first find majority element
        cur = nums[0]
        cnt = 0
        for i in range(0,len(nums)):
            if cur!=nums[i]:
                cnt-=1
            else:
                cnt+=1
            if cnt==0:
                cnt = 1
                cur = nums[i]

        total = sum([x==cur for x in nums])
        cnt = 0
        for i in range(0, len(nums)-1):
            cnt+=(nums[i]==cur)
            if cnt>((i+1)/2) and (total-cnt)>((len(nums)-i-1)/2):
                return i
        return -1