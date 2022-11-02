from lexer import get_tokens
from parser import ll1

from collections import deque
ruta = "Tests/test2.txt"

cola = deque()
colaVar = deque()

def agregarElemVar(par):
    colaVar.append(par)

def agregarElem(par):
    cola.append(par)

def eliminarElem(dicc, nomFun):
    if dicc == nomFun:
        siguiente_elemento = cola.popleft()
        print(f'Elemento Eliminado: {siguiente_elemento}')

def verificarElem(nomVar, cola, diccionario):

    if nomVar in colaVar:
        print(f'La VARIABLE ',(nomVar),' ya se encuentra en el diccionario - ERROR SEMANTICO')
        #time.sleep(5)
    if nomVar not in colaVar: 
        print(f'La VARIABLE {nomVar} No encuentra en el diccionario')
        agregarElem(diccionario)

def mostrarCola(cola):
    c=0
    while c < len(cola) :
        c+=1
    print(f'Cola: {cola}')




def creationVar(root):
    #print(root.symbol.symbol)
    for c in root.children:
        ##Creando una variable
        if c.symbol.symbol == "TYPE":
            node_id = c.father.children[1]
            funPadre = c.father.father.father.children[1]
            print("Variable creada '", node_id.lexeme, "' en línea", node_id.line)
            diccionario = {'lexeme': node_id.lexeme, 'id/funcion':'id', 'funPadre': funPadre.lexeme}
            verificarElem(node_id.lexeme, cola, diccionario)
            agregarElemVar(node_id.lexeme)
            #asas agr_ _ egarElem(diccionario)

        creationVar(c)


def funcTerm(root):
    for c in root.children:
        if c.symbol.symbol == "funcion":
            ############## Creando función ##############
            func_id = c.father.children[1]
            print("funcion creada '", func_id.lexeme, "' en línea ", func_id.line)
            agregarElem({'lexeme': func_id.lexeme, 'id/funcion':'id', 'funPadre': 'GLOBAL'})


            ############## Terminando función ##############
            tam = len(c.father.children)
            func_term_id = c.father.children[tam-2]
            print("funcion terminada en la línea: ", func_term_id.line)
            diccionario = {'lexeme': func_id.lexeme, 'id/funcion':'funcion', 'funPadre': 'GLOBAL'}
            eliminarElem(diccionario.get('lexeme') , func_id.lexeme)
            
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

def findInTree(root, colaVar):
    for c in root.children:
        #Viendo que la coincidencia no sea la creación
        ev = c.father.children[0]
        varI = c.father.children[0]
        #if (ev.symbol.symbol != "TYPE") and (c.lexeme == sym):
        #    print("Elemento '", c.lexeme, "' encontrado en", c.line)
        #if (c.symbol.symbol == "id") and (c.lexeme in colaVar):
        #    print(print("ELEEMEMEME '", varI.lexeme, "' encontrado en", varI.symbol.symbol))
        findInTree(c,colaVar)

def UsageVar(root):
    for c in root.children:
        ##Creando una variable
        if (c.symbol.symbol == "id") and (c.father.children[0].symbol.symbol != "funcion") and (c.father.children[0].symbol.symbol != "TYPE"):

            #print(c.lexeme)
            if (c.lexeme not in colaVar):
                print("ERROR", c.lexeme, "NO HA SIDO CREADO")
        UsageVar(c)


if __name__ == "__main__":
    root, element_tree = ll1(ruta)
    
    creationVar(root)
    funcTerm(root)
    findInTree(root, "x")
    UsageVar(root)
    mostrarCola(cola)
