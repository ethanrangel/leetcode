
class Solution(object):
    def bruteForce(self, nums: list[int], target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Ex:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
  
        First approach using two nested for loops.
        Iterate through every value nums and check
        if its sum with another value is equal to 
        target

        Time: O(N^2), in the worst case the list 
        gets iterated for every value nums

        Space: O(1), no datastructure created
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    if nums[i] + nums[j] == target:
                        return [i, j]
                
    def bruteForceV2(self, nums: list[int], target: int):
        """
        Same as previous version but does not 
        check previous sum of numbers
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def hashmap(self, nums: list[int], target: int) -> list[int] | None:
        """
        Used a hashmap to allow for 1 loop through
        nums and store value, indice pairs. We first 
        compute the complement and see if it exists 
        in our hashmap, if true we return the indices, 
        else append pair to hashmap

        Time: O(N), in the worst case, we iterate
        through the list once

        Space: O(N), created hashmap but its value are
        limited to the n values in list
        """
        hashmap = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashmap:
                return [i, hashmap[val]]
            hashmap[nums[i]] = i

    def best(self, nums: list[int], target: int) -> list[int] | None:
        """
        Same approach as before but simplified. Use 
        enumerate to get the index and value in a for 
        loop.
        """
        seen = {}
        for index, value in enumerate(nums):
            need = target - value
            if need in seen:
                return [index, seen[need]] 
            seen[value] = index

