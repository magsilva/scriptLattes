#!/usr/bin/python
# encoding: utf-8
# filename: areasDeAtuacao.py

class AreaDeAtuacao:
	descricao = ''

	def __init__(self, partesDoItem):
		# partesDoItem[0]: Número do item (NAO usado)
		# partesDoItem[1]: Descricao da Area de Atuacao
		self.descricao = partesDoItem[1].strip()

	# ------------------------------------------------------------------------ #
	def __str__(self):
		s  = "[AREAS DE ATUACAO] \n"
		s += "+DESCRICAO   : " + self.descricao.encode('utf8','replace') + "\n"
		return s
