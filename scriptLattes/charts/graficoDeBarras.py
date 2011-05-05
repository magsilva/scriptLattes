#!/usr/bin/python
# encoding: utf-8
# filename: graficoDeBarras.py

import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use("Agg")
	
class GraficoDeBarras:
	diretorioDeSaida = None
	listaCompleta = None
	prefixo = None
	titulo = None

	def __init__(self, diretorioDeSaida):
		self.diretorioDeSaida = diretorioDeSaida

	
	def criarGrafico(self, listaCompleta, prefixo, titulo):
		self.listaCompleta = []
		self.listaCompleta = listaCompleta
		self.prefixo = prefixo
		self.titulo = titulo


		vetorDeAnos = []
		vetorDeQuantidades = []

		keys = self.listaCompleta.keys()
		keys.sort(reverse=False) #keys.sort(reverse=True)
		for k in keys:
			if k==0:
				vetorDeAnos.append('*itens sem ano')
			else:
				vetorDeAnos.append(k)

			vetorDeQuantidades.append( len(self.listaCompleta[k]) )

		if len(vetorDeAnos)>0: # Apenas para listas com elemtos
			print "\n[CRIANDO GRAFICO DE BARRAS]"
			print self.prefixo + ": "
			print vetorDeAnos
			print vetorDeQuantidades

			ind = np.arange(len(vetorDeAnos)) 
			bar_width = 0.20

			plt.clf()
			plt.figure(111, figsize=(8.5,3), dpi=80)

			rects = plt.bar(ind, vetorDeQuantidades, color='#006600', edgecolor='#006600')

			plt.ylabel(self.titulo.encode('utf8'), fontsize=10, color='#000099') #, family='sans-serif')
			plt.yticks([])

			plt.xticks(ind+2*bar_width, vetorDeAnos , rotation=90, fontsize=8, color='#000099') #, family='sans-serif')
			#plt.axis('tight')
			old_axis = plt.axis()
			plt.axis([old_axis[0], old_axis[1], 0, max(vetorDeQuantidades)*1.15 ] )

			# rotulos sobre as barras
			for rect in rects:
				height = rect.get_height()
				plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom', fontsize=6, color='#001100')

			plt.savefig(self.diretorioDeSaida+"/"+self.prefixo+'.png', format='png', transparent=False, pad_inches=0.1, bbox_inches='tight')

