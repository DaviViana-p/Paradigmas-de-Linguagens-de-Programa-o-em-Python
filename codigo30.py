while True:
    try:
        x = int(input("digite um numero"))
        break
    except ValueError:
        print("digite um numero valido")