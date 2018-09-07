#Impresion de la parte grafica
#-----------------------------------------------------------
#-----------------------------------------------------------

class Print:
    #Constructor
    def __init__(self):
        pass
        

    def imprime_Columnas(self,arregloCol):
        
        aux="\t"
        aux2="\t"
        for i in arregloCol:
            aux+=i+"\t"
            aux2+="------"
        aux2+="------------"
        print (aux+"\n"+aux2)

    def imprimeFilaU(self,tabla,arregloFilas):

        aux=arregloFilas[0]+"\t"
        for x in range (len(tabla[0])):
            if tabla[0][x].numeroM == 0: aux+=str(tabla[0][x].numeroSinM)+"\t"
            elif tabla[0][x].numeroM != 0 and tabla[0][x].numeroSinM == 0:
                aux+=str(tabla[0][x].numeroM)+"M\t"
            else: aux+=str(tabla[0][x].numeroSinM)+"+"+str(tabla[0][x].numeroM)+"M\t"
        print (aux)
 
    def imprime_Matriz(self,tabla,arregloFilas,arregloCol):

       if(len(tabla) is not 0):
          aux=""
          self.imprime_Columnas(arregloCol)
          self.imprimeFilaU(tabla,arregloFilas)
          for i in range (1,len(tabla)):
              aux=arregloFilas[i]+"\t"
              for j in range (len(tabla[i])):
                  aux+=str(tabla[i][j])+"\t"
              print(aux)

#-----------------------------------------------------------
#-----------------------------------------------------------

class Solucion:
    '''Impresion del resultado final'''
    
    def __init__(self):
        
        self.lista=[]
        self.lista2=[]
        
        
    def mostrarSolucion(self,tabla,arregloFilas,arregloCol):
        self.lista.append("U")
        self.lista2.append(str(round(tabla[0][len(tabla[0])-2].numeroM,2)) +"M + "+str(round(tabla[0][len(tabla[0])-2].numeroSinM,2)))
        for i in range(1, len(arregloFilas)):
            self.lista.append(arregloFilas[i])
            
            self.lista2.append(tabla[i][len(tabla[i])-2])
        
        self.colocar_Variables(arregloCol)
        self.imprimirVar()
        
    def colocar_Variables(self,arregloCol):
        for i in range(0,len(arregloCol)-2):
            
            if arregloCol[i] in self.lista:
                continue
            else:
                self.lista.append(arregloCol[i])
                self.lista2.append(0)
                
    def imprimirVar(self):
        print("*************************\n ->Respuesta Final: ")
        aux="( "+str(self.lista[0]) +": "+ str(self.lista2[0])
        for i in range(1,len(self.lista)):
            aux+=","+str(self.lista[i]) +": "+ str(round(self.lista2[i],2))
        print (aux+" )")
        
                       
            
#-----------------------------------------------------------
#-----------------------------------------------------------

class Multiples_Solucion:
    '''Impresion del resultado final'''
    
    def __init__(self):
        self.listaPosiciones=[]
        
    def localizar_VB(self, tabla,arregloFilas,arregloCol):
        for i in range(1,len(arregloFilas)):
            self.listaPosiciones.append(arregloCol.index(arregloFilas[i]))
        
        return self.verificar_Multiples_Soluciones(tabla)
        
    def verificar_Multiples_Soluciones(self,tabla):
        for i in range(len (tabla[0])-2):
            if not i in self.listaPosiciones:
                if tabla[0][i].numeroM == 0 and tabla[0][i].numeroSinM == 0:
                    return i
        return -1
#-----------------------------------------------------------
#-----------------------------------------------------------
              
