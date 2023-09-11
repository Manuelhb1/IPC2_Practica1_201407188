from nodo import Nodo

class ListaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0


    def vacia(self):
        return self.primero == None
    

    def agregarFinal(self, dato):   #Ejemlo 5->8->15->6->3 el 3 es el ultimo que se ingreso
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.tamanio += 1

    
    def agregarInicio(self, dato):  #Ejemlo 5->8->15->6->3 el 5 es el ultimo que se ingreso
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.tamanio +=1
        
    
    def recorrerInicioFin(self):  #No imprime objetos a menos que se especifique el atributo
        
        aux = self.primero
        if self.vacia():
            print("Lista vacia")

        while aux:            
            print(aux.dato)  
            aux = aux.siguiente
            #return aux.dato
            
    
    def recorrerFinInicio(self):
        aux = self.ultimo

        if self.vacia():
            print("Lista vacia")

        while aux:        
            print(aux.dato)              
            aux = aux.anterior

    
    def buscarPosicion(self, posicion):    #---------Busca un dato por su posicion iniciando en 0, por insercion al inicio

        if self.vacia():
            return "Lista vacia"
        
        aux = self.primero        
        posList = 0
        while aux:
                                        
            if posList == posicion:
                return aux.dato
            
            posList += 1 
            aux = aux.siguiente


    def buscarDato(self, dato):            #---------Busca un dato por su posicion iniciando en 0, por insercion al inicio devuelve una lista de las posiciones donde ser repite el dato buscado
        listaRetorno = ListaDoble()

        vacia = False
                   
        aux = self.primero        
        posList = 0
        while aux:
                                        
            if dato == aux.dato:                
                listaRetorno.agregarFinal(posList) 
                vacia = True
            
            posList += 1 
            aux = aux.siguiente

        if self.vacia() or vacia == False:
            return False
        else:
            return listaRetorno 
        

    def quitarRepetidos(self): 
        listaRetorno = ListaDoble()

        aux = self.primero
        while aux:

            if listaRetorno.vacia():
                listaRetorno.agregarFinal(aux.dato)
                
            else:                

                if listaRetorno.buscarDato(aux.dato) == False:
                    listaRetorno.agregarFinal(aux.dato)        
                                   
            aux = aux.siguiente
       
        return listaRetorno
    

    def eliminarInicio(self):
        if self.vacia():
            print("Lista vacia")

        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.tamanio = 0
        
        else: 
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.tamanio -= 1
         
    
    def eliminarFinal(self):
        if self.vacia():
            print("Lista vacia")

        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.tamanio = 0
        
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.tamanio -= 1


    def eliminarPosicion(self, posicion):
        if self.vacia():
            print("Lista vacia")            
               
        aux = self.primero
        posList = 0

        if posicion == 0:
            self.eliminarInicio() 
                        

        elif posicion == self.tamanio-1:
            self.eliminarFinal()
                
        
        while aux:
            if posList == posicion:
                
                aux.anterior.siguiente = aux.siguiente
                aux.siguiente.anterior = aux.anterior
                self.tamanio -=1
                            
            posList += 1 
            aux = aux.siguiente

    
    def modificarPosicion(self, posicion, datoN):
        aux = self.primero
        posList = 0
        
        while aux:

            if posList == posicion:
                aux.dato = datoN            
           
            posList += 1
            aux = aux.siguiente

    
    def vaciarLista(self):
        for x in range(self.tamanio):
            self.eliminarFinal()
        self.tamanio = 0

    
