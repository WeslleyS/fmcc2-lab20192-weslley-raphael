#coding: utf-8

from deputado import *
from vetor import *

matriculas = ["119110413", "119111241", ""] #Preencham suas matrículas dentro desta variável

'''
Tarefa 02 - Comparar o alinhamento de dois deputados
A função abaixo recebe o nome de dois deputados e o
dicionário mapeando o nome do deputado com seu objeto
da classe Deputado, e retorna o produto interno representando
o grau de similaridade entre a política de voto dos dois deputados dados.
'''
def comparar(dep_a, dep_b, deputados):
	return (Vetor(deputados[dep_a].votos) * Vetor(deputados[dep_b].votos)).soma_elementos()

'''
Tarefa 03 - Encontrar o deputado mais similar com um deputado dado
A função deve receber o nome de um deputado e o dicionário mapeando
o nome do deputado com seu objeto da classe Deputado, e o nome do deputado 
mais similar ao que foi dado como entrada. No caso, de haver mais de um
deputado com o grau de similaridade máxima, todos os nomes devem ser retornados
em uma lista.
'''
def mais_similar(dep, deputados):
	deputados_similares = []
	grau_similaridade = 0
	votos_deputadado = deputados[dep].votos

	for e in deputados:
		grau_temporario = (deputados[dep].votos * deputados[e].votos).soma_elementos()

		if grau_temporario > grau_similaridade and e != dep:
			deputados_similares = []
			grau_similaridade = grau_temporario
			deputados_similares.append(e)
		elif grau_temporario == grau_similaridade and e != dep:
			deputados_similares.append(e)

	if len(deputados_similares) == 1:
		return deputados_similares[0]

	return deputados_similares

'''
Tarefa 04 - Encontrar o deputado menos similar com um deputado dado
Similar a tarefa 03, porém deve retornar o nome do deputado menos similar
ou uma lista com todos os nomes, em caso de empate.
'''
def menos_similar(dep, deputados):
	deputados_pouco_similares = []
	grau_similaridade = 867
	votos_deputadado = deputados[dep].votos

	for e in deputados:
		grau_temporario = (deputados[dep].votos * deputados[e].votos).soma_elementos()

		if grau_temporario < grau_similaridade and e != dep:
			deputados_pouco_similares = []
			grau_similaridade = grau_temporario
			deputados_pouco_similares.append(e)
		elif grau_temporario == grau_similaridade and e != dep:
			deputados_pouco_similares.append(e)

	if len(deputados_pouco_similares) == 1:
		return deputados_pouco_similares[0]

	return deputados_pouco_similares

'''
Tarefa 05 - Implementar a função encontra_similaridade_media(dep, dep_set, deputados)
que, dado o nome de um deputado, compara seu registro de votos com o registro de votos
com todos os deputados cujos nomes estão em dep_set, computando um produto interno para
cada, e então retornando o produto interno médio.
'''
def encontra_similaridade_media(dep, dep_set, deputados):
	soma = 0.0
	for e in dep_set:
		soma += comparar(dep, e, deputados)
	
	return soma / len(dep_set)

'''
Tarefa 06 - Implemente a função encontra_registro_medio(dep_set, voting_dict) que,
dado um conjunto com o nome dos deputados, encontre a média do registro de votação.
Isto é, realize adição vetorial na listas representando o registro de suas votações,
e então divida a soma pelo número de vetores. O resultado deve ser um vetor.
'''
def encontra_registro_medio(dep_set, deputados):
	vetorResposta = deputados[dep_set[0]].votos * 0
	
	for e in dep_set:
		vetorResposta = vetorResposta + Vetor(deputados[e].votos)
		
	return vetorResposta / len(dep_set)

'''
Tarefa 07 - Implemente as funções a seguir
- registro_medio_partido(partido, deputados) que, dado o nome de um partido 
  encontra o registro médio de votação deste partido;
- registro_medio_estado(estado, deputados) que, dado o nome de um estado do
  Brasil encontra o registro médio de votação deste estado;
- registro_medio_regiao(regiao, deputados) que, dada o nome de uma região do
  Brasil encontra o registro médio de votação desta região.
  Considere os nomes da regiões brasileiras sendo NORTE, SUL, SUDESTE, NORDESTE e CENTRO-OESTE
O retorno de todas as funções descritas nesta tarefa deve ser um vetor.
'''

def registro_medio_partido(partido, deputados):
	deputadosDoPartido = []
	for e in deputados:
		if deputados[e].partido == partido:
			deputadosDoPartido.append(e)
			
	return encontra_registro_medio(deputadosDoPartido, deputados)
    
def registro_medio_estado(estado, deputados):
	deputadosDoEstado = []
	for e in deputados:
		if deputados[e].estado == estado:
			deputadosDoEstado.append(e)
			
	return encontra_registro_medio(deputadosDoEstado, deputados)
    
    
def registro_medio_regiao(regiao, deputados):
	regioes_estados = {'DF': 'CENTRO-OESTE', 'BA': 'NORDESTE', 'PR': 'SUL', 'RR': 'NORTE', 'RS': 'SUL', 'PB': 'NORDESTE', 'TO': 'NORTE', 'PA': 'NORTE', 'PE': 'NORDESTE', 'RN': 'NORDESTE', 'RO': 'NORTE', 'RJ': 'SUDESTE', 'AC': 'NORTE', 'AM': 'NORTE', 'AL': 'NORDESTE', 'CE': 'NORDESTE', 'AP': 'NORTE', 'GO': 'CENTRO-OESTE', 'ES': 'SUDESTE', 'MG': 'SUDESTE', 'PI': 'NORDESTE', 'MA': 'NORDESTE', 'SP': 'SUDESTE', 'MT': 'CENTRO-OESTE', 'MS': 'CENTRO-OESTE', 'SC': 'SUL', 'SE': 'NORDESTE'}

	deputadosDaRegiao = []
	for e in deputados:
		if regioes_estados[deputados[e].estado] == regiao:
			deputadosDaRegiao.append(e)
			
	return encontra_registro_medio(deputadosDaRegiao, deputados)

'''
Tarefa 08 - Implemente as funções a seguir:
- similaridade_no_partido(dep, deputados) que,
  dado o nome de um deputado encontra o grau de similaridade dele com seu partido.
- similaridade_no_estado(dep, deputados) que,
  dado o nome de um deputado encontra o grau de similaridade dele com seu estado.
- similaridade_na_regiao(dep, deputados) que,
  dado o nome de um deputado encontra o grau de similaridade dele com sua regiao.
Para as funções acima o retorno deve ser o respectivo grau de similaridade.
- encontra_mais_alinhado_partido(partido, deputados) que,
  dado o nome de um partido encontra o deputado mais similar ao partido.
  
Para a função acima o retorno deve ser uma lista contendo o nome do deputado e seu respectivo
grau de similaridade.
'''

def similaridade_no_partido(dep, deputados):
	partido = deputados[dep].partido
	deputadosDoPartido = []
	for e in deputados:
		if deputados[e].partido == partido:
			deputadosDoPartido.append(e)
			
	return encontra_similaridade_media(dep, deputadosDoPartido, deputados)
	

def similaridade_no_estado(dep, deputados):
	estado = deputados[dep].estado
	deputadosDoEstado = []
	for e in deputados:
		if deputados[e].estado == estado:
			deputadosDoEstado.append(e)
			
	return encontra_similaridade_media(dep, deputadosDoEstado, deputados)

def similaridade_na_regiao(dep, deputados):
	regioes_estados = {'DF': 'CENTRO-OESTE', 'BA': 'NORDESTE', 'PR': 'SUL', 'RR': 'NORTE', 'RS': 'SUL', 'PB': 'NORDESTE', 'TO': 'NORTE', 'PA': 'NORTE', 'PE': 'NORDESTE', 'RN': 'NORDESTE', 'RO': 'NORTE', 'RJ': 'SUDESTE', 'AC': 'NORTE', 'AM': 'NORTE', 'AL': 'NORDESTE', 'CE': 'NORDESTE', 'AP': 'NORTE', 'GO': 'CENTRO-OESTE', 'ES': 'SUDESTE', 'MG': 'SUDESTE', 'PI': 'NORDESTE', 'MA': 'NORDESTE', 'SP': 'SUDESTE', 'MT': 'CENTRO-OESTE', 'MS': 'CENTRO-OESTE', 'SC': 'SUL', 'SE': 'NORDESTE'}
	regiao = regioes_estados[deputados[dep].estado]
	deputadosDaRegiao = []
	for e in deputados:
		if regioes_estados[deputados[e].estado] == regiao:
			deputadosDaRegiao.append(e)
			
	return encontra_similaridade_media(dep, deputadosDaRegiao, deputados)

def encontra_mais_alinhado_partido(partido, deputados):
	deputadosDoPartido = []
	for e in deputados:
		if deputados[e].partido == partido:
			deputadosDoPartido.append(e)
			
	similaridade = 0
	nome = ""
	for e in deputados:
		similaridade_media = encontra_similaridade_media(e, deputadosDoPartido, deputados)
		if similaridade_media > similaridade:
			similaridade = similaridade_media
			nome = deputados[e].nome
	
	resposta = [nome, similaridade]
	return resposta

'''
Tarefa 09 - Implemente as funções a seguir:
- rivais_amargos(deputados) que encontra os dois deputados menos similares do conjunto inteiro.
- amigos_adocicados(deputados) que encontra os dois deputados mais similares do conjunto inteiro.
O retorno deve ser uma lista contendo os nomes dos dois deputados.
'''

def rivais_amargos(deputados):
	resposta = []
	similaridade = 867
	for e in deputados:
		for x in deputados:
			grau_temporario = (deputados[e].votos * deputados[x].votos).soma_elementos()
			if grau_temporario < similaridade and x != e:
				resposta = []
				similaridade = grau_temporario
				resposta.append(e)
				resposta.append(x)	
	return resposta
	
	
def amigos_adocicados(deputados):
	resposta = []
	similaridade = 0
	for e in deputados:
		for x in deputados:
			grau_temporario = (deputados[e].votos * deputados[x].votos).soma_elementos()
			if grau_temporario > similaridade and x != e:
				resposta = []
				similaridade = grau_temporario
				resposta.append(e)
				resposta.append(x)	
	return resposta

'''
Tarefa 10 - Implemente as funções a seguir:
- encontra_partido_mais_coerente(deputados) que encontra o partido
  cujos congressistas são mais similares entre si, ou seja, cuja média das
  similaridades entre cada deputado é a maior.
- encontra_partido_menos_coerente(deputados) que encontra o partido
  cujos congressistas são menos similares entre si, ou seja, cuja média das
  similaridades entre cada deputado é a menor.
  
O retorno, para ambas, deve ser o nome do partido.
'''

def encontra_partido_mais_coerente(deputados):
	partidos = {}
	similaridade = 0
	nome_partido = ""
	for e in deputados:
		if deputados[e].partido in partidos:
			partidos[deputados[e].partido].append(e)
		else:
			partidos[deputados[e].partido] = []
			partidos[deputados[e].partido].append(e)
	
	for partido in partidos:
		vetor = []
		for e in deputados[partidos[partido][0]].votos:
			vetor.append(1)
		vetor = Vetor(vetor)
		for deputado in partidos[partido]:
			vetor = vetor * deputados[deputado].votos
		
		if vetor.soma_elementos() > similaridade:
			similaridade = vetor.soma_elementos()
			nome_partido = partido
	return nome_partido
    
def encontra_partido_menos_coerente(deputados):
	partidos = {}
	similaridade = 867
	nome_partido = ""
	for e in deputados:
		if deputados[e].partido in partidos:
			partidos[deputados[e].partido].append(e)
		else:
			partidos[deputados[e].partido] = []
			partidos[deputados[e].partido].append(e)
	
	for partido in partidos:
		vetor = []
		for e in deputados[partidos[partido][0]].votos:
			vetor.append(1)
		vetor = Vetor(vetor)
		for deputado in partidos[partido]:
			vetor = vetor * deputados[deputado].votos
		
		if vetor.soma_elementos() < similaridade:
			similaridade = vetor.soma_elementos()
			nome_partido = partido
	return nome_partido
