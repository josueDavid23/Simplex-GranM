#Metodo Gran M
#TEC - Costa Rica
#Investigacion de Operaciones
#Kevin Rodriguez - Josue Rodriguez
#I Tarea Programada
from GranM import *
tabla=[[]]
variablesDecision=2
arregloCol=[]#ubicar en tabla u
arregloFilas=["Z"]
arregloZ=[]
#-----------------------------------------------------------
class Z_Aux:
    #Constructor
    def __init__(self,numeroM,numeroSinM,letra):
        self.numeroM= numeroM
        self.numeroSinM=numeroSinM
        self.letra=letra 
#-----------------------------------------------------------
#crear Z
class Z:
    #Constructor
    def __init__(self,arreglo,esMin,u):
        self.esMin= esMin
        self.restricciones=arreglo
        self.u= u

    def crearZ(self):
        global tabla
        self.convertirNulo_ObjetosU()
        for i in range(len(self.u)):
            global arregloZ
            z=Z_Aux(0,self.u[i],"x"+str(i+1))
            arregloZ.append(z)
        sol=Z_Aux(0,0,"SOL")
        arregloZ.append(sol)

    def buscarArreglo(self,identificador):
        global arregloZ
        for x in range(len(arregloZ)):
            if arregloZ[x].letra == identificador:
                return x
        return -1
    
    def imprimeArregloZ(self):
        global arregloZ
        for x in range(len(arregloZ)):
            print("M:"+str(arregloZ[x].numeroM) +"\t Sin M:"+str(arregloZ[x].numeroSinM)+ "\t Letra:"+arregloZ[x].letra)
    
    
    def verificarMinX(self,numero):
        if self.esMin is True:
            return numero*-1
        else: return numero
       
    def agregarRestricciones(self):
        global arregloZ
        for i in range (len(self.restricciones)):
     
             if self.restricciones[i][len(self.restricciones[i])-1]!= "<=":
                 for j in range(len(self.restricciones[i])-2): ## por que los dos ultimos son solucion y simbolo
                     if self.buscarArreglo("x"+str(j+1)) != -1: # si lo encontro devuelve la pos donde esta si no -1
                         numero = self.verificarMinX(self.restricciones[i][j])# si es minimizar lo deja igual
                         arregloZ[self.buscarArreglo("x"+str(j+1))].numeroM+=numero

                 numero = self.verificarMinX(self.restricciones[i][len(self.restricciones[i])-2])# si es minimizar lo multiplica*-1
                 x=self.buscarArreglo("SOL")
                 arregloZ[x].numeroM+=numero
                 
        self.cambiarSignos()
        #self.imprimeArregloZ() # verifica si esta imprimiendo bien M

    def cambiarSignos(self):
        global arregloZ,tabla
        for x in range(len(arregloZ)):
            arregloZ[x].numeroM=arregloZ[x].numeroM*-1
            arregloZ[x].numeroSinM=arregloZ[x].numeroSinM*-1
            tabla[0][self.ubicar_En_Tabla(arregloZ[x])]=arregloZ[x]    

    def ubicar_En_Tabla(self,elemento):
        global arregloCol
        for x in range(len(arregloCol)):
            if elemento.letra == arregloCol[x]:
                return x
        return -1         

    def convertirNulo_ObjetosU(self):
        for x in range(len(arregloCol)):
            z=Z_Aux(0,0,arregloCol[x])
            tabla[0][x]=z
       

#-------------------------------------------------------
#Matriz      
class Matriz:
    #Constructor
    def __init__(self, arreglo):
        self.matriz = arreglo
       
   
    def set_Matriz(self, valor):  #set matriz  
        print("Matriz cambiada")
        self.matriz = valor

    def get_Matriz(self):
        return self.matriz
   
    def cantidad_filas(self):
        if(len(self.matriz) is not 0):
           global variablesDecision, tabla
           filas=variablesDecision+2 # col solucion y col division
           for i in range (len(self.matriz)):
               indica = self.matriz[i][len(self.matriz[i])-1]
               filas+=self.cantidad_filasAux(indica)
        tabla=[[0 for i in range(filas)] for i in range(len(self.matriz)+1)]

    def cantidad_filasAux(self,argument):
        switcher = {">=": 2}
        return switcher.get(argument, 1)

    def variablesX(self):
        global variablesDecision
        for i in range (0,variablesDecision):
            arregloCol.append("x"+str(i+1))
        


#-----------------------------------------------------------
#Restricciones

class Restricciones:
    #Constructor
    def __init__(self, arreglo,esMin):
        self.matriz = arreglo
        self.varR=1
        self.varS=1
        self.esMin=esMin
       
    def colocar_Restricciones(self):
        global variablesDecision
        posicion = variablesDecision-1  # aumenta en R y S
        
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])-2):
                tabla[i+1][j]=self.matriz[i][j]
            m = Matriz(self.matriz)
            self.verificar_Signo(self.matriz[i][len(self.matriz[i])-1])
            x= m.cantidad_filasAux(self.matriz[i][len(self.matriz[i])-1])
            posicion += x
            tabla[i+1][len(tabla[i])-2]=self.matriz[i][len(self.matriz[i])-2]
            if x is 2:
                tabla[i+1][posicion-1]=1
                tabla[i+1][posicion]=-1
            else: tabla[i+1][posicion]=1

        arregloCol.append("SOL")
        arregloCol.append("DIV")
       
    def MayorIgual(self):
        arregloCol.append("R"+str(self.varR))
        arregloCol.append("S"+str(self.varS))
        arregloFilas.append("R"+str(self.varR))
        z=Z_Aux(self.verificar_Min(self.esMin),0,"S"+str(self.varS))
        global arregloZ
        arregloZ.append(z)
        self.varR+=1
        self.varS+=1
        
    def verificar_Min(self,argument):
        switcher = {True: 1}
        return switcher.get(argument, -1)
            
        
    def MenorIgual(self):
        arregloCol.append("S"+str(self.varS))
        arregloFilas.append("S"+str(self.varS))
        self.varS+=1

    def Igual(self):
        arregloCol.append("R"+str(self.varR))
        arregloFilas.append("R"+str(self.varR))
        self.varR+=1    
 
    def verificar_Signo(self,signo):
        switcher = {">=": self.MayorIgual,"<=": self.MenorIgual, "=": self.Igual }
        switcher [signo]()
        

#------------------------------------------------------------          
class Controlador:
    '''
    Metodo main en donde se llaman a las funciones para
    la implementacion metodo M """
      
    '''
    def __init__(self):
        self.esMinimizar= True# se recibe
        self.arregloZ=[3,5]
        self.arregloEntrada=[[2,1,6,"<="],[-1,3,9,"="],[0,1,4,">="]] # lo que entra ***************
        #------------**------------------------**------------------

    def inicioControlador(self):    
        print("-> Representacion de la impresion:")
        print(" ----------------------")
        print("|* R = Var Artificial   |")
        print("|* S = Var Holgura      |")
        print("|* X = Var Decision     |")
        print(" ----------------------\n\n")

        matriz = Matriz(self.arregloEntrada) # crea objeto para la impresion
        #matriz.imprime_Matriz(matriz.get_Matriz())
        matriz.cantidad_filas() # crea la tabla
        matriz.variablesX()
        restricciones=Restricciones(self.arregloEntrada,self.esMinimizar)
        restricciones.colocar_Restricciones()
        #
        z=Z(self.arregloEntrada,self.esMinimizar,self.arregloZ)
        z.crearZ()
        z.agregarRestricciones()
      #-----
        global arregloFilas,arregloCol,tabla
        gM=GranM(tabla,arregloFilas,arregloCol,self.esMinimizar)
        gM.start_MetodoM_Max()
        
  
    #tabla de forma estandar OK
   
    #print(arregloEntrada)
#-------------------------------------------------------------
#-------------------------------------------------------------
#INICIO DEL PROGRAMA
def mainControlador():
    controlador = Controlador()
    controlador.inicioControlador()
mainControlador()
