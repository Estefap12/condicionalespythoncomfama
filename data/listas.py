#Toda lista se debe escribir en PLURAL
arboles=['ceiba','yarumo','manzano','guayacan']
municipios=['Medelllin','Titiribi','Carolina del principe']
hectareaSembradas=[2500,500,1200]
lluviasMayoresA500=[False,True,True]

#Recorriendo un arreglo...
#Acceder de FORMA DINAMICA al contenido de un arreglo
#Para recorrerlo DEBO UTILIZAR UN CICLO O BUCLE O LOOP

#Ciclo While (mientras)
'''contador=0
while contador<10 :
    contador=contador+1
    print ("estoy triunfando...")'''

#Ciclo For (Para)
'''for i in range(1,301,2):
    print(i)'''

#Recorrer dinanicamnete un arreglo usando un FOREACH (Para cada uno)
for arbol in arboles:
    print(arbol)

for municipio in municipios:
    print(municipio)

