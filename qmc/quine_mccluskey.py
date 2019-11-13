from . import patrick

def checkerInput(truthTable):
	if truthTable == []:
		return 'Empty entry'
	elif len(truthTable) == truthTable.count('1'):
		return '1'
	elif not bits(truthTable):
		return 'Invalid input'
	for e in truthTable:
		if e != '0' and e != '1' and e.lower() != 'x':
			return 'Invalid input'
	if truthTable.count('1') == 0:
		return '0'
	return True
	
def bits(truthTable):
	n = 1
	while n < len(truthTable):
		if 2**n == len(truthTable):
			return n
		n += 1
	return 0

def minimalBooleanExpression(extractedPrimes):
	expression = []
	for primes in extractedPrimes:
		prime = ''
		for i in range(len(primes)):
			if primes[i] == '1':
				if prime != '':
					prime += '.'
				prime += chr(65+i)
			elif primes[i] == '0':
				if prime != '':
					prime += '.'
				prime += chr(65+i)+"'"
		expression.append(prime)
	minimalExpression = ''
	for i in range(len(expression)-1):
		minimalExpression += "({})+".format(expression[i])
	minimalExpression += "({})".format(expression[-1])
	
	return minimalExpression
	
def criarMinitermos(bits, truthTable):
    listaMinitermos = []

    for i in range(len(truthTable)):
        if truthTable[i] == '1' or truthTable[i] == 'x':
            minitermo = format(i, '0' + str(bits) + 'b')
            listaMinitermos.append(minitermos(minitermo, i))

    return listaMinitermos


class minitermos():
    def __init__(self, implicanteBin, implicanteCompared):
        self.compared = False
        self.implicanteBin = implicanteBin
        self.implicanteCompared = implicanteCompared


def separateIntoGroups1s(minitermos):
    grups1s = [list() for l in range(len(minitermos[0].implicanteBin) + 1)]

    for obj in minitermos:
        indice = obj.implicanteBin.count('1')
        grups1s[indice].append(obj)

    while [] in grups1s:
        grups1s.pop(grups1s.index([]))

    return grups1s


def comparasionMiniterm(miniterm1, miniterm2):
    difference = 0
    miniterm1plus2 = ''

    for i in range(len(miniterm1.implicanteBin)):

        if miniterm1.implicanteBin[i] != miniterm2.implicanteBin[i]:
            difference += 1
            miniterm1plus2 += '-'
        else:
            miniterm1plus2 += miniterm1.implicanteBin[i]
    if difference == 1:
        miniterm1.compared = True
        miniterm2.compared = True

        implicante = minitermos(miniterm1plus2, str(miniterm1.implicanteCompared) + ',' + str(miniterm2.implicanteCompared))
        return implicante


def comparasion(primeImplicants):
    implicantsCompared = []

    for i in range(len(primeImplicants) - 1):
        for e1 in primeImplicants[i]:
            for e2 in primeImplicants[i + 1]:

                newTerm = comparasionMiniterm(e1, e2)

                if newTerm != None:
                    implicantsCompared.append(newTerm)

    for l in primeImplicants:
        for obj in l:
            if obj.compared == False:
                implicantsCompared.append(obj)
    repit = True
    while repit:
        repit = False
        for obj in implicantsCompared:
            for obj2 in implicantsCompared:
                if str(obj.implicanteBin) == str(obj2.implicanteBin) and obj != obj2:
                    implicantsCompared.pop(implicantsCompared.index(obj2))
                    repit = True

    return implicantsCompared


def primeImplicantChart(miniterms, implicants):
    Map = {}
    chartIndice = [" " for s in range(len(miniterms))]

    for e in implicants:
        Map[e.implicanteBin] = chartIndice[:]

        for i in range(len(miniterms)):
            implicantCompare = str(e.implicanteCompared).split(',')
            if str(miniterms[i].implicanteCompared) in implicantCompare:
                Map[e.implicanteBin][i] = 'O'

    return Map


def essentialPrimeImplicants(miniterms):
    groups = separateIntoGroups1s(miniterms)
    comparasionGroups = comparasion(groups)
    if comparasionGroups == miniterms:
        return comparasionGroups
    return essentialPrimeImplicants(comparasionGroups)


def reducePrimeImplicantChart(mapa, miniterms, implicants):
    indices = []
    essentialPrime = []
    lastInd = ''
    
    while mapa != {}:
        iteration = 0
        if len(mapa[list(mapa.keys())[0]]) == 1:
            for key in mapa:
                if mapa[key][0] == 'O':
                    essentialPrime.append(key)

        for x in range(len(mapa[list(mapa.keys())[0]])):
            l = []
            for y in mapa:
                l.append(mapa[y][x])
                if mapa[y][x] == 'O':
                    lastInd = y
            if l.count('O') == 1:
                indices.append(x)
                if lastInd not in essentialPrime and lastInd != '':
                    essentialPrime.append(lastInd)
            else:
                iteration += 1
        indices.sort()
        indices.reverse()
        for e in essentialPrime:
            if e in mapa:
                while 'O' in mapa[e]:
                    ind = mapa[e].index('O')
                    for key in mapa:
                        mapa[key].pop(ind)
        for e in essentialPrime:
            try:
                del(mapa[e])
            except KeyError:
                continue
                
        if mapa != {}:
            if iteration == len(mapa[list(mapa.keys())[0]]):
                break
            
        primeRep = []
        for key in mapa:
            for key2 in mapa:
                if key != key2 and mapa[key] == mapa[key2]:
                    primeRep.append(key)
                    
        primeRep = list(set(primeRep))
        for i in range(len(primeRep)-1):
            del(mapa[primeRep[i]])
            
    if mapa != {}:
        essentialPrime += patrick.extractPatrickImplicants(mapa)

    return minimalBooleanExpression(essentialPrime)

def main(truthTable):
	verificationInput = checkerInput(truthTable)
	if verificationInput == True:
		miniterms = criarMinitermos(bits(truthTable), truthTable)
		implicants = essentialPrimeImplicants(miniterms)
		mapa = primeImplicantChart(miniterms, implicants)
		return reducePrimeImplicantChart(mapa, miniterms, implicants)
	return verificationInput
