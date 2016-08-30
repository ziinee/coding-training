# 직사각형 방의 면적 

input1 = input("What is the lenght of the room in feet? ")
input2 = input("Whiat is the width of the room in feet? ")

length = int(input1)
width = int(input2)

txt = "You entered dimensions of " + input1 + " feet by " + input2 + " feeet\n"

area = length * width
area_meters = area * 0.09290304

txt += "The area is\n"
txt += str(area) + "square feet\n"
txt += str(area_meters) + "square meters"

print(txt)
