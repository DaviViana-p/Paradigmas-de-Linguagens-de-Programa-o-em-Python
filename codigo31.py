def dividir(x, y):
    try:
        resultado = x / y
        print("a resposta é :", resultado)
    except ZeroDivisionError:
        print("divisao por zero")

dividir(int(input("digite um numero")), int(input("digite um numero")))