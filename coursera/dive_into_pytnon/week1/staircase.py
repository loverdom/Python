import sys



amount = int(sys.argv[1])
num = 0
while amount >= 0:
    spaces = " "*amount
    fig = "#"*num
    if fig != "":
        print(spaces, fig, sep="")
    amount -= 1
    num += 1
