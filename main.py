import quintupla

K = []
E = []
F = []



quintupla.estados(K)
quintupla.alfabeto(E)
S = quintupla.estado_inicial(K)
quintupla.estado_final(K,F)
Q=quintupla.tabla_transiciones(K,E)

#IMPRIMIR QUINTULPLA

print ("\nK: ")
print (K)

print ("\nE: ")
print (E)

print("\nS:\n"+S)

print("\nF:")
print (F)

print("\nTabla de transiciones:")
for i in range(len(Q)):
    print (K[i],Q[i])


print ("\n")
while(True):
    while True:
        x = input("\nIngresar palabra: ")
        if quintupla.validar_palabra(E,x) or len(x)==0:
            EP = quintupla.AFD(K,E,S,F,Q,x)
            print ("Estado en que termina la maquina: "+EP)
            if (quintupla.pertenece(EP,F)):
                print ("-Palabra reconocida por la maquina")
            else:
                print ("-Palabra no reconocida por la maquina")
        else:
            print("-Palabra no reconocida por el lenguaje.")
            continue
