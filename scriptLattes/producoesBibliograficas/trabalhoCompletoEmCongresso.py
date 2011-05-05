#!/usr/bin/python
# encoding: utf-8
# filename: trabalhoCompletoEmCongresso.py

from scriptLattes import *
from geradorDePaginasWeb import *
import re

class TrabalhoCompletoEmCongresso:
	item = None # dado bruto
	idMembro = None

	relevante = None
	autores = None
	titulo = None
	nomeDoEvento = None
###	tituloDosAnais = None
	ano = None
	volume = None
	paginas = None
	chave = None

	def __init__(self, idMembro, partesDoItem='',  relevante=''):
		self.idMembro = set([])
		self.idMembro.add(idMembro)

		if not partesDoItem=='': 
			# partesDoItem[0]: Numero (NAO USADO)
			# partesDoItem[1]: Descricao do livro (DADO BRUTO)

			self.item = partesDoItem[1]
			self.relevante = relevante

			# Dividir o item na suas partes constituintes
			partes = self.item.partition(" . ")
			self.autores = partes[0].strip()
			partes = partes[2]
	
			partes = partes.rpartition(" p. ")
			if partes[1]=='': # se nao existem paginas
				self.paginas = ''
				partes = partes[2]
			else:
				self.paginas = partes[2].rstrip(".").rstrip(",")
				partes = partes[0]
			
			partes = partes.rpartition(" v. ")
			if partes[1]=='': # se nao existem informacao de volume
				self.volume = ''
				partes = partes[2]
			else:
				self.volume = partes[2].rstrip(".").rstrip(",")
				partes = partes[0]
	
			aux = re.findall(u', ((?:19|20)\d\d)\\b', partes)
		
			if len(aux)>0:
				partes = partes.rpartition(",")
				self.ano = aux[-1].strip().rstrip(".").rstrip(",")
				partes = partes[0]
			else:
				self.ano = ''

	###		partes = partes.rpartition(". ")
	###		self.tituloDosAnais = partes[2].strip().rstrip('.').rstrip(",")
	###		partes = partes[0]
	
			partes = partes.rpartition(" In: ")
			if partes[1]=='': # se nao existe nome do evento
				self.nomeDoEvento = ''
				partes = partes[2]
			else:
				self.nomeDoEvento = partes[2].strip().rstrip(".")
				partes = partes[0]
	
			self.titulo = partes.strip().rstrip(".")
			self.chave = self.autores # chave de comparação entre os objetos

		else:
			self.relevante = ''
			self.autores = ''
			self.titulo = ''
			self.nomeDoEvento = ''
			self.ano = ''
			self.volume = ''
			self.paginas = ''


	def compararCom(self, objeto):
		if self.idMembro.isdisjoint(objeto.idMembro) and compararCadeias(self.titulo, objeto.titulo):
			# Os IDs dos membros são agrupados. 
			# Essa parte é importante para a criação do GRAFO de colaborações
			self.idMembro.update(objeto.idMembro)

			if len(self.autores)<len(objeto.autores):
				self.autores = objeto.autores

			if len(self.titulo)<len(objeto.titulo):
				self.titulo = objeto.titulo

			if len(self.nomeDoEvento)<len(objeto.nomeDoEvento):
				self.nomeDoEvento = objeto.nomeDoEvento

			if len(self.volume)<len(objeto.volume):
				self.volume = objeto.volume

			if len(self.paginas)<len(objeto.paginas):
				self.paginas = objeto.paginas

			return self
		else: # nao similares
			return None


	def html(self, listaDeMembros):
		s = self.autores + '. <b>' + self.titulo + '</b>. '

		s+= 'Em: ' + self.nomeDoEvento + ', '  if not self.nomeDoEvento==''  else ''
		s+= 'v. ' + self.volume + ', '  if not self.volume==''  else ''
		s+= 'p. ' + self.paginas + ', ' if not self.paginas=='' else ''
		s+= str(self.ano) + '.'         if str(self.ano).isdigit() else '.'

 		s+= menuHTMLdeBuscaPB(self.titulo)
		return s



	def ris(self):
		paginas = self.paginas.split('-')
		if len(paginas)<2:
			p1 = self.paginas
			p2 = ''
		else:
			p1 = paginas[0]
			p2 = paginas[1]
		s = '\n'
		s+= '\nTY  - CONF'
		s+= '\nAU  - '+self.autores
		s+= '\nT1  - '+self.titulo
		s+= '\nTI  - '+self.nomeDoEvento
		s+= '\nVL  - '+self.volume
		s+= '\nSP  - '+p1
		s+= '\nEP  - '+p2
		s+= '\nPY  - '+str(self.ano)
		s+= '\nER  - '
		return s


	# ------------------------------------------------------------------------ #
	def __str__(self):
		s  = "\n[TRABALHO COMPLETO PUBLICADO EM CONGRESSO] \n"
		s += "+ID-MEMBRO   : " + str(self.idMembro) + "\n"
		s += "+RELEVANTE   : " + str(self.relevante) + "\n"
		s += "+AUTORES     : " + self.autores.encode('utf8','replace') + "\n"
		s += "+TITULO      : " + self.titulo.encode('utf8','replace') + "\n"
		s += "+NOME EVENTO : " + self.nomeDoEvento.encode('utf8','replace') + "\n"
###		s += "+ANAIS       : " + self.tituloDosAnais.encode('utf8','replace') + "\n"
		s += "+ANO         : " + str(self.ano) + "\n"
		s += "+VOLUME      : " + self.volume.encode('utf8','replace') + "\n"
		s += "+PAGINAS     : " + self.paginas.encode('utf8','replace') + "\n"
###		s += "+item        : @@" + self.item.encode('utf8','replace') + "@@\n"
		return s
