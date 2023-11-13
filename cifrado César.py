def cifrar_cesar(texto, desplazamiento):
    texto_cifrado = ""

    for caracter in texto:
        if caracter.isalpha():
            codigo = ord(caracter)
            es_mayuscula = caracter.isupper()

            if es_mayuscula:
                codigo_base = ord('A')
            else:
                codigo_base = ord('a')

            codigo_cifrado = ((codigo - codigo_base + desplazamiento) % 26) + codigo_base
            caracter_cifrado = chr(codigo_cifrado)

            texto_cifrado += caracter_cifrado
        else:
            texto_cifrado += caracter

    return texto_cifrado


texto_original = input("Ingresa el texto a cifrar: ")
desplazamiento = int(input("Ingresa el número de espacios para cifrar: "))

texto_cifrado = cifrar_cesar(texto_original, desplazamiento)
print("Texto cifrado:", texto_cifrado)
