#arbol

#El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
#resolver los siguientes requerimientos:
#1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
#conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
#por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
#distintos, los códigos no pueden ser repetidos (tenga cuidado);
#2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
#código;
#3. realizar un barrido en orden del árbol ordenado por nombre;
#4. mostrar toda la información del dinosaurio 792;
#5. mostrar toda la información de todos los T-Rex que hay en la isla;
#6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
#cargado, su nombre correcto es Stygimoloch;
#7. mostrar la ubicación de todos los Raptores que hay en la isla;
#8. contar cuantos Diplodocus hay en el parque;
#9. debe cargar al menos 15 elementos.

from arbol_binario import Arbol

arbolA = Arbol ()
arbolB = Arbol ()

dinosaurio = {'nombre': 'T-REX', 'codigo': 'ARF4A', 'zona': ' sur'}        #1
dinosaurio = {'nombre': 'dinosaurioB', 'cod': '792', 'zona': ' norte'}
dinosaurio = {'nombre': 'dinosaurioC', 'cod': 'AR6tr', 'zona': ' este'}
dinosaurio = {'nombre': 'dinosaurioD', 'cod': 'SED44', 'zona': ' central'}
dinosaurio = {'nombre': 'dinosaurioE', 'cod': 'POL00', 'zona': ' oeste'}
dinosaurio = {'nombre': 'dinosaurioF', 'cod': 'QWE33', 'zona': ' sur '}
dinosaurio = {'nombre': 'dinosaurioG', 'cod': 'QAS39', 'zona': ' oeste'}
dinosaurio = {'nombre': 'dinosaurioH', 'cod': 'VBGF5', 'zona': ' central'}
dinosaurio = {'nombre': 'dinosaurioI', 'cod': 'SXZD44', 'zona': ' este'}
dinosaurio = {'nombre': 'dinosaurioJ', 'cod': 'PLUJ88', 'zona': ' norte'}

for dinosaurio in dinosaurio:                                           #2
    arbolA = arbolA.insertar_nodo(dinosaurio['nombre'],dinosaurio)
    arbolB = arbolB.insertar_nodo(dinosaurio['cod'],dinosaurio)


arbolA.inorden() #3


buscado = '792'                        #4
pos = arbolB.busqueda(buscado)
if pos:
    print ('la informacion del dinosaurio 792 es:' 'buscado' ,pos.datos)
print()

arbolA.busqueda_proximidad('T-Rex')  #5

buscado = input ('ingrese el nombre a modificar')       #6
pos = arbolA.busqueda (buscado)

if (pos):
    nombre_nuevo = ('ingrese el nombre modificado')
    nombre, dinosaurio = arbolA.eliminar_nodo (buscado)
    dinosaurio ['nombre'] = nombre_nuevo
    arbol = arbolA.insertar_nodo(nombre_nuevo,dinosaurio)

arbolA.busqueda_proximidad('Raptores')  #7


print ("cantidad de diplodocus: ")
print(arbolA.contar_ocurrencias('Diplodocus')) #8




#grafo


#Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
#necesarios para resolver las tareas, listadas a continuación:
#1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
#2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
#Hat, Debian, Arch;
#3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
#Debian y Red Hat, hasta el servidor “MongoDB”;
#4. encontrar el árbol de expansión mínima;
#5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
#realice un barrido en profundidad para corroborar que efectivamente fue borrada;
#6. debe utilizar un grafo no dirigido.

from grafo import Grafo

grafo = Grafo(dirigido=False)

#vertice

grafo.insertar_vertice("pc1",data={"tipo":"PC"})
grafo.insertar_vertice("pc2",data={"tipo":"PC"})
grafo.insertar_vertice("pc3",data={"tipo":"PC"})
grafo.insertar_vertice("pc4",data={"tipo":"PC"})
grafo.insertar_vertice("pc5",data={"tipo":"PC"})

grafo.insertar_vertice("red hat",data={"tipo":"notebook"})
grafo.insertar_vertice("debian",data={"tipo":"notebook"})
grafo.insertar_vertice("arch",data={"tipo":"notebook"})

grafo.insertar_vertice("servidor1",data={"tipo":"Servidor"})
grafo.insertar_vertice("mongoDB",data={"tipo":"Servidor"})


grafo.insertar_vertice("router1",data={"tipo":"Router"})
grafo.insertar_vertice("router2",data={"tipo":"Router"})
grafo.insertar_vertice("router3",data={"tipo":"Router"})

grafo.insertar_vertice("switch1",data={"tipo":"switch"})
grafo.insertar_vertice("switch2",data={"tipo":"switch"})

grafo.insertar_vertice("impresora",data={"tipo":"impresora"})


#arista

grafo.insertar_arista(9,"router1","switch1")      #1

grafo.insertar_arista(20,"router2","servidor1")
grafo.insertar_arista(25,"router2","red hat")

grafo.insertar_arista(0,"router3","router2")
grafo.insertar_arista(4,"router3","router1")

grafo.insertar_arista(11,"switch1","debian")
grafo.insertar_arista(8,"switch1","pc4")
grafo.insertar_arista(22,"switch1","Impresora")
grafo.insertar_arista(7,"switch1","pc3")

grafo.insertar_arista(10,"switch2","pc2")
grafo.insertar_arista(13,"switch2","pc1")
grafo.insertar_arista(5,"switch2","mongoDB")
grafo.insertar_arista(1,"switch2","arch")
grafo.insertar_arista(3,"switch2","pc5")
grafo.insertar_arista(6,"switch2","router2")


posicion_redhat = grafo.buscar_vertice("red hat")       #2
grafo.barrido_profundidad(posicion_redhat)
grafo.barrido_amplitud(posicion_redhat)


posicion_debian = grafo.buscar_vertice("debian")
grafo.barrido_profundidad(posicion_debian)
grafo.barrido_amplitud(posicion_debian)


posicion_arch = grafo.buscar_vertice("arch")
grafo.barrido_profundidad(posicion_arch)
grafo.barrido_amplitud(posicion_arch)


debian_redhat = "debian", "redhat"                 #3
origen = grafo.buscar_vertice (debian_redhat)

mongodb = "mongoDB"
destino = grafo.buscar_vertice (mongodb)

camino = grafo.dijkstra (origen, destino)

print ("el camino mas corto es:")

destino = mongodb
costo = None
while (not camino.pila_vacia ()):
    dato = camino.desapilar ()
    if (dato [1][0] == destino):
        if (costo is None):
            cosot = dato [0]
        print (dato [1][0])
        destino = dato 
print ("costo total desde debian y red hat hasta mongo es:", costo)





def exp_minima(grafo):           #4
    arbol = []
    exp_minima = grafo.prim()

    for m in exp_minima:
        print(m)


grafo.eliminar_vertice("impresora")       #5
grafo.barrido_profundidad(0) 




