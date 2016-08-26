# 퇴직 계산기

import time

input1 = input("What is your current age? ")
input2 = input("At what age would you like to retire? ")
str_year = time.strftime("%Y")

age = int(input1)
retire_age = int(input2)
year = int(str_year)

left_year = str(retire_age - age)
retire_year = str(age + year)

txt = "You have " + left_year + " years left until you can retire. \n"
txt += "It's " + str_year + ", so you can retire in " + retire_year
print(txt)
