tabla=[[]]
arregloFilas=[]
arregloCol=[]
from Print import *

#-----------------------------------------------------------

class GranM:
    
    def __init__(self, tablaAux,arregloFilasAux,arregloColumnasAux,esMin):
        global tabla,arregloFilas,arregloCol
        tabla = tablaAux
        arregloFilas=arregloFilasAux
        arregloCol=arregloColumnasAux
        self.esMin=esMin
        self.flagDg=False
      
#------------------------------------------------
#verificar si el ciclo ya acabo
    def optimoMax(self):
        global tabla
        for x in range(0,len(tabla[0])-2):
            valor = tabla[0][x].numeroM * 100000 + tabla[0][x].numeroSinM
            if(valor<0): return False
        return True
        
    def optimoMin(self):
        for x in range(len(tabla[0])-2):
            valor = tabla[0][x].numeroM * 100000 + tabla[0][x].numeroSinM
            if(valor>0):return False
        return True
#------------------------------------------------

    def encontrarColPivotMax(self):
        global tabla
        indica=tabla[0][0].numeroM * 100000 + tabla[0][0].numeroSinM
        col=0
        for x in range(len(tabla[0])-2):
            if indica>tabla[0][x].numeroM * 100000 + tabla[0][x].numeroSinM:
                indica = tabla[0][x].numeroM * 100000 + tabla[0][x].numeroSinM
                col=x
        return col

    def encontrarColPivotMin(self):
        global tabla
        indica=tabla[0][0].numeroM * 100000 + tabla[0][0].numeroSinM
        col=0
        
        for x in range(len(tabla[0])-2):
            if indica<tabla[0][x].numeroM * 100000 + tabla[0][x].numeroSinM:
                indica = tabla[0][x].numeroM * 100000 + tabla[0][x].numeroSinM
                
                col=x
        return col
#-------------------------------------------------
    def realizarDivision(self,columna):
        global tabla
        for x in range(1,len(tabla)):
            if tabla[x][columna]!=0:
                i=round(tabla[x][len(tabla[x])-2]/tabla[x][columna], 2)
                tabla[x][len(tabla[x])-1]=i
            else : tabla[x][len(tabla[x])-1]=0

    def hallarFilaPivot(self):  #OJO VERIFICAR QUE HAYAN POSITIVOS Y QUE NO HAYAN IGUALES MENORES POSITIVOS
        global tabla # indica siempre debera ser positivo
        indica=1000
        fila=-1
        for x in range(1,len(tabla)):
            if(tabla[x][len(tabla[x])-1]>0 and tabla[x][len(tabla[x])-1] < indica):
                indica =tabla[x][len(tabla[x])-1]
                fila=x
        return fila
            
    def elegirCol(self):
        if(self.esMin is True):return self.encontrarColPivotMin()
        else: return self.encontrarColPivotMax()

    def degeneradaSolucion(self,fila):
        cont=0
        for i in range(1,len(tabla)):
            if tabla[i][len(tabla[i])-1] == tabla[fila][len(tabla[i])-1]:
                cont+=1
        return cont

    def verificarDegenerada(self):
        if self.flagDg is True:
            print("\n\n-> Solucion Degenerada hubo empate en coef minimo")
        #else: print("\n\n-> No es una solucion degenerada")
    #-----------------------------------------------------
            
    def solucionExtra(self, col):
        global tabla,arregloFilas,arregloCol
        impresion=Imprime()
        columnaPivot= col
        self.realizarDivision(columnaPivot)
        filaPivot=self.hallarFilaPivot()
        print("- Numero Pivot: "+ str(round(tabla[filaPivot][columnaPivot],2))+ ",VB entrante: "+ arregloCol[columnaPivot]+ ",VB saliente: "+ arregloFilas[filaPivot])
        self.convertir_Fila_Pivot(filaPivot,columnaPivot)
        self.modificar_Filas(filaPivot,columnaPivot)
        self.modificar_FilaZ(filaPivot,columnaPivot)
        arregloFilas[filaPivot]=arregloCol[columnaPivot]
        impresion.imprime_Matriz()
        print("\n\n*** Solucion EXTRA ***")
    #------------------------------------------------

    def start_MetodoM_Max(self):#primero lo voy hacer con Maximizar
        '''
        CONTROLA LAS FUNCIONALIDA
        '''
        impresion=Imprime()
        estados=0
        global tabla,arregloFilas,arregloCol
        print_Aux= Print()
        multiplesSol=Multiples_Solucion()
        s=Solucion()
        s_Extra=Solucion()
        print_Aux.imprime_Matriz(tabla,arregloFilas,arregloCol)
        while True:
            
            if self.optimoMax() is True and self.esMin is False or self.optimoMin() is True and self.esMin is True :
                self.verificarDegenerada()
                print("- Estado Final")
                s.mostrarSolucion(tabla,arregloFilas,arregloCol)
                if multiplesSol.localizar_VB(tabla,arregloFilas,arregloCol)!= -1:
                    #existen multiples soluciones
                    self.solucionExtra(multiplesSol.localizar_VB(tabla,arregloFilas,arregloCol))
                    
                    s_Extra.mostrarSolucion(tabla,arregloFilas,arregloCol)
                break
            
            columnaPivot= self.elegirCol()
            self.realizarDivision(columnaPivot)
            filaPivot=self.hallarFilaPivot()
            if(filaPivot == -1):#VERIFICA SOLUCION ACOTADA
                print("\n- Estado: "+ str(estados))
                print("********* Solucion acotada *********")
                s.mostrarSolucion(tabla,arregloFilas,arregloCol)
                break
            
            if self.degeneradaSolucion(filaPivot) >= 2:
                self.flagDg=True
            
            print("\n- Estado: "+ str(estados))
            estados+=1
            print("- Numero Pivot: "+ str(round(tabla[filaPivot][columnaPivot],2))+ ",VB entrante: "+ arregloCol[columnaPivot]+ ",VB saliente: "+ arregloFilas[filaPivot])
            arregloFilas[filaPivot]=arregloCol[columnaPivot]
            
            self.convertir_Fila_Pivot(filaPivot,columnaPivot)
            self.modificar_Filas(filaPivot,columnaPivot)
            self.modificar_FilaZ(filaPivot,columnaPivot)
            impresion.imprime_Matriz()
            
            
            #cambiar columnas
            #multiplicaresa fila por 1 / ese numero que es 2
            #demas filas sumar multiplicadas por el 1 de fila pivot
            
            #print(tabla[filaPivot][columnaPivot])
            #---------------------Imprimiendo
              # se encuentra en archivo gran M
            

    def modificar_Filas(self,filaPivot,columnaPivot):
        global tabla
        for i in range(1,len(tabla)):
            if i != filaPivot:
                arg1=tabla[i][columnaPivot]
                for j in range(0,len(tabla[i])-1):
                    x=tabla[i][j]-arg1*tabla[filaPivot][j]
                    tabla[i][j]=x

    def modificar_FilaZ(self,filaPivot,columnaPivot):
        global tabla
        lista=[]
        lista2=[]
        for i in range(len(tabla[0])-1):
            arg1=tabla[0][columnaPivot].numeroM
            arg2=tabla[0][columnaPivot].numeroSinM
            x=tabla[0][i].numeroM-arg1*tabla[filaPivot][i]
            y=tabla[0][i].numeroSinM-arg2*tabla[filaPivot][i]
            lista.append(x)
            lista2.append(y)
        #print(lista)
        x=0
        while x < len(lista):
            tabla[0][x].numeroM=lista[x]
            tabla[0][x].numeroSinM=lista2[x]
            x+=1
            
    
    def convertir_Fila_Pivot(self,filaPivot,columnaPivot):
        denominador=(1/tabla[filaPivot][columnaPivot])
        y=0
        while y < len(tabla[filaPivot])-1:
            numerador=(tabla[filaPivot][y])
            x= numerador*denominador
            tabla[filaPivot][y]=x
            y+=1

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

#Impresion de la parte grafica
class Imprime:
    #Constructor
    def __init__(self):
        pass

    def imprime_Columnas(self):
        global arregloCol
        aux="\n\n\n\t"
        aux2="\t"
        for i in arregloCol:
            aux+=i+"\t     |"
            aux2+="-------------"
        aux2+="------------"
        print (aux+"\n"+aux2)

    def imprimeFilaU(self):
        global arregloFilas
        aux=arregloFilas[0]+"\t"
        for x in range (len(tabla[0])):
            var=round(tabla[0][x].numeroM,2)
            var2=round(tabla[0][x].numeroSinM,2)
            if tabla[0][x].numeroM == 0: aux+=str(var2)+"\t    |"
            elif tabla[0][x].numeroM != 0 and tabla[0][x].numeroSinM == 0:
                aux+=str(var)+"M\t    |"
            else:aux+=str(var2)+"+"+str(var)+"M\t    |"
        print (aux)
 
    def imprime_Matriz(self):
       global tabla,arregloFilas
       if(len(tabla) is not 0):
          aux=""
          self.imprime_Columnas()
          self.imprimeFilaU()
          for i in range (1,len(tabla)):
              aux=arregloFilas[i]+"\t"
              for j in range (len(tabla[i])):
                  var=round(tabla[i][j],2)
                  aux+=str(var)+"\t    |"
              print(aux)

#-----------------------------------------------------------     
