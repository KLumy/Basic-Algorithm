import re
from collections import deque


def solution(expression):
    priorities = ["*-+", "*+-", "-*+", "-+*", "+-*", "+*-"]
    expression = re.split(r"([+]|[-]|[*])", expression)

    def calc(exp, priority):

        new_exp = exp[:]
        for op in priority:
            temp_exp = []
            i = 0
            while i < len(new_exp):
                if new_exp[i] == op:
                    x, y = int(temp_exp[-1]), int(new_exp[i + 1])
                    if op == "*":
                        temp_exp[-1] = str(x * y)
                    if op == "-":
                        temp_exp[-1] = str(x - y)
                    if op == "+":
                        temp_exp[-1] = str(x + y)
                    i += 1
                else:
                    temp_exp.append(new_exp[i])
                i += 1
            new_exp = temp_exp
        return int(new_exp[0])

    answer = -1
    for p in priorities:
        answer = max(answer, abs(calc(expression, p)))
    return answer


# def solution(expression):
#     priorities = ["*-+", "*+-", "-*+", "-+*", "+-*", "+*-"]
#     expression = re.split(r"([+]|[-]|[*])", expression)

#     def calc(exp, p):

#         operator = []
#         operand = []

#         for e in exp:
#             if e.isdigit():
#                 operand.append(int(e))
#             else:
#                 if not operator:
#                     operator.append(e)
#                     continue
#                 while operator and (p.find(operator[-1]) > p.find(e)):
#                     y = operand.pop()
#                     x = operand.pop()
#                     op = operator.pop()
#                     if op == "*":
#                         operand.append(x * y)
#                     elif op == "+":
#                         operand.append(x + y)
#                     elif op == "-":
#                         operand.append(x - y)
#                 operator.append(e)

#         while operand and operator:
#             y = operand.pop()
#             x = operand.pop()
#             op = operator.pop()
#             if op == "*":
#                 operand.append(x * y)
#             elif op == "+":
#                 operand.append(x + y)
#             elif op == "-":
#                 operand.append(x - y)

#         return operand[0]

#     answer = -1
#     for p in priorities:
#         answer = max(answer, abs(calc(expression, p)))
#     return answer


if __name__ == "__main__":
    i = "100-200*300-500+20"
    print(solution(i))
