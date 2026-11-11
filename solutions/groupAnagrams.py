from collections import defaultdict
import string

class Solution(object):
    def useSorted(self, strs: list[str]) -> list[list[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        use a dictionary and loop through
        the strings in the list, use sorted()
        to create a key we can group anagrams by.

        N = number of strings
        K = maximum length of a string

        Time: O(N x KlogK) loop through the list 
        and have to sort each value KlogK

        Space: O(N X K) dict can hold as many 
        distinct values string exist in strs
        """
        group: dict[str, list[str]] = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in group:
                group[sorted_string] = []
            group[sorted_string].append(string)
        return list(group.values())
    
    def useStringLibrary(self, strs: list[str]) -> list[list[str]]:
        """
        This uses the string module to make
        a string with all lowercase letters
        in the alpahabet. We can also then use
        tuple directly instead of list 
        comprehension.

        Time: O(N x 26 x K) loop through the list 
        and create a code for each string

        Space: O(N X K) dict can hold as many 
        distinct values string exist in strs
        """
        res: dict[tuple[int, ...], list[str]] = defaultdict(list)
        alphabet = string.ascii_lowercase

        # print(type(alphabet))  # <class 'str'>
        # print(alphabet)        # abcdefghijklmnopqrstuvwxyz
        # print(alphabet[0])     # a

        for s in strs:
            key = tuple(s.count(ch) for ch in alphabet)
            res[tuple(key)].append(s)
        return list(res.values())

    def best(self, strs: list[str]) -> list[list[str]]:
        """
        use a dictionary to store a code, this
        will be a tuple of ints that represents
        the all letters in alphabet, and the current
        string count for each letter, matching 
        anagrams would have the same code.

        Time: O(N x K) loop through the list 
        and create a code for each string

        Space: O(N X K) dict can hold as many 
        distinct values string exist in strs
        """
        res: dict[tuple[int, ...], list[str]] = defaultdict(list)

        for string in strs:
            code = [0] * 26

            for letter in string:
                code[ord(letter.lower()) - ord('a')] += 1
            res[tuple(code)].append(string)
        return list(res.values())
    





