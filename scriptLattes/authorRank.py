#!/usr/bin/python
# encoding: utf-8
# filename: authorRank.py

import numpy

class AuthorRank:
	matriz = None
	vectorRank = None

	def __init__(self, matriz, iteracoes):
		self.matriz = matriz
		self.vectorRank = numpy.ones( len(matriz), dtype=numpy.float32)

		print "[CALCULANDO AUTHOR-RANK (PROCESSO ITERATIVO)]"
		for index in range(0,iteracoes):
			self.vectorRank = self.calcularRanks(self.vectorRank)


	def calcularRanks(self, vectorRank):
		vectorRankNovo = numpy.zeros( len(vectorRank), dtype=numpy.float32)
		d = 0.85 # dumping factor (fator de amortecimento)

		for i in range(0, len(vectorRank)):
			soma = 0
			for j in range(0, len(vectorRank)):
				soma += vectorRank[j] * self.matriz[j][i]
			vectorRankNovo[i] = (1-d) + d*soma

		return vectorRankNovo

