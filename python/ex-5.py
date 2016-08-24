# 간단한 수학 : 두개의 숫자를 입력 받아 사칙연산 결과를 반환

first = input("What is the first number? ")
second = input("What is the second number? ")

num1 = int(first)
num2 = int(second)

plus = num1 + num2
minus = num1 - num2
multiplication = num1 * num2
division = num1 / num2

txt = first + " + " + second + " = " + str(plus) + '\n'
txt += first + " - " + second + " = " + str(minus) + '\n'
txt += first + " * " + second + " = " + str(multiplication) + '\n'
txt += first + " / " + second + " = " + str(division) + '\n'

print(txt)
