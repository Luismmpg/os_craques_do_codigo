import os
import random

forca_torre = [
    """
_ _ __ _ _ _ _ _
|               |
|    	  _     |    _
|    	 |_| _ _ _ _|_|
|   	 |_ _ _ _ _ _ |
|        |_ _ _ _ _ _ |
|   	_|_ _ _ _ _ _ |_
|      |_ _ _ _ _ _ _ _ |
|      |_ _ _ _ _ _ _ _ |
|      |_ _ _ _ _ _ _ _ |
|     _|_ _ _ _ _ _ _ _ |_
|     |_ _ _ _ _ _ _ _ _ _|
|     |_ _ __ _ _ _ _ _ _ |
|___________________________

""",
    """
_ _ __ _ _ _ _ _
|               |
|    	  _     |    _
|    	 |_| _ _ _ _|_|
|   	 |_ _ _ _ _ _ |
|        |_ _ _ _ _ _ |
|   	_|_ _ _ _ _ _ |_
|      |_ _ _ _ _ _ _ _ |
|      |_ _ _ _ _ _ _ _ |
|      |_ _ _ _ _ _ _ _ |
|      |_ _ _ _ _ _ _ _ |
|     
|    
|___________________________

""",
    """
_ _ __ _ _ _ _ _
|               |
|    	  _     |    _
|    	 |_| _ _ _ _|_|
|   	 |_ _ _ _ _ _ |
|        |_ _ _ _ _ _ |
|   	_|_ _ _ _ _ _ |_
|      |_ _ _ _ _ _ _ _ |
|      |_ _ _ _ _ _ _ _ |
|  	   
|     
|     
|     
|___________________________

""",
    """
_ _ __ _ _ _ _ _
|               |
|    	  _     |    _
|    	 |_| _ _ _ _|_|
|   	 |_ _ _ _ _ _ |
|        |_ _ _ _ _ _ |
|   	 |_ _ _ _ _ _ |
|      
|      
|  	   
|    
|     
|     
|___________________________

""",
    """
_ _ __ _ _ _ _ _
|               |
|         _     |    _
|    	 |_| _ _ _ _|_|
|   	 |_ _ _ _ _ _ |
|        
|   
|      
|      
|  	   
|     
|     
|     
|___________________________

""",
    """
_ _ __ _ _ _ _ _
|               |
|    	        |    
|    	 
|   	 
|        
|   	
|      
|      
|  	   
|     
|     
|     
|___________________________

""",
]

tentativas = 5
fase_forca = 6
letras_utilizadas = []
palavra_secreta = ""
continuar = False

print()
print("Os Craques do Código apresentam:")
print()
print(":::::: O Jogo da Forca - Versão Torre de Belém ::::::")

print(forca_torre[5])

print("Escolha o modo de jogo:")
print("1. Palavra secreta escolhida aleatóriamente de uma lista.")
print("2. Palavra secreta à sua escolha.")
print()

lista_palavras = [
    "bitaite",
    "relogio",
    "garrafa",
    "esternocleidomastoideu",
    "otorrinolaringologista",
    "pinguim",
    "python",
]

escolha = input("Introduza 1 ou 2 para escolher o modo de jogo: ")

while continuar == False:
    if escolha == "1":
        palavra_secreta = random.choice(lista_palavras)
        continuar = True
        os.system("cls")
        print("Optou por jogar com uma palavra aleatoria.")
        print()
    elif escolha == "2":
        os.system("cls")
        print("Optou por jogar com uma palavra escolhida por si.")
        print()
        palavra_secreta = input("Escreva uma palavra a ser adivinhada: ").lower()
        continuar = True
        os.system("cls")
    else:
        continuar = False
        escolha = input("Esse número não é válido, escolha 1 ou 2: ")

while tentativas > 0:
    letras_certas = 0
    print()
    adivinha_a_letra = input("Adivinhe uma letra: ").lower()
    print()
    if adivinha_a_letra in letras_utilizadas:
        print("Essa letra já foi usada, tente de novo.")
        print("Letras usadas:", letras_utilizadas)
        print()
        continue
    else:
        letras_utilizadas.append(adivinha_a_letra)
        if adivinha_a_letra not in palavra_secreta:
            tentativas -= 1
            fase_forca -= 1
            print(forca_torre[fase_forca - 1])
            print("Essa letra não está na palavra, restam", tentativas, "tentativas!")
            print()
            print("Letras usadas:", letras_utilizadas)
        if tentativas == 0:
            print()
            print("Você perdeu, esgotou as 5 tentativas.")
            print("A palavra secreta era:", palavra_secreta)
            print()
            break

    for letra in palavra_secreta:
        if letra in letras_utilizadas:
            print(letra, end=" ")
            letras_certas += 1
        else:
            print("_", end=" ")

    if letras_certas == len(palavra_secreta):
        print()
        print("Parabéns, você acertou a palavra e ganhou o jogo!")
        print()
        break
