class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency table
        # Sort by values
        # Return k keys

        # Time: O(n + nlogn + k) -> O(nlogn + k)
        # Space: O(m) - unique values

        freqs = {}
        for el in nums:
            freqs[el] = freqs.get(el, 0) + 1
        
        freqs = dict(sorted(freqs.items(), key=lambda item: item[1]))
        print(freqs)
        final = list(freqs.keys())[-k:]
        return final
            