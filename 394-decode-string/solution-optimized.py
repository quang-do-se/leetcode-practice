class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = 0
        current_string = ""

        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            elif c == "[":
                stack.append(current_string)
                stack.append(n)
                
                current_string = ""
                n = 0
            elif c == "]":
                # Get k - the number of times the string should be repeated
                repeat_count = stack.pop()  # This should be an `int` in a valid pattern
                current_string = current_string * repeat_count

                # Add back the previous string that is before the decoded string
                prev_string = stack.pop()
                current_string =  prev_string + current_string
            else:
                current_string += c

        return current_string


sol = Solution()
print(sol.decodeString("x3[a2[b]]") == "xabbabbabb")
print(sol.decodeString("10[a]") == "aaaaaaaaaa")
print(sol.decodeString("a") == "a")
print(sol.decodeString("3[a]2[bc]") == "aaabcbc")
print(sol.decodeString("3[a2[c]]xyz10[d]uuu") == "accaccaccxyzdddddddddduuu")
print(sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
