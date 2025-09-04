from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operants = []
        operators = set(["+", "-", "*", "/"])

        for t in tokens:
            if t in operators:
                b = operants.pop()
                a = operants.pop()

                if t == "+":
                    r = a + b
                elif t == "-":
                    r = a - b
                elif t == "*":
                    r = a * b
                else:
                    r = int(a / b)

                operants.append(r)
            else:
                operants.append(int(t))

        return operants[0]


sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]) == 9)
print(sol.evalRPN(["4","13","5","/","+"]) == 6)
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22)