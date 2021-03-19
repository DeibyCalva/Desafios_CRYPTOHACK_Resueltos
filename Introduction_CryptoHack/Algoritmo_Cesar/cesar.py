import recorrido as en
TextoPlano = input("Introducir Mensaje: ")
desplazamiento  = int(input("numero de desplazamiento: "))
modoSeguridad    = input("Para cifrar pulse c   ....Para descifrar puse  d ")
if modoSeguridad.lower().startswith('c'):
        modoSeguridad = "cifrar"
elif modoSeguridad.lower().startswith('d'):
        modoSeguridad = "descifrar"
Textocifrado = en.encriptar(TextoPlano, desplazamiento, modoSeguridad)
if modoSeguridad ==   "cifrar":
    print(("Mensaje Cifrado:", Textocifrado))
elif modoSeguridad == "descifrar":
    print(("Mensaje Descifrado:", Textocifrado))
        
        

