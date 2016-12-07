
from sys import argv

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
	dicionarios = [{} for x in range(k)] #Lista de dicionario de valor menor ou igual ao k para o inicio do texto
	
	charCount = 0 #Quantas palavras para limitar o tamanho do texto de saida

	with open(fileName, "r") as file:
		
		lido = readWord(file, k)
		
		while len(lido) > 0:
			
			charCount +=1
			print len(lido)
			for i in xrange(len(lido)-1): # TODO: Mudar para pegar nivel 0 tbm
				dicionario = dicionarios[i]
				key, value = sliceKeyValue(lido, i)
				addValueToDic(dicionario, key, value)

			lido = readWord(file, k)
	
	return dicionarios, charCount

def main(args):
	k = int(args[1])
	inFileName = args[2]
	entrada, charCount = readIn(inFileName, k)


if __name__ == '__main__':
	main(argv)