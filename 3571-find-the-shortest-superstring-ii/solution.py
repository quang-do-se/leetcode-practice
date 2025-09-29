class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        if len(s1) < len(s2):
            shorter = s1
            longer = s2
        else:
            shorter = s2
            longer = s1

        if shorter in longer:
            return longer
        
        shared_head = ""
        temp_a = ""
        temp_b = ""
        for i in range(len(shorter)):
            temp_a += shorter[i]
            temp_b = longer[-i - 1] + temp_b
            if temp_a == temp_b:
                shared_head = temp_a

        shared_tail = ""
        temp_a = ""
        temp_b = ""
        for i in range(len(shorter)):
            temp_a = shorter[-i - 1] + temp_a
            temp_b += longer[i]
            if temp_a == temp_b:
                shared_tail = temp_a

        if len(shared_head) > len(shared_tail):
            return (
                longer[0 : len(longer) - len(shared_head)]
                + shared_head
                + shorter[len(shared_head) :]
            )
        else:
            return (
                shorter[0 : len(shorter) - len(shared_tail)]
                + shared_tail
                + longer[len(shared_tail) :]
            )


sol = Solution()
print(sol.shortestSuperstring("abc", "bcda") == "abcda")
print(sol.shortestSuperstring("bcda", "abc")  == "abcda")
print(sol.shortestSuperstring("a", "a") == "a")
print(sol.shortestSuperstring("a", "b") == "ba")
print(sol.shortestSuperstring("b", "abc") == "abc")
print(sol.shortestSuperstring("gwb", "slfg") == "slfgwb")
print(sol.shortestSuperstring("kbcdefg", "defghijk") == "kbcdefghijk")
print(sol.shortestSuperstring("abcd", "cdea") == "abcdea")
print(sol.shortestSuperstring("m", "azmvzfh") == "azmvzfh")