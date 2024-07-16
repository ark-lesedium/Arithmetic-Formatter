import re

def arithmetic_arranger(problems, my_answer=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    first = ''
    second = ''
    lines = ''
    sumx = ''
    string = ''

    for problem in problems:
        if re.search("[^\s0-9.+-]", problem):
            if re.search("[/]", problem) or re.search("[*]", problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        firstNumber, operator, secondNumber = problem.split(" ")

        if len(firstNumber) >= 5 or len(secondNumber) >= 5:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            sum_result = str(int(firstNumber) + int(secondNumber))
        elif operator == "-":
            sum_result = str(int(firstNumber) - int(secondNumber))
        else:
            return "Error: Operator must be '+' or '-'."

        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)
        line = '-' * length
        res = str(sum_result).rjust(length)

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

    if my_answer:
        string = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        string = first + '\n' + second + '\n' + lines

    return string
