#!/usr/bin/python
# encoding: utf-8
# filename: projetoDePesquisa.py

from scriptLattes import *
from geradorDePaginasWeb import *
import datetime

class ProjetoDePesquisa:
	idMembro = None
	anoInicio = None
	anoConclusao = None
	nome = ''
	descricao = ''
	chave = None
	ano = None

	def __init__(self, idMembro, partesDoItem):
		# partesDoItem[0]: Periodo do projeto de pesquisa
		# partesDoItem[1]: cargo e titulo do projeto
		# partesDoItem[2]: NULL
		# partesDoItem[3]: Descricao (resto)

		self.idMembro = list([])
		self.idMembro.append(idMembro)

		anos =  partesDoItem[0].partition(" - ")
		self.anoInicio = anos[0]
		self.anoConclusao = anos[2]

		# detalhe = partesDoItem[1].rpartition(":")
		#self.cargo = detalhe[0].strip()
		#self.nome = detalhe[2].strip()
		self.nome = partesDoItem[1]

		self.descricao= list([])
		self.descricao.append(partesDoItem[3])

		self.chave = self.nome # chave de comparação entre os objetos

		self.ano = self.anoInicio # para comparação entre objetos


	def html(self, listaDeMembros):
		if self.anoConclusao==datetime.datetime.now().year:
			self.anoConclusao = 'Atual'
		if self.anoInicio==0 and self.anoConclusao==0:
			s = '<span class="projects"> (*) </span> '
		else:
			s = '<span class="projects">' + str(self.anoInicio) + '-' + str(self.anoConclusao) + '</span>. '
		s+= '<b>' + self.nome + '</b>'


		for i in range(0, len(self.idMembro)):
			s+= '<br><i><font size=-1>'+ self.descricao[i] +'</font></i>'
			m = listaDeMembros[ self.idMembro[i] ]
			s+= '<br><i><font size=-1>Membro: <a href="'+m.url+'">'+m.nomeCompleto+'</a>.</font>'

		return s


	def compararCom(self, objeto):
		if set(self.idMembro).isdisjoint(set(objeto.idMembro)) and compararCadeias(self.nome, objeto.nome):
			# Os IDs dos membros são agrupados. 
			# Essa parte é importante para a geracao do relorio de projetos
			self.idMembro.extend(objeto.idMembro)

			self.descricao.extend(objeto.descricao) # Apenas juntamos as descrições

			return self
		else: # nao similares
			return None
	


	# ------------------------------------------------------------------------ #
	def __str__(self):
		s  = "\n[PROJETO DE PESQUISA] \n"
		s += "+ID-MEMBRO   : " + str(self.idMembro) + "\n"
		s += "+ANO INICIO  : " + str(self.anoInicio) + "\n"
		s += "+ANO CONCLUS.: " + str(self.anoConclusao) + "\n"
		s += "+NOME        : " + self.nome.encode('utf8','replace') + "\n"
		s += "+DESCRICAO   : " + str(self.descricao).encode('utf8','replace') + "\n"
		return s

