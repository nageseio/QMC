def extractPatrickImplicants(mapa):
	patrickTerms = {}
	for i in range(len(mapa)):
		patrickTerms[chr(97+i)] = list(mapa.keys())[i]
	
	terms = []
	for x in range(len(mapa[list(mapa.keys())[0]])):
		terms_temp = []
		ylist = []
		for y in mapa:
			ylist.append(mapa[y][x])
		for i in range(len(patrickTerms)):
			if ylist[i] == 'O':
				terms_temp.append(chr(97+i))
		terms += [terms_temp[:]]
	
	implicants = []
	if terms == []:
		return []
	primeImplicants = petrickMethod(terms)
	for e in primeImplicants:
		implicants.append(patrickTerms[str(e)])
	return implicants
		

def minimalExpression(expressions):
	controle = float('inf')
	minimal = ''
	for e in expressions:
		if len(e) < controle:
			minimal = e
			controle = len(e)
	return minimal
	
def minimizeTerm(term):
	termAux = ''
	for e in term:
		if e not in termAux:
			termAux += e
	return termAux
	
def petrickMethod(lista):
	if len(lista) == 1:
		return minimalExpression(lista[0])

	term1 = lista[0]
	term2 = lista[1]
	newTermList = []
	lista.pop(0)
	lista.pop(0)
	for i in term1:
		for i2 in term2:
			if i != i2:
				newTermList.append(minimizeTerm(i+i2))
			elif i == i2 or i in i2 or i2 in i:
				newTermList.append(minimizeTerm(i2))

	lista.append(newTermList)
	return petrickMethod(lista)
