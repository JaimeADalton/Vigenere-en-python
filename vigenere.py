#!/usr/bin/python
#-*- coding: utf-8 -*-
# CIFRADO VIGENERE. 
#

alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890|@#~{[]}\!"$%&/()=?^*_:;,.-+`<> '
def vigenere(texto,clave):
    cifrado = ''
    for letra in range(len(texto)):
        cifrado += alfa[(alfa.index(texto[letra])+alfa.index(clave[letra%len(clave)]))%len(alfa)]
    return cifrado

def des_vigenere(texto_encriptado,clave):
    texto = ''
    for letra in range(len(texto_encriptado)):
        texto += alfa[(alfa.index(texto_encriptado[letra])-alfa.index(clave[letra%len(clave)]))%len(alfa)]
    return texto
    
def main():
    c = str(raw_input("Introduce cadena a cifrar: ")).lower()    # PARA QUE SIEMPRE LA CONVIERTA A MINUSCULA
    clave = str(raw_input("Introduce clave: ")).lower() 
    print vigenere(c, clave)
    print

    c = str(raw_input("Introduce cadena a descifrar: ")).lower()    # PARA QUE SIEMPRE LA CONVIERTA A MINUSCULA
    clave = str(raw_input("Introduce clave: ")).lower()
    print des_vigenere(c, clave) 
    print

if __name__ == "__main__"
    main()
