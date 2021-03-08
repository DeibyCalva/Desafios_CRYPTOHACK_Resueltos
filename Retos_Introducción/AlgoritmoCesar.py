# -*- coding: utf-8 -*-
"""

@author: leonardo
"""

def main():
    TextoPlano = input("Introducir Mensaje: ") 
    desplazamiento  = int(input("numero de desplazamiento: "))
    modoSeguridad    = input("Para cifrar pulse c   ....Para descifrar puse  d ")
   

    if modoSeguridad.lower().startswith('c'):
        modoSeguridad = "cifrar"
    elif modoSeguridad.lower().startswith('d'):
        modoSeguridad = "descifrar"

    Textocifrado = encriptar(TextoPlano, desplazamiento, modoSeguridad)
    if modoSeguridad ==   "cifrar":
        print(("Mensaje Cifrado:", Textocifrado))
    elif modoSeguridad == "descifrar":
        print(("Mensaje Descifrado:", Textocifrado)) 
        
        
def encriptar(texto, despl, modo):
    
    Texto= texto.upper()
    imprimeTexto = ""
    abecedario    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letra in Texto:
        if letra in abecedario:
            num = abecedario.find(letra)
            if modo ==   "cifrar":
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
    input()
