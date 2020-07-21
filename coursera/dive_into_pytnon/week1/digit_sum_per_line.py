import sys


while True:
    digit_string = sys.argv[1]
    result = 0
    if digit_string != "":
        for i in digit_string:
            t = int(i)
            if type(t) is int:
                result += t
            else:
                continue
        print(result)
        break
    else:
        print("Введите строку!")
        continue
