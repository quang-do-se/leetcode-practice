class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = 0
        res = ""

        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
                continue
            if c == '[':
                stack.append(str(n))
                n = 0
                continue
            if c == ']':
                expanded_string = ""                
                while not stack[-1].isnumeric():
                    expanded_string = stack.pop() + expanded_string

                repeat = int(stack.pop())

                expanded_string = expanded_string * repeat      

                if stack:
                    stack.append(expanded_string)
                else:
                    res += expanded_string

                continue

            if stack:
                stack.append(c)
            else:
                res += c

        return res



sol = Solution()
print(sol.decodeString("10[a]") == "aaaaaaaaaa")
print(sol.decodeString("a") == "a")
print(sol.decodeString("3[a]2[bc]") == "aaabcbc")
print(sol.decodeString("3[a2[c]]xyz10[d]uuu") == "accaccaccxyzdddddddddduuu")
print(sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")