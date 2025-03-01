class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        The idea is to maintain two dictionaries i.e. one for s1 and one for s2.
        We will be iterating over string s2 and keep a track of all the consecutive
        chars in the s2_dict and also keep on comparing it with the s1_dict.
        '''
        s1_dict = {}
        s2_dict = {}
        i = -1  # used for iterating and removing elements
        j = -1  # point from where i must start

        for char in s1:  # create s1_dict
            if s1_dict.get(char) is None:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1
        
        for char in s2:
            j += 1
            # if the char is not in s1_dict, initialize s2_dict to {}
            if s1_dict.get(char) is None:
                s2_dict = {}
                i = j  # V.Imp: i must be set to j if char is not in s1_dict
                continue

            else:                
                if s2_dict.get(char) is None:  # add the char in s2_dict if not there
                    s2_dict[char] = 1
                else:
                    s2_dict[char] += 1  # increment if already there in s2_dict
                
                '''
                If count of a char increases than expected, then iterate from left to right and
                keep on subtracting the frequencies of the chars in the s2_dict until the current
                char frequency becomes same as that in s1_dict.
                '''
                if s2_dict.get(char) > s1_dict.get(char):

                    while i < len(s2):    
                        i += 1
                        
                        if s2_dict.get(s2[i]):
                            s2_dict[s2[i]] -= 1  # decrement freq

                            if s2_dict[s2[i]] == 0:  # if freq is 0 then remove it from s2_dict
                                s2_dict.pop(s2[i])
                        
                        if s2_dict[char] == s1_dict[char]:  # break once freq is same in s1_dict and s2_dict
                            break
                    
                if s1_dict == s2_dict:  # T.C = O(26)
                    return True

        return False
    

s = Solution()
print(s.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
