def trivia_fetch(num):
    trivia = {"number": num, "text": "Agrega un numero"}

    if num == 10:
        trivia["text"] = "¿Cual es la suma de los primeros cuatro numeros enteros positivos mas el numero cero?"

    return trivia


def main():
    numero = int(input("ingresa un numero"))
    trivia = trivia_fetch(numero)
    print(trivia)


if __name__ == "__main__":
    main()