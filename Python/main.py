import math
from func import soma, sub, divisao, mult, finalizar


if __name__ == "__main__" :
   
    fim = False
    while fim == False :
        operador = input("------\nqual operação deseja fazer:\n'+' para soma\n'-' para subtração\n'/' para divisão\n'*' para multiplicação\n'x' para finalizar\nOpção: ")
        match operador:
            case "+":
                soma()  
                finalizar(fim)
            case "-":
                sub()
                finalizar(fim)
            case "/":
                divisao()
                finalizar(fim)
            case "*":
                mult()
                finalizar(fim)

            case "x":
                fim = True
            case _ :
                print("Operador invalido, tente novamente.")


