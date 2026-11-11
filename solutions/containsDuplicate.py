class Solution(object):
    def firstAttempt(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Example 1:

        Input: nums = [1,2,3,1]
        Output: true

        Use a hashset and iterate through
        the list while adding the value
        if value does not exist in set. 
        Else, return True.

        Time: O(N)
        Space: O(N)
        """

        empty = set()
        for num in nums:
            if num not in empty:
                empty.add(num)
            else:
                return True
        return False
    
    def best(self, nums: list[int]) -> bool:
        """
        cleaner implementation
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False