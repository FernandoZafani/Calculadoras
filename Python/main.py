import math
from func import soma, sub, divisao, mult, finalizar


if __name__ == "__main__" :
   
    fim = False
    while fim == False :
        operador = input("------\nqual operação deseja fazer:\n'+' para soma\n'-' para subtração\n'/' para divisão\n'*' para multiplicação\n'x' para finalizar\nOpção: ")
        match operador:
            case "+":
                soma()  
               
            case "-":
                sub()
               
            case "/":
                divisao()
                
            case "*":
                mult()
                
            case "x":
                fim = True
            case _ :
                print("Operador invalido, tente novamente.")


