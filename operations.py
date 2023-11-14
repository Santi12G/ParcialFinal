def caracter_a_ascii(caracter):
    return ord(caracter)

def ascii_a_binario(ascii):
    return bin(ascii)[2:]

def concatenar_resultados(resultado_ascii, resultado_binario):
    return f"ASCII: {resultado_ascii} | Binario: {resultado_binario}"

def main():
    caracter = input("Introduzca un carácter: ")
    resultado_ascii = caracter_a_ascii(caracter)
    resultado_binario = ascii_a_binario(resultado_ascii)
    print(concatenar_resultados(resultado_ascii, resultado_binario))

if __name__ == "__main__":
    main()
