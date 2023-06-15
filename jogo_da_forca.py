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
letras_utilizadas =[]
palavra_secreta = ""
continuar = False

print()
print("Os Craques do Código apresentam:")
print()
print(":::::: O Jogo da Forca - Versão Torre de Belém ::::::")

print(forca_torre[5])

print("Escolha o modo de jogo:")
print("1. Palavra secreta escolhida aleatóriamente de uma lista")
print("2. Palavra secreta à sua escolha")
print()

lista_palavras = ["bitaite", "relogio", "garrafa", "esternocleidomastoideu","otorrinolaringologista", "pinguim", "python"]

escolha = input("Introduza 1 ou 2 para escolher o modo de jogo")
