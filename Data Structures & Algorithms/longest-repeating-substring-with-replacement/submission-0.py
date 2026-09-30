class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window_length - most_frequent_count <= k    
        counts ={}
        maxLength = 0
            

        l = 0


        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            window_len = r-l + 1
            most_frequent_count = max(counts.values())
            replacements = window_len - most_frequent_count

            while replacements > k:
                counts[s[l]] -= 1
                l += 1

                window_len = r-l + 1

                most_frequent_count = max(counts.values())
                replacements = window_len - most_frequent_count

            maxLength = max(maxLength, r - l + 1)
        return maxLength
                             
