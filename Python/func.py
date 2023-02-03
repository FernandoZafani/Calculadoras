import math

def soma() :
     num1 = float(input("------\n_ + ? =\nPrimeiro número: "))
     num2 = float(input(f"{num1} + _ =\nSegundo número: "))
     return(print(f'{num1} + {num2} = {num1 + num2}'))

def sub() :
    num1 = float(input("------\n_ - ? =\nPrimeiro número: "))
    num2 = float(input(f"{num1} - _ =\nSegundo número: "))
    return(print(f'{num1} - {num2} = {num1 - num2}'))

def divisao() :
    num1 = float(input("------\n_ / ? =\nPrimeiro número: "))
    test = False
    while test == False :
        num2 = float(input(f"{num1} / _ =\nSegundo número: "))
        if num2 != 0 :
            test = True
        else :
            print("invalido.")
    return(print(f'{num1} / {num2} = {round(num1 / num2,2)}'))
        
def mult() :
    num1 = float(input("------\n_ x ? =\nPrimeiro número: "))
    num2 = float(input(f"{num1} x _ =\nSegundo número: "))
    return(print(f'{num1} x {num2} = {round(num1 * num2),2}'))
    

            
