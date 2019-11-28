#coding: utf-8

import csv
from deputado import *
from vetor import *
from main import *

'''
Leitura e manipulação do arquivo
'''

def ler_votacao(path):

	f = open(path, 'r')
	csv_file = csv.reader(f)
	headers = next(csv_file, None)

	voting_dict = {}

	for row in csv_file:
		dep_nome = row[0]
		dep_estado = row[1]
		dep_partido = row[2]
		dep_votos = list(map(int, row[3:len(row)]))
		voting_dict[dep_nome] = Deputado(dep_nome, dep_estado, dep_partido, Vetor(dep_votos))

	return voting_dict

print(ler_votacao("../data/exemplo.csv"))
x = Deputado("teste", "pb", "mito", [5, 10])

y = Deputado("biu", "tttb", "wwww", [10, 10])
p = {"teste":x, "biu":y}
print(p["teste"].votos)
print(comparar("teste", "biu",{"teste":x, "biu":y}))
