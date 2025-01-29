from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s = "Fizz"
            if i % 5 == 0:
                s += "Buzz"

            if s == "":
                answer.append(str(i))
            else:
                answer.append(s)
                
        return answer