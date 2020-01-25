import networkx as nx
import pandas as pd

edgelist = pd.read_excel('morse_code_tree.xlsx')
nodelist =  pd.read_excel('morse_code_tree.xlsx', sheet_name='nodes')

#funcion translate_to_morse()

def translate_to_morse(letra):
    morse = []
    p = nx.shortest_path(g, source=letra, target='Start')
    for i in range(len(p)-1):
        morse.insert(0,g.get_edge_data(p[i], p[i+1])['attr_dict'])
    print (morse)
    return morse

def translate_to_english(morse):
    nodo='Start'
    nodo_viejo ='Start'
    letra = list(morse)
    for letter in letra:
        for i in nx.all_neighbors(g,nodo):
            if i != nodo_viejo:
                valor = g.get_edge_data(nodo,i)['attr_dict']
                if str(letter) == str(valor):
                    nodo_viejo = nodo
                    nodo = i
                    break
    return nodo


#Create the tree
g = nx.Graph()

#Create the edges
for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2])

#Crea the nodes
for i, node in nodelist.iterrows():
    g.add_node(node[0])


#What do you want to do?

userInput = input('English_to_morse (1), Morse_to_English (2):')
if userInput == '1':
    Text_English = input("Input the words to translate to morse : ")
    Text_English = Text_English.upper()
    Text_English_Palabras = Text_English.split(" ")

    for palabras in Text_English_Palabras:
        letras = list(palabras)
        for letra in letras:
            translate_to_morse(letra)
        print(' ')

elif userInput == '2':
    Text_morse = input("Input the morse code to translate to english: ")
    Text_morse_letras = Text_morse.split(" ")
    for letras in Text_morse_letras:
        letra = translate_to_english(letras)
        print(letra)
