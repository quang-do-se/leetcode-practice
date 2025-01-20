from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        size = len(chars)
        group_char = None
        next_index = 0
        group_count = 0

        for i in range(size):
            if group_char is None:
                next_index = i + 1
                group_char = chars[i]
                group_count = 1
            elif chars[i] == group_char:
                group_count += 1
            else:
                if group_count > 1:
                    group_count_str = str(group_count)

                    for c in group_count_str:
                        chars[next_index] = c
                        next_index += 1

                chars[next_index] = chars[i]
                group_char = chars[i]
                group_count = 1
                next_index += 1

        if group_count > 1:
            group_count_str = str(group_count)

            for c in group_count_str:
                chars[next_index] = c
                next_index += 1

        return next_index


sol = Solution()

input = ["a","a","b","b","c","c","c"]
print(input[:sol.compress(input)] == ["a", "2", "b", "2", "c", "3"])

input = ["a"]
print(input[:sol.compress(input)] == ["a"])

input = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c"]
print(input[:sol.compress(input)] == ["a","b","1","2","c"])