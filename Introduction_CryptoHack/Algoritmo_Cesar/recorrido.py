def encriptar(texto, despl, modo):
    Texto = texto.upper()
    imprimeTexto = ""
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letra in Texto:
        if letra in abecedario:
            num = abecedario.find(letra)
            if modo == "cifrar":
                num = num + despl
            elif modo == "descifrar":
                num = num - despl

            if num >= len(abecedario):
                num -= len(abecedario)
            elif num < 0:
                num += len(abecedario)

            imprimeTexto += abecedario[num]
        else:
            imprimeTexto += letra
    return imprimeTexto
