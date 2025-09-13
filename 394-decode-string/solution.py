class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = 0
        res = ""

        for c in s:
            if c.isnumeric():
                n = n * 10 + int(c)
                continue
            if c == '[':
                stack.append(str(n))
                n = 0
                continue
            if c == ']':
                expand = ""                
                while not stack[-1].isnumeric():
                    expand = stack.pop() + expand

                repeat = int(stack.pop())

                expand = expand * repeat      

                if stack:
                    stack.append(expand)
                else:
                    res += expand

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