from collections import defaultdict

class Solution(object):
    def twoHashmaps(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool

        Can first check if the size of the
        strings are equal

        Hashmaps can be used to keep track of
        the distinct letters and their counts.
        After looping through s and updating
        s_count, we loop through t and update 
        t_count but check to make sure the value
        for a letter found in t has been recorded
        in s_count and the count is not more.

        Time: O(s + t), have too loop through each
        string

        Space: O(1), there will only be up to 26
        charcter in each dictonary, regardless of
        the size of s or t.
        """
        if len(s) != len(t):
            return False
        
        s_count: dict[str, int] = {}
        t_count: dict[str, int] = {}

        for letter in s:
            if letter in s_count:
                s_count[letter] += 1
            else:
                s_count[letter] = 1
        for letter in t:
            if letter not in s_count:
                return False
            if letter in t_count:
                t_count[letter] += 1
                if t_count[letter] > s_count[letter]:
                    return False
            else:
                t_count[letter] = 1
        return True

    def oneHashmap(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool

        Use one hashmap to keep track of the distinct 
        letters and their counts. After looping 
        through s and updating count, we loop through 
        t and subtact the count value, and if we ever 
        reach a letter not in count or the value
        goes below 0, its not an anagram.
        """
        if len(s) != len(t):
            return False
    
        count: dict[str, int] = {}

        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        for letter in t:
            if letter not in count:
                return False
            if letter in count:
                count[letter] -= 1
                if count[letter] < 0:
                    return False
        return True

    def best(self, s: str, t:str) -> bool:
        """
        same approach as before but using better
        syntax, we can use defaultdict(int), 
        which gives the value 0 to accessed that
        does not yet exist in a hashmap. We can use
        this to return False as well.
        """
        if len(t) != len(s):
            return False

        count: dict[str, int] = defaultdict(int)
        for letter in s:
            count[letter] += 1
        
        for letter in t:
            if not count[letter]:
                return False
            count[letter] -= 1
        return True