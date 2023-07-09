#Daniel Sebastian Badillo Neira 2220071
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.padre = None
        self.izquierdo = None
        self.derecho = None
    
class MinHeap:
    def __init__(self):
        self.root = None
        self.tamaño = 0

    def insert(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.root is None:
            self.root = nuevo_nodo
        else:
            cola = [self.root]
            
            while len(cola) > 0:
                current = cola[0]
                if current.izquierdo is None:
                    current.izquierdo = nuevo_nodo
                    nuevo_nodo.padre = current
                    break

                elif current.derecho is None:
                    current.derecho = nuevo_nodo
                    nuevo_nodo.padre = current
                    break
                else:
                    cola.append(current.izquierdo)
                    cola.append(current.derecho)
                    cola.pop(0)
            self.ubicar(nuevo_nodo)
        self.tamaño +=1
    

    def ubicar(self, node):
        while node.padre is not None and node.padre.dato > node.dato:
            temp = node.dato
            node.dato = node.padre.dato
            node.padre.dato = temp
            node = node.padre

    def obtener_last(self):
        if self.root is None:
            return None
        cola = [self.root]
        last_node = None
        while len(cola) > 0:
            current = cola[0]
            last_node = current
            if current.izquierdo is not None:
                cola.append(current.izquierdo)
            if current.derecho is not None:
                cola.append(current.derecho)
            cola.pop(0)
        return last_node
        
    def extraerMin(self):
        if self.root is None:
            return None
        minimo = self.root.dato
        ultimo = self.obtener_last()

        if ultimo.dato != self.root.dato:
            self.root.dato = ultimo.dato
            if ultimo == ultimo.padre.izquierdo:
                ultimo.padre.izquierdo = None
            else:
                ultimo.padre.derecho = None
            self.hundir(self.root)
        else:
            self.root = None

        
        self.tamaño-=1
        return minimo

    def  hundir(self, node):
        while True:
            nodo_min = node
            if node.izquierdo is not None and node.izquierdo.dato < nodo_min.dato:
                nodo_min = node.izquierdo
            if node.derecho is not None and node.derecho.dato < nodo_min.dato:
                nodo_min = node.derecho
            if nodo_min is not node:
                temp = node.dato
                node.dato = nodo_min.dato 
                nodo_min.dato = temp
                node = nodo_min
            else:
                break
            
    def por_niveles(self):
        if self.root is None:
            print('None')
            return 0
        cola = [self.root]
        while len(cola) > 0:
            current = cola.pop(0)
            print(current.dato)
            if current.izquierdo is not None:
                cola.append(current.izquierdo)
            if current.derecho is not None:
                cola.append(current.derecho)

    def pre_order(self):
        if self.root is None:
            print('None')
            return 0
        cola = [self.root]
        while len(cola) > 0:
            current = cola.pop((len(cola)-1))
            print(current.dato)
            if current.derecho is not None:
                cola.append(current.derecho)
            if current.izquierdo is not None:
                cola.append(current.izquierdo)
            

minHeap = MinHeap()
minHeap.insert(10)
minHeap.insert(30)
minHeap.insert(40)
minHeap.insert(70)
minHeap.insert(15)
minHeap.insert(1)
minHeap.insert(0)

print('Recorrido en Pre-Order')
minHeap.pre_order()

print('Recorrido en Por niveles')
minHeap.por_niveles()

print('Extracciones')
print(minHeap.extraerMin())
print(minHeap.extraerMin())
print(minHeap.extraerMin())
print(minHeap.extraerMin())

