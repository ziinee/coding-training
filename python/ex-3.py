# 따옴표 출력

txt = ""
speaker = ""

while (txt == ""):
    txt = input("What is the quote?")

while (speaker == ""):
    speaker = input("Who said it?")

print(speaker + " says, \"" + txt + ".\"")
