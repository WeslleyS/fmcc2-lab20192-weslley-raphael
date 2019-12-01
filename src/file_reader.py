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


#print(ler_votacao("../data/exemplo.csv"))


x = Deputado("teste", "PB", "PSOL", Vetor([1, 1, 1, 1]))
y = Deputado("biu", "PB", "PSDB", Vetor([-1, -1, -1, 1]))
z = Deputado("irineu", "AM", "PT", Vetor([1, 1, 0, 0]))
f = Deputado("joao", "AM", "PT", Vetor([1, 1, 1, 1]))
p = {"teste":x, "biu":y, "irineu": z, "joao": f}
p["oi"] = []
#print(amigos_adocicados(p))
p['oi'].append(2)
p['oi'].append(3)
#print(p)

l =  ["irineu", "biu", "teste"]
#print(encontra_registro_medio(l, p))
#print(menos_similar("teste", p))

a = Vetor([2,2])
b = Vetor([9,8])
#print(b / (3))



