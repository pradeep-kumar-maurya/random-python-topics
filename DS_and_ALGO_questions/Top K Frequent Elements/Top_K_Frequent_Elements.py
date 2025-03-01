from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1st: Maintain a frequency dict to record the frequency of all the numbers in nums array.
        2nd: Also, maintain the greatest frequency seen among all the frequencies.
        3rd: Reverse the frequency dict i.e. for multiple same frequencies, the value will be an array of all the numbers that has
             that frequency.
        4th: Use a while loop and keep on decrementing the greatest frequency by 1 and keep on searching it within the reversed dict.
             As soon as we get top k elements, return the ans array.
        '''
        map = {}
        reverse_map = {}
        greatest_frequency = 0
        temp_count = 0
        ans = []

        for num in nums:
            if map.get(num) is None:
                map[num] = 0
            else:
                map[num] += 1
            
            if map[num] > greatest_frequency:  # finding the greatest frequency
                greatest_frequency = map[num]

        for key, value in map.items():  # reversing the map dict
            if reverse_map.get(value) is None:
                reverse_map[value] = [key]
            else:
                reverse_map[value].append(key)

        while greatest_frequency >= 0:  # decrementing greatest_frequency by 1
            if reverse_map.get(greatest_frequency):
                data = reverse_map.get(greatest_frequency)

                for num in data:
                    ans.append(num)
                    temp_count += 1
                    if temp_count == k:  # when k == temp_count, return ans array
                        return ans
    
            greatest_frequency -= 1
        
        return ans


s = Solution()
print(s.topKFrequent(nums = [0], k = 2))
