number = int(input("Factorial: "))

def fac(number):    

    if number == 1:
        return number
    else:
        return number * fac(number-1)

print(str(number)+"!","=",fac(number))
