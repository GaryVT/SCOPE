from lexer import get_tokens
from parser import ll1

from collections import deque

ruta = "Tests/test2.txt"

cola = deque()

def agregarElem(par):
    cola.append(par)

def mostrarCola(cola):
    while len(cola) > 0:
        #extraer el primer elemento de la cola
        siguiente_elemento = cola.popleft()

        print(f'Elemento Eliminado: {siguiente_elemento}')
        print(f'Cola: {cola}')
        print('##########')




def creationVar(root):
    #print(root.symbol.symbol)
    for c in root.children:
        ##Creando una variable
        if c.symbol.symbol == "TYPE":
            node_id = c.father.children[1]
            print("Variable creada '", node_id.lexeme, "' en línea", node_id.line)
        creationVar(c)


def funcTerm(root):
    for c in root.children:
        if c.symbol.symbol == "funcion":
            ############## Creando función ##############
            func_id = c.father.children[1]
            print("funcion creada '", func_id.lexeme, "' en línea ", func_id.line)

            ############## Terminando función ##############
            tam = len(c.father.children)
            func_term_id = c.father.children[tam-2]
            print("funcion terminada en la línea: ", func_term_id.line)
            
        funcTerm(c)

'''
def findInTree(element_tree, sym):
    for nod in element_tree:
        #print(nod.symbol.symbol)
        
        if (nod.lexeme == sym ):
            print(nod.father.symbol)##and nod.father
            print("Elemento encontrado en", nod.line)
            print(nod.lexeme)
'''

def findInTree(root, sym):
    for c in root.children:
        #Viendo que la coincidencia no sea la creación
        ev = c.father.children[0]
        if (ev.symbol.symbol != "TYPE") and (c.lexeme == sym):
            print("Elemento '", c.lexeme, "' encontrado en", c.line)
        findInTree(c, sym)


if __name__ == "__main__":
    root, element_tree = ll1(ruta)
    
    creationVar(root)
    #funcTerm(root)
    #findInTree(root, "x")