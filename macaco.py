
from sys import argv
from random import choice

def addValueToDic(dicionario, key, value):
	if not key in dicionario:
		dicionario[key] = []
	dicionario[key].append(value)

def readWord(file, k):
	lido = file.read(k+1)
	file.seek(-len(lido)+1, 1)
	return lido

def sliceKeyValue(lido, i):
	return lido[:i+1], lido[i+1]

def readIn(fileName, k):
	dicionarios = [{} for x in range(k)] #Lista de dicionario de valor menor ou igual a k
	dicionario0 = []
	charCount = 0 #Quantas palavras para limitar o tamanho do texto de saida

	with open(fileName, "r") as file:
		
		lido = readWord(file, k)
		
		while len(lido) > 0:
			dicionario0.append(lido[0]) #Para o nivel 0
			charCount +=1
			for i in xrange(len(lido)-1): 
				dicionario = dicionarios[i]
				key, value = sliceKeyValue(lido, i)
				addValueToDic(dicionario, key, value)

			lido = readWord(file, k)
	
	return dicionarios, dicionario0, charCount

def geraAtual(anterior, dicionariosEntrada, dicionarioNivel0):
	copia = anterior[:]
	while len(copia) > 0 and not copia in dicionariosEntrada[len(copia)-1]: #verifica qual a maior palavra pode ser avaliada nos dicionarios
		copia = copia[1:]
	if len(copia) > 0:
		atual = choice(dicionariosEntrada[len(copia)-1][copia]) 
	else:
		atual = nivel0(dicionarioNivel0) #se naum conseguiu achar em nenhum dicionario, coloca uma como no nivel 0
	anterior += atual
	return atual, anterior

def writeOut(fileName, dicionariosEntrada, dicionarioNivel0, k, size):
	with open(fileName, "w") as file:
		anterior = nivel0(dicionarioNivel0)
		file.write(anterior)
		if k > 0:

			indice = 1

			for i in xrange(1, k): # Incrementa as palavras ate alcancar o tamanho k
				
				atual, anterior = geraAtual(anterior, dicionariosEntrada, dicionarioNivel0)
				
				indice = i
				file.write(atual)
				file.flush()
			
			for i in xrange(indice + 1, size): # Para de incrementar as palavras e so desloca
				
				atual, anterior = geraAtual(anterior, dicionariosEntrada, dicionarioNivel0)
				
				anterior = anterior[1:]
				file.write(atual)
				file.flush()

		else:
			
			for i in xrange(1,size): # Nivel 0
				file.write(nivel0(dicionarioNivel0))
				file.flush()

def nivel0(dicionarioNivel0):
	return choice(dicionarioNivel0)

def main(args):
	
	if len(args) < 4:
		print "Erro de argumentos! Execucao correta: python macaco.py <k> <arquivo de entrada> <arquivo de saida>"
		exit()
	
	k = int(args[1])
	inFileName = args[2]
	outFileName = args[3]
	
	entrada, nivel0, charCount = readIn(inFileName, k)
	
	writeOut(outFileName, entrada, nivel0, k, charCount)


if __name__ == '__main__':
	main(argv)