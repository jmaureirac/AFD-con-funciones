import sys

# VALIDAR ENTRADA QUE NO SE REPITA
def validar(K,x):
    if (pertenece(x,K)!= True):
        K.append(x)
        return True
    else:
        return False


# VALIDAR UN CARACTER PARA ALFABETO
def unchar(e):
    if len(e)==1:
        return True
    else:
        return False


# COMPROBAR SI x PERTENECE A K
def pertenece(x,K):
    if x in K:
        return True
    else:
        return False


# FUNCION INGRESAR ESTADOS
def estados(K):
    print("\n\t+-------------------------------------------------------+")
    print("\t|                 CONJUNTO DE ESTADOS                   |")
    print("\t|             Digite 'ok' para finalizar                |")
    print("\t+-------------------------------------------------------+\n")
    while (True):
        x = input("   -> Ingrese estado: ")
        if (x=="ok" or x=="OK") and (len(K)>0):
            break
        if(validar(K,x)==True):
            continue
        else:
            print("\t* Estado ya ingresado.")
            continue
    return K


# FUNCION INGRESAR LENGUAJE
def alfabeto(E):
    print("\n\t+-------------------------------------------------------+")
    print("\t|                     ALFABETO                          |")
    print("\t|             Digite 'ok' para finalizar                |")
    print("\t+-------------------------------------------------------+\n")
    while (True):
        x = input("   -> Ingrese caracter alfabeto: ")
        if (x=="ok" or x=="OK"):
            break
        if(unchar(x)==True):
            if(validar(E,x)==True):
                continue
            else:
                print("\t* Caracter ya ingresado.")
                continue
        else:
            print("\t* Caracter invalido, tiene que ser un caracter")
            continue
    return E


# FUNCION PARA ESTADO INICIAL
def estado_inicial(K):
    print("\n\t+-------------------------------------------------------+")
    print("\t|                   ESTADO INICIAL                      |")
    print("\t+-------------------------------------------------------+\n")
    x = input("   -> Ingrese estado inicial: ")
    while (True):
        if (pertenece(x,K)==True):
            return x
        else:
            print("\t* '"+x+"' no pertenece al conjunto K.")
            x = input("   -> Ingrese nuevamente: ")
            continue


# FUNCION PARA CONJUNTO DE ESTADOS FINALES
def estado_final(K,F):
    largo = len(K)
    n = 0
    print("\n\t+-------------------------------------------------------+")
    print("\t|              CONJUNTO ESTADOS FINALES                 |")
    print("\t|             Digite 'ok' para finalizar                |")
    print("\t+-------------------------------------------------------+\n")
    while n < largo :
        #x = input("   -> Ingrese estado final: ")
        while (True):
            x = input("   -> Ingrese estado final: ")
            if x in K:
                if x not in F:
                    F.append(x)
                else:
                    print("\t* '"+x+"' ya ingresado.")
                    break

                n+=1

            else:
                if (x=="ok" or x=="OK"):
                    return F
                else:
                    print("\t* '"+x+"' no pertenece al conjunto K.")
                    break
    return F


# FUNCION INICIALIZAR TABLA
def inicializar(tabla,lenK,lenE):
    for i in range(lenK):
        tabla.append([])
        for j in range(lenE):
            tabla[i].append([None])
    return tabla


# FUNCION RECIBIR TRANSICIONES
def tabla_transiciones(K,E):
    tabla = []
    filas = len(K)
    columnas = len(E)
    tabla_t = inicializar(tabla,filas,columnas)
    print("\n\t+-------------------------------------------------------+")
    print("\t|               TABLA DE TRANSICIONES                   |")
    print("\t+-------------------------------------------------------+\n")
    for i in range(filas):
        for j in range(columnas):
            while(True):
                x = input("   -> '"+K[i]+"' ingresando '"+E[j]+"': ")
                if (pertenece(x,K)==True):
                    tabla_t[i][j] = x
                    break
                else:
                    print("\t  "+x+" no pertenece a K.")
                    continue
    return tabla_t


# FUNCION VALIDAR PALABRA CON LENGUAJE
def validar_palabra(E,palabra):
    final = False
    for i in range(len(palabra)):
        if pertenece(palabra[i],E)==True:
            final = True
        else:
            return False
    return final


# FUNCION POSICION ESTADO INICIAL, PRESENTE
def pos(S,K):
    for i in range(len(K)):
        if K[i] == S:
            return i


# FUNCION PARA INICIALIZAR AFD E INGRESAR DATOS
def inicializarAFD():
    K = []
    E = []
    F = []

    estados(K)
    alfabeto(E)
    S = estado_inicial(K)
    estado_final(K,F)
    Q=tabla_transiciones(K,E)

    afd = [K,E,S,F,Q]

    return afd


# FUNCION IMPRIMIRCONJUNTO
def imprimir_conjunto(C):
    print("\n\t\t\t>>   {  ",end ="")
    for i in range(len(C)):
        print(C[i]+"  ",end="")
    print("}",end="")


# FUNCION PARA IMPRIMIR LA QUINTUPLA DEL AFD
def imprimirAFD(afd):
    K = afd[0]
    E = afd[1]
    S = afd[2]
    F = afd[3]
    Q = afd[4]
    print("\n\t+-------------------------------------------------------+")
    print("\t|          QUINTUPLA DEL AUTOMATA INGRESADO             |")
    print("\t+-------------------------------------------------------+\n")
    print ("\n\t\tCONJUNTO DE ESTADOS: ")
    imprimir_conjunto(K)
    print ("\n\n\t\tALFABETO: ")
    imprimir_conjunto(E)
    print("\n\n\t\tESTADO INICIAL:")
    imprimir_conjunto(S)
    print("\n\n\t\tCONJUNTO DE ESTADOS FINALES:")
    imprimir_conjunto(F)
    print("\n\n\t\tTABLA DE TRANSICIONES:")
    print("\n\t\t\t|Estado\t|   ", end = "")
    for indice in range(len(E)):
        print(E[indice]+"\t|   ", end = "")
    print("")
    for i in range(len(Q)):
        print("\n\t\t\t| '"+K[i]+"' \t|   ", end = "")
        for j in range(len(E)):
            print (Q[i][j]+"\t|   ", end = "")
        print("")

    print("\n\t\t+-----------------------------------------------+")
    print("\t\t| Digite 'mostrar' para desplegar AFD ingresado |")
    print("\t\t| Digite 'nuevo' para ingresar nuevo AFD        |")
    print("\t\t| Digite 'salir' para terminar programa         |")
    print("\t\t+-----------------------------------------------+")


# FUNCION LEER PALABRA
def AFD(K,E,S,F,Q,palabra):
    EP = pos(S,K)
    ES = 0
    for i in range(len(palabra)):
        for j in range(len(E)):
            if palabra[i] == E[j]:
                ES = Q[EP][j]
        EP = pos(ES,K)
    return K[EP]


# FUNCION PRINCIPAL
def main():
    while(True):
        afd = inicializarAFD()
        imprimirAFD(afd)
        K = afd[0]
        E = afd[1]
        S = afd[2]
        F = afd[3]
        Q = afd[4]
        while True:
            x = input("\n\n\t >> Ingresar palabra: ")
            if (x == 'mostrar'):
                imprimirAFD(afd)
                continue
            if (x == 'nuevo'):
                main()
            if (x == 'salir'):
                print("\n\nFINALIZANDO PROGRAMA\n")
                fin=input("PULSE ENTER PARA SALIR...")
                sys.exit(0)
            elif validar_palabra(E,x) or len(x)==0:
                EP = AFD(K,E,S,F,Q,x)
                print ("\n\t\t\tEstado en que termina la maquina: "+EP)
                if (pertenece(EP,F)):
                    print ("\t\t\t>> Palabra reconocida por la maquina")
                else:
                    print ("\t\t\t* Palabra no reconocida por la maquina")
            else:
                print("\n\t\t\t* Lenguaje erroneo")
                continue
