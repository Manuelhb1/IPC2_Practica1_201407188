from colorama import Fore, Style, Back, init
from listaDoble import ListaDoble
import time
from os import system


class Principal:

    def __init__(self, matriz = None):
        self.matriz = matriz

    def limpiar(self):
        system("cls")   

    def crearTablero(self, filas, columnas):

        self.matriz = ListaDoble()
        for x in range(filas):
            fila = ListaDoble()
            
            for y in range(columnas):                                 
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

            color = f"""{Fore.BLUE}A{Style.RESET_ALL}"""
            nuevoT.matriz.buscarPosicion(fila).modificarPosicion(columna,color)

        elif color.upper() == "ROJO" or color.upper() == "R":

            color = f"""{Fore.RED}R{Style.RESET_ALL}"""
            nuevoT.matriz.buscarPosicion(fila).modificarPosicion(columna,color)

        elif color.upper() == "VERDE" or color.upper() == "V":

            color = f"""{Fore.GREEN}V{Style.RESET_ALL}"""
            nuevoT.matriz.buscarPosicion(fila).modificarPosicion(columna,color)    

        elif color.upper() == "PURPURA" or color.upper() == "P":

            color = f"""{Fore.MAGENTA}P{Style.RESET_ALL}"""
            nuevoT.matriz.buscarPosicion(fila).modificarPosicion(columna,color) 

        elif color.upper() == "NARANJA" or color.upper() == "N":

            color = f"""{Fore.YELLOW}N{Style.RESET_ALL}"""
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
        pass





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
                regresar = False
                
    elif int(opcion) == 2:
        nuevoT.logo()
        nuevoT.mostrarDatos()
    elif int(opcion) == 3:
        exit()
    else:
        print("Ingresa una opcion correcta")       
            



