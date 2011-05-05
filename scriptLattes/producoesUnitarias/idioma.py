#!/usr/bin/python
# encoding: utf-8
# filename: idioma.py

class Idioma:
	descricao = ''

	def __init__(self, partesDoItem):
		# partesDoItem[0]: Nome do idioma
		# partesDoItem[1]: Descricao da proficiencia do idioma
		self.nome = partesDoItem[0].strip()
		self.proficiencia = partesDoItem[1].strip()


	# ------------------------------------------------------------------------ #
	def __str__(self):
		s  = "\n[IDIOMA] \n"
		s += "+NOME        : " + self.nome.encode('utf8','replace') + "\n"
		s += "+PROFICIENCIA: " + self.proficiencia.encode('utf8','replace') + "\n"
		return s
