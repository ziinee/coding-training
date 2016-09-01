# 피자 파티

input1 = input("How many people? ")
input2 = input("How many pizzas do you have? ")
input3 = input("How many pieces are in a pizza? ")

def convert_int(s):
    try:
        float(s)
        return int(s)
    except ValueError:
        print("Error! Please input a numeric value")
        return False

people = convert_int(input1)
pizza = convert_int(input2)
peices = convert_int(input3)

per_pizza = int(pizza*peices/people)
left_pizza = pizza*peices%people

txt = input1 + " people with " + input2 + " pizzas\n"
txt += "Each person gets " + str(per_pizza) + " of pizza.\n"
txt += "There are " + str(left_pizza) + " leftover pieces."

print(txt)
