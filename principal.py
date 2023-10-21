from colorama import Fore, Style, Back, init
from listaDoble import ListaDoble
import time
from os import system
import os


class Principal:

    def __init__(self, matriz = None, alto = None, ancho = None):
        self.matriz = matriz
        self.ancho = ancho
        self.alto = alto

    def limpiar(self):
        system("cls")   

    def crearTablero(self, filas, columnas):
        self.alto = filas
        self.ancho = columnas
        self.matriz = ListaDoble()
        for x in range(self.ancho):
            fila = ListaDoble()
            
            for y in range(self.alto):                                 
                fila.agregarFinal("■")
            self.matriz.agregarFinal(fila)
        
        self.mostrarMatriz()
        print("\nTablero creado correctamente.")

    def mostrarMatriz(self):
        #print("")
        for x in range(nuevoT.matriz.tamanio):                
            for y in range(nuevoT.matriz.buscarPosicion(x).tamanio):               
                print(nuevoT.matriz.buscarPosicion(x).buscarPosicion(y), end=" ")
            print("")

    def ingresarColores(self, fila, columna, color):

        if color.upper() == "AZUL" or color.upper() == "A":

            color = "A"
            nuevoT.matriz.buscarPosicion(fila).modificarPosicion(columna,color)

        elif color.upper() == "ROJO" or color.upper() == "R":

            color = "R"
            nuevoT.matriz.buscarPosicion(fila).modificarPosicion(columna,color)

        elif color.upper() == "VERDE" or color.upper() == "V":

            color = "V"
            nuevoT.matriz.buscarPosicion(fila).modificarPosicion(columna,color)    

        elif color.upper() == "PURPURA" or color.upper() == "P":

            color = "P"
            nuevoT.matriz.buscarPosicion(fila).modificarPosicion(columna,color) 

        elif color.upper() == "NARANJA" or color.upper() == "N":

            color = "N"
            nuevoT.matriz.buscarPosicion(fila).modificarPosicion(columna,color)

    def logo(self):
        
        color = f"""\n------------------------{Fore.BLUE}C{Style.RESET_ALL}"""
        color = color + f"""{Fore.RED}o{Style.RESET_ALL}"""           
        color = color + f"""{Fore.GREEN}l{Style.RESET_ALL}"""            
        color = color + f"""{Fore.MAGENTA}o{Style.RESET_ALL}""" 
        color = color + f"""{Fore.YELLOW}r{Style.RESET_ALL}"""
        color = color + f"""{Fore.BLUE}é{Style.RESET_ALL}"""
        color = color + f"""{Fore.RED}a{Style.RESET_ALL}"""           
        color = color + f"""{Fore.GREEN}l{Style.RESET_ALL}"""            
        color = color + f"""{Fore.MAGENTA}o{Style.RESET_ALL}------------------------\n"""    

        print(color)
        
    def mostrarDatos(self):

        

        nombre = f'''\n*******************************************
|                                         |
|   - 201407188                           |
|   - Werner Manuel Hernandez Bonilla     |
|   - Introduccion a la programacion      |
|     y computacion 2                     |           
|   - Seccion D                           |
|                                         |
*******************************************\n'''
        
        print(nombre)

    def graficar(self):

        graficod = """digraph grafo{\n
        node[shape=circle];\n"""
        
        n =f'''n0 [label="Guatematel\nColorealo"];\n''' 

        enlace = ''
        num = 1


        #Creando los nodos ----------------
        for y in range(self.alto+1):
            for z in range(self.ancho+1):

                if y == 0:
                    n = n + f'''n{num} [label="{z}"];\n'''
            
                else:
                    if z == 0:    
                        n = n + f'''n{num} [label="{y}"];\n'''
                    else:
                        if self.matriz.buscarPosicion(y-1).buscarPosicion(z-1)=="A":
                            n = n + f'''n{num} [label="" fillcolor="#0000ff" style=filled];\n'''              
                        elif self.matriz.buscarPosicion(y-1).buscarPosicion(z-1)=="R":
                            n = n + f'''n{num} [label="" fillcolor="#ff0000" style=filled];\n'''
                        elif self.matriz.buscarPosicion(y-1).buscarPosicion(z-1)=="V":
                            n = n + f'''n{num} [label="" fillcolor="#3EE300" style=filled];\n'''
                        elif self.matriz.buscarPosicion(y-1).buscarPosicion(z-1)=="P":
                            n = n + f'''n{num} [label="" fillcolor="#630b57" style=filled];\n'''
                        elif self.matriz.buscarPosicion(y-1).buscarPosicion(z-1)=="N":
                            n = n + f'''n{num} [label="" fillcolor="#ff8000" style=filled];\n'''    
                        else:
                            n = n + f'''n{num} [label=""];\n'''
                num+=1

        actual = 1
        
        #Creando los enlaces ------------Matriz cuadrada MxM

        if self.alto == self.ancho:
            pass
        elif self.ancho > self.alto:
            pass
        else:
            pass






        for y in range(self.alto+2): 
            actual = y
            siguiente = actual + (self.alto + 1)

            for z in range(self.ancho+1):

                #------Evita que los enlaces se salgan de rango y si y != 0 no se enlaza de la misma manera  
                if z == self.alto and y != 0:
                    break  

                #En y = 0 tiene que enlazar el nodo0 con la primera fila
                if y == 0:                    
                    enlace = enlace + f'''n{y} -> n{z+1}\n'''                  
                                                      
                else: 

                    enlace = enlace + f'''n{actual} -> n{siguiente}\n'''
                              
                actual = actual + (self.alto + 1)
                siguiente = siguiente + (self.alto + 1)


        """for y in range(self.alto+2):
            actual = y
            siguiente = actual"""






        
        graf = graficod + n +  enlace+"\n}"
        
        
        with open('grafica.dot', 'w') as f:
            f.write(graf)
        os.system('dot -Tpdf grafica.dot -o grafica.pdf')




menu = f'''\n\n+-----------------------------------------+
|                                         |
|   GUATEMATEL                            |
|   COLOREALO                             |
|                                         |
|   Menu:                                 |
|                                         |
|       1. Crear tablero                  |
|       2. Mostrar datos del estudiante   |
|       3. Salir                          |
|                                         |
+-----------------------------------------+\n'''

print(menu)


nuevoT = Principal()

salir = True
opcion = 0 

while salir:
    nuevoT.logo()
    opcion = input("Ingresa una opcion  ")

    if int(opcion) == 1:
        nuevoT.logo()
        colorE = f'''Elige un color:
- AZUL
- ROJO
- VERDE
- PURPURA
- NARANJA'''
        regresar = True
        alto = input("Ingresa el alto del tablero\n")
        ancho = input("Ingresa el ancho del tablero\n")
        nuevoT.logo()
        nuevoT.crearTablero(int(alto),int(ancho))

        nuevoT.logo()
        print(colorE)
        nuevoT.logo()
        color = input("   ")
        
        
        fM = f"""Ingresa una fila donde colocar una pieza: Rango 1-{alto}\n"""
        cM = f"""Ingresa una columna donde colocar una pieza: Rango 1-{ancho}\n"""
        
        nuevoT.logo()
        f = input(fM)
        c = input(cM)
        nuevoT.logo()

        nuevoT.ingresarColores(int(f)-1,int(c)-1,color)
        nuevoT.mostrarMatriz()
        nuevoT.logo()
        
        while regresar:

            atras = input("Deseas colocar otro color (S/N)\n")
            if atras.upper() == "S": 
                nuevoT.logo()     
                color = input("Elige un color\n")
                nuevoT.logo()
                f1=input(fM)
                c1 = input(cM)
                nuevoT.logo()
                nuevoT.ingresarColores(int(f1)-1,int(c1)-1, color)
                nuevoT.mostrarMatriz()
                nuevoT.logo()
                
            if atras.upper() == "N":
                nuevoT.graficar()
                regresar = False
                
    elif int(opcion) == 2:
        nuevoT.logo()
        nuevoT.mostrarDatos()
    elif int(opcion) == 3:
        print("Saliendo...\n")
        exit()
    else:
        print("Ingresa una opcion correcta")       
            



