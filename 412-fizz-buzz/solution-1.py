from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        map = {2: "Jazz", 3: "Fizz", 5: "Buzz"}
        answer = []
        for i in range(1, n + 1):
            s = []
            for key in map:
                if i % key == 0:
                    s.append(map[key])

            if s:
                answer.append("".join(s))
            else:
                answer.append(str(i))
                
        return answer
    

sol = Solution()
print(sol.fizzBuzz(42))