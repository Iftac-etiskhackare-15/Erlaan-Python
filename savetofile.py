namn=input("Vad heter du? ")
color=input("Vilken är din favoritfärg? ")
with open('namncolor.txt', 'a') as file_object:
    file_object.write(namn + ", " + color + "\n" )

with open('namncolor.txt') as file:
    for line in file.readlines():
        line=line.rstrip()
        info=line.split(',')
        print(info[0] + "s favoritfär är" + info[1])