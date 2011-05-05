#!/usr/bin/python
# encoding: utf-8
# filename: formacaoAcademica.py


class FormacaoAcademica:
	anoInicio = None
	anoConclusao = None
	tipo = ''
	nomeInstituicao = ''
	descricao = ''

	def __init__(self, partesDoItem):
		# partesDoItem[0]: Periodo da formacao Profissional
		# partesDoItem[1]: Descricao da formacao Profissional

		anos =  partesDoItem[0].partition(" - ")
		self.anoInicio = anos[0];
		self.anoConclusao = anos[2];

		detalhe = partesDoItem[1].partition(".")
		self.tipo = detalhe[0].strip()

		detalhe = detalhe[2].strip().partition(".")
		self.nomeInstituicao = detalhe[0].strip()
		self.descricao = detalhe[2].strip()


	# ------------------------------------------------------------------------ #
	def __str__(self):
		s  = "\n[FORMACAO ACADEMICA] \n"
		s += "+ANO INICIO  : " + self.anoInicio.encode('utf8','replace') + "\n"
		s += "+ANO CONCLUS.: " + self.anoConclusao.encode('utf8','replace') + "\n"
		s += "+TIPO        : " + self.tipo.encode('utf8','replace') + "\n"
		s += "+INSTITUICAO : " + self.nomeInstituicao.encode('utf8','replace') + "\n"
		s += "+DESCRICAO   : " + self.descricao.encode('utf8','replace') + "\n"
		return s
