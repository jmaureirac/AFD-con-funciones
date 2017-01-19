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
    print("->Ingresar conjunto de estados.\nPara finalizar digite end/fin.\n")
    while (True):
        x = input("Ingrese estado: ")
        if (x=="fin" or x=="end"):
            break
        if(validar(K,x)==True):
            continue
        else:
            print("Estado ya ingresado.")
            continue
    return K


# FUNCION INGRESAR LENGUAJE
def alfabeto(E):
    print("\n->Ingresar alfabeto.\nPara finalizar digite end/fin.\n")
    while (True):
        x = input("Ingrese caracter alfabeto: ")
        if (x=="fin" or x=="end"):
            break
        if(unchar(x)==True):
            if(validar(E,x)==True):
                continue
            else:
                print("Caracter ya ingresado.")
                continue
        else:
            print("Caracter invalido.")
            continue
    return E


# FUNCION PARA ESTADO INICIAL
def estado_inicial(K):
    print("")
    x = input("->Ingrese estado inicial: ")
    while (True):
        if (pertenece(x,K)==True):
            return x
        else:
            print(x+" no pertenece al conjunto K.")
            x = input("Ingrese nuevamente: ")
            continue


# FUNCION PARA CONJUNTO DE ESTADOS FINALES
def estado_final(K,F):
    print ("")
    largo = len(K)
    n = 0
    print ("->Ingresar estado/s final/es \nPara finalizar digite end/fin\n")
    while n < largo :
        x = input("Ingrese estado final: ")
        while (True):
            if (pertenece(x,K)==True):
                F.append(x)
                break
            else:
                if (x=="fin" or x=="end"):
                    return F
                else:
                    print(x+" no pertenece al conjunto K.")
                    break
        n+=1

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
    print("\n-> Tabla de transiciones\n")
    for i in range(filas):
        for j in range(columnas):
            while(True):
                x = input("'"+K[i]+"' ingresando '"+E[j]+"': ")
                if (pertenece(x,K)==True):
                    tabla_t[i][j] = x
                    break
                else:
                    print(x+" no pertenece a K.")
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
