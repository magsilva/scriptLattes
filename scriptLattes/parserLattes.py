#!/usr/bin/python
# encoding: utf-8
# filename: parserLattes.py
#
#  scriptLattes V8
#  Copyright 2005-2011: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
#  http://scriptlattes.sourceforge.net/
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opnião) qualquer versão.
#
#  Este programa é distribuido na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#


import HTMLParser
import re
import string
from tidylib import tidy_document
from htmlentitydefs import name2codepoint

# ---------------------------------------------------------------------------- #
from HTMLParser import HTMLParser
from formacaoAcademica import *
from areaDeAtuacao import *
from idioma import *
from premioOuTitulo import *
from projetoDePesquisa import *

from artigoEmPeriodico import *
from livroPublicado import *
from capituloDeLivroPublicado import *
from textoEmJornalDeNoticia import *
from trabalhoCompletoEmCongresso import *
from resumoExpandidoEmCongresso import *
from resumoEmCongresso import *
from artigoAceito import *
from apresentacaoDeTrabalho import *
from outroTipoDeProducaoBibliografica import *

from softwareComPatente import *
from softwareSemPatente import *
from produtoTecnologico import *
from processoOuTecnica import *
from trabalhoTecnico import *
from outroTipoDeProducaoTecnica import *
from producaoArtistica import *
from orientacaoEmAndamento import *
from orientacaoConcluida import *

from organizacaoDeEvento import *
from participacaoEmEvento import *


class ParserLattes(HTMLParser):
	item = None
	nomeCompleto = ''
	bolsaProdutividade = ''
	enderecoProfissional = ''
	sexo = ''
	nomeEmCitacoesBibliograficas = ''
	atualizacaoCV = ''
	foto = ''
	textoResumo = ''

	salvarNome = None
	salvarBolsaProdutividade = None
	salvarEnderecoProfissional = None
	salvarSexo = None
	salvarNomeEmCitacoes = None
	salvarAtualizacaoCV = None
	salvarTextoResumo = None
	salvarFormacaoAcademica = None
	salvarProjetoDePesquisa = None
	salvarAreaDeAtuacao = None
	salvarIdioma = None
	salvarPremioOuTitulo = None
	salvarItem = None
	salvarParticipacaoEmEvento = None
	salvarOrganizacaoDeEvento = None

	achouGrupo = None
	achouEnderecoProfissional = None
	achouSexo = None
	achouNomeEmCitacoes = None
	achouFormacaoAcademica = None
	achouProjetoDePesquisa = None
	achouAreaDeAtuacao = None
	achouIdioma = None
	achouPremioOuTitulo = None

	achouArtigoEmPeriodico = None
	achouLivroPublicado = None
	achouCapituloDeLivroPublicado = None
	achouTextoEmJornalDeNoticia = None
	achouTrabalhoCompletoEmCongresso = None
	achouResumoExpandidoEmCongresso = None
	achouResumoEmCongresso = None
	achouArtigoAceito = None
	achouApresentacaoDeTrabalho = None
	achouOutroTipoDeProducaoBibliografica = None

	achouSoftwareComPatente = None
	achouSoftwareSemPatente = None
	achouProdutoTecnologico = None
	achouProcessoOuTecnica = None
	achouTrabalhoTecnico = None
	achouOutroTipoDeProducaoTecnica = None
	achouProducaoArtistica = None

	achouOrientacoesEmAndamento	= None
	achouOrientacoesConcluidas = None
	achouSupervisaoDePosDoutorado = None
	achouTeseDeDoutorado = None
	achouDissertacaoDeMestrado = None
	achouMonografiaDeEspecializacao = None
	achouTCC = None
	achouIniciacaoCientifica = None
	achouOutroTipoDeOrientacao = None

	achouParticipacaoEmEvento = None
	achouOrganizacaoDeEvento = None

	procurarCabecalho = None
	partesDoItem = []

	listaIDLattesColaboradores = []
	listaFormacaoAcademica = []
	listaProjetoDePesquisa = []
	listaAreaDeAtuacao = []
	listaIdioma = []
	listaPremioOuTitulo = []

	listaArtigoEmPeriodico = []
	listaLivroPublicado = []
	listaCapituloDeLivroPublicado = []
	listaTextoEmJornalDeNoticia = []
	listaTrabalhoCompletoEmCongresso = []
	listaResumoExpandidoEmCongresso = []
	listaResumoEmCongresso = []
	listaArtigoAceito = []
	listaApresentacaoDeTrabalho = []
	listaOutroTipoDeProducaoBibliografica = []

	listaSoftwareComPatente = []
	listaSoftwareSemPatente = []
	listaProdutoTecnologico = []
	listaProcessoOuTecnica = []
	listaTrabalhoTecnico = []
	listaOutroTipoDeProducaoTecnica = []
	listaProducaoArtistica = []

	# Orientaççoes em andamento (OA)
	listaOASupervisaoDePosDoutorado = []
	listaOATeseDeDoutorado = []
	listaOADissertacaoDeMestrado = []
	listaOAMonografiaDeEspecializacao = []
	listaOATCC = []
	listaOAIniciacaoCientifica = []
	listaOAOutroTipoDeOrientacao = []

	# Orientações concluídas (OC)
	listaOCSupervisaoDePosDoutorado = []
	listaOCTeseDeDoutorado = []
	listaOCDissertacaoDeMestrado = []
	listaOCMonografiaDeEspecializacao = []
	listaOCTCC = []
	listaOCIniciacaoCientifica = []
	listaOCOutroTipoDeOrientacao = []

	# Eventos
	listaParticipacaoEmEvento = []
	listaOrganizacaoDeEvento = []

	# auxiliares
	doi = ''
	relevante = 0
	umaTabela = 0
	idOrientando = None

	# ------------------------------------------------------------------------ #
	def __init__(self, idMembro, cvLattesHTML):
		HTMLParser.__init__(self)

		# inicializacao obrigatoria
		self.idMembro = idMembro
		self.sexo = 'Masculino'

		self.item = ''
		self.listaIDLattesColaboradores = []
		self.listaFormacaoAcademica = []
		self.listaProjetoDePesquisa = []
		self.listaAreaDeAtuacao = []
		self.listaIdioma = []
		self.listaPremioOuTitulo = []

		self.listaArtigoEmPeriodico = []
		self.listaLivroPublicado = []
		self.listaCapituloDeLivroPublicado = []
		self.listaTextoEmJornalDeNoticia = []
		self.listaTrabalhoCompletoEmCongresso = []
		self.listaResumoExpandidoEmCongresso = []
		self.listaResumoEmCongresso = []
		self.listaArtigoAceito = []
		self.listaApresentacaoDeTrabalho = []
		self.listaOutroTipoDeProducaoBibliografica = []

		self.listaSoftwareComPatente = []
		self.listaSoftwareSemPatente = []
		self.listaProdutoTecnologico = []
		self.listaProcessoOuTecnica = []
		self.listaTrabalhoTecnico = []
		self.listaOutroTipoDeProducaoTecnica = []
		self.listaProducaoArtistica = []

		self.listaOASupervisaoDePosDoutorado = []
		self.listaOATeseDeDoutorado = []
		self.listaOADissertacaoDeMestrado = []
		self.listaOAMonografiaDeEspecializacao = []
		self.listaOATCC = []
		self.listaOAIniciacaoCientifica = []
		self.listaOAOutroTipoDeOrientacao = []

		self.listaOCSupervisaoDePosDoutorado = []
		self.listaOCTeseDeDoutorado = []
		self.listaOCDissertacaoDeMestrado = []
		self.listaOCMonografiaDeEspecializacao = []
		self.listaOCTCC = []
		self.listaOCIniciacaoCientifica = []
		self.listaOCOutroTipoDeOrientacao = []

		self.listaParticipacaoEmEvento = []
		self.listaOrganizacaoDeEvento = []


		# inicializacao para evitar a busca exaustiva de algumas palavras-chave
		self.salvarAtualizacaoCV = 1 
		self.salvarFoto = 1
		self.procurarCabecalho = 0
		self.achouGrupo = 0
		self.doi = ''
		self.relevante = 0
		self.idOrientando = ''

		# feed it!
		cvLattesHTML, errors = tidy_document(cvLattesHTML, options={'numeric-entities':1})
		#print errors
		#print cvLattesHTML.encode("utf8")

		## tentativa errada (não previsível)
		# options = dict(output_xhtml=1, add_xml_decl=1, indent=1, tidy_mark=0)
		# cvLattesHTML = str(tidy.parseString(cvLattesHTML, **options)).decode("utf8")

		self.feed(cvLattesHTML)

	# ------------------------------------------------------------------------ #
	def handle_starttag(self, tag, attributes):

		if tag=='p':
			for name, value in attributes:
				if name=='class' and value=='titulo':
					self.salvarNome = 1
					self.item = ''
					break
				if name=='class' and value=='texto':
					self.salvarTextoResumo = 1
					self.item = ''
					break

		if (tag=='br' or tag=='img') and self.salvarNome:
			self.nomeCompleto = stripBlanks(self.item)
			self.item = ''
			self.salvarNome = 0
			self.salvarBolsaProdutividade = 1

		if tag=='span' and self.salvarBolsaProdutividade:
			self.item = ''


		if tag=='table':
			for name, value in attributes:
				if name=='class' and value=='IndicProdTabela':
					self.umaTabela = 1	
					self.item = self.item + ' '
					break

		if tag=='tr':
			if self.umaTabela:
				if self.achouAreaDeAtuacao and not self.salvarAreaDeAtuacao:
					self.salvarAreaDeAtuacao = 1
					self.partesDoItem = []
					self.item = ''
					return

				if self.achouIdioma and not self.salvarIdioma:
					self.salvarIdioma = 1
					self.partesDoItem = []
					self.item = ''
					return

				if self.achouPremioOuTitulo and not self.salvarPremioOuTitulo:
					self.salvarPremioOuTitulo = 1
					self.partesDoItem = []
					self.item = ''
					return


		if tag=='td':
			if self.umaTabela:
				if self.achouFormacaoAcademica and not self.salvarFormacaoAcademica:
					self.salvarFormacaoAcademica = 1
					self.partesDoItem = []
					self.item = ''
					return

				if self.achouProjetoDePesquisa and not self.salvarProjetoDePesquisa:
					self.salvarProjetoDePesquisa = 1
					self.partesDoItem = []
					self.item = ''
					return

				if self.achouParticipacaoEmEvento and not self.salvarParticipacaoEmEvento:
					self.salvarParticipacaoEmEvento = 1
					self.partesDoItem = []
					self.item = ''
					return

				if self.achouOrganizacaoDeEvento and not self.salvarOrganizacaoDeEvento:
					self.salvarOrganizacaoDeEvento = 1
					self.partesDoItem = []
					self.item = ''
					return

				if not self.salvarItem and self.achouGrupo:
					#if self.achouArtigoEmPeriodico or self.achouLivroPublicado or self.achouCapituloDeLivroPublicado or self.achouTextoEmJornalDeNoticia or self.achouTrabalhoCompletoEmCongresso or self.achouResumoExpandidoEmCongresso or self.achouResumoEmCongresso or self.achouArtigoAceito or self.achouApresentacaoDeTrabalho or self.achouOutroTipoDeProducaoBibliografica or \
					#   self.achouSoftwareSemPatente or self.achouProdutoTecnologico or self.achouProcessoOuTecnica or self.achouTrabalhoTecnico or self.achouOutroTipoDeProducaoTecnica:
					self.salvarItem = 1
					self.partesDoItem = []
					self.item = ''
					return


			for name, value in attributes: # procuramos Agrupado
				if name=='class' and u'agrupadorsub' in value:
					self.achouGrupo = 1

					# Resetamos as variaveis!
					self.achouArtigoEmPeriodico = 0
					self.achouLivroPublicado = 0
					self.achouCapituloDeLivroPublicado = 0
					self.achouTextoEmJornalDeNoticia = 0
					self.achouTrabalhoCompletoEmCongresso = 0
					self.achouResumoExpandidoEmCongresso = 0
					self.achouResumoEmCongresso = 0
					self.achouArtigoAceito = 0
					self.achouApresentacaoDeTrabalho = 0
					self.achouOutroTipoDeProducaoBibliografica = 0

					self.achouSoftwareComPatente = 0
					self.achouSoftwareSemPatente = 0
					self.achouProdutoTecnologico = 0
					self.achouProcessoOuTecnica = 0
					self.achouTrabalhoTecnico = 0
					self.achouOutroTipoDeProducaoTecnica = 0
					self.achouProducaoArtistica = 0

					self.achouSupervisaoDePosDoutorado = 0
					self.achouTeseDeDoutorado = 0
					self.achouDissertacaoDeMestrado = 0
					self.achouMonografiaDeEspecializacao = 0
					self.achouTCC = 0
					self.achouIniciacaoCientifica = 0
					self.achouOutroTipoDeOrientacao = 0

					self.salvarItem = 0
					return	

				# resetamos as variaveis para grupos
				if name=='class' and u'AtuaProfTabelaCelula95' in value:
					self.salvarItem = 0
					self.achouGrupo = 0
					return


			if self.salvarFormacaoAcademica or self.salvarProjetoDePesquisa or self.salvarAreaDeAtuacao or self.salvarIdioma or self.salvarPremioOuTitulo or self.salvarParticipacaoEmEvento or self.salvarOrganizacaoDeEvento or self.salvarItem:
				self.item = ''

			if self.achouEnderecoProfissional:
				self.salvarEnderecoProfissional = 1
				self.item = ''
				return

			if self.achouSexo:
				self.salvarSexo = 1
				self.item = ''
				return

			if self.achouNomeEmCitacoes:
				self.salvarNomeEmCitacoes = 1
				self.item = ''
				return

		if tag=='br':
			self.item = self.item + ' '

		if tag=='a':
			if self.salvarItem: # and self.achouArtigoEmPeriodico:
				for name, value in attributes:
					if name=='href' and u'doi' in value:
						self.doi = value
						break

					id = re.findall(u'http://lattes.cnpq.br/(\d{16})', value)
					if name=='href' and len(id)>0:
						self.listaIDLattesColaboradores.append(id[0])
						if self.achouOrientacoesEmAndamento or self.achouOrientacoesConcluidas:
							self.idOrientando = id[0]
						break
			

		if tag=='img':
			if self.salvarFoto: 
				for name, value in attributes:
					if name=='src' and u'servletrecuperafoto' in value:
						self.foto = 'http://buscatextual.cnpq.br'+value
						self.salvarFoto = 0
						break

			if self.salvarItem:
				for name, value in attributes:
					if name=='src' and u'ico_relevante' in value:
						self.relevante = 1
						break

		if tag=='em':
			self.procurarCabecalho = 1
			
			self.salvarFormacaoAcademica = 0 # Desativamos a Lista 1: formacao academica
			self.achouFormacaoAcademica = 0

			self.salvarProjetoDePesquisa = 0 # Desativamos a Lista 2: projetos de pesquisa
			self.achouProjetoDePesquisa = 0

			self.salvarAreaDeAtuacao = 0 # Desativamos a Lista 3: area de atuacao
			self.achouAreaDeAtuacao = 0
			
			self.salvarIdioma = 0 # Desativamos a Lista 4: idioma
			self.achouIdioma = 0

			self.salvarPremioOuTitulo = 0 # Desativamos a Lista 5: premios e titulos
			self.achouPremioOuTitulo = 0

			self.salvarParticipacaoEmEvento = 0
			self.achouParticipacaoEmEvento = 0

			self.salvarOrganizacaoDeEvento = 0
			self.achouOrganizacaoDeEvento = 0

			self.salvarItem = 0 # Desativamos as listas das producoes em C,T&A
			self.achouGrupo = 0


	# ------------------------------------------------------------------------ #
	def handle_endtag(self, tag):
		if tag=='p':
			if self.salvarNome:
 				self.nomeCompleto = stripBlanks(self.item)
				self.salvarNome = 0
			if self.salvarBolsaProdutividade:
				self.salvarBolsaProdutividade = 0

			if self.salvarTextoResumo:
				self.textoResumo = stripBlanks(self.item)
				self.salvarTextoResumo = 0

		if tag=='span' and self.salvarBolsaProdutividade:
			self.bolsaProdutividade = stripBlanks(self.item)
			self.bolsaProdutividade = re.sub('Bolsista de Produtividade em Pesquisa do CNPq - ','', self.bolsaProdutividade)
			self.bolsaProdutividade = self.bolsaProdutividade.strip('()')
			self.salvarBolsaProdutividade = 0
		
		if tag=='table': # para os items armazenados em TABELAS
			self.umaTabela = 0
			
			if self.salvarFormacaoAcademica:
				iessimaFormacaoAcademica = FormacaoAcademica(self.partesDoItem) # criamos um objeto com a lista correspondentes às celulas da linha
				self.listaFormacaoAcademica.append(iessimaFormacaoAcademica) # acrescentamos o objeto de FormacaoAcademica
				self.salvarFormacaoAcademica = 0
				return

			if self.salvarProjetoDePesquisa:
				iessimoProjetoDePesquisa = ProjetoDePesquisa(self.idMembro, self.partesDoItem) # criamos um objeto com a lista correspondentes às celulas da linha
				self.listaProjetoDePesquisa.append(iessimoProjetoDePesquisa) # acrescentamos o objeto de ProjetoDePesquisa
				self.salvarProjetoDePesquisa = 0
				return

			if self.salvarParticipacaoEmEvento:
				self.listaParticipacaoEmEvento.append(ParticipacaoEmEvento(self.idMembro, self.partesDoItem))
				self.salvarParticipacaoEmEvento = 0
				return

			if self.salvarOrganizacaoDeEvento:
				self.listaOrganizacaoDeEvento.append(OrganizacaoDeEvento(self.idMembro, self.partesDoItem))
				self.salvarOrganizacaoDeEvento = 0
				return

			if self.salvarItem:
				# Produção bibliográfica
				if self.achouArtigoEmPeriodico:
 					iessimoItem = ArtigoEmPeriodico(self.idMembro, self.partesDoItem, self.doi, self.relevante)
					self.listaArtigoEmPeriodico.append(iessimoItem)
					self.salvarItem = 0
					self.doi = ''
					self.relevante = 0
					return

				if self.achouLivroPublicado:
 					iessimoItem = LivroPublicado(self.idMembro, self.partesDoItem, self.relevante)
					self.listaLivroPublicado.append(iessimoItem)
					self.salvarItem = 0
					self.relevante = 0
					return

				if self.achouCapituloDeLivroPublicado:
 					iessimoItem = CapituloDeLivroPublicado(self.idMembro, self.partesDoItem, self.relevante)
					self.listaCapituloDeLivroPublicado.append(iessimoItem)
					self.salvarItem = 0
					self.relevante = 0
					return

				if self.achouTextoEmJornalDeNoticia:
 					iessimoItem = TextoEmJornalDeNoticia(self.idMembro, self.partesDoItem, self.relevante)
					self.listaTextoEmJornalDeNoticia.append(iessimoItem)
					self.salvarItem = 0
					self.relevante = 0
					return

				if self.achouTrabalhoCompletoEmCongresso:
 					iessimoItem = TrabalhoCompletoEmCongresso(self.idMembro, self.partesDoItem, self.relevante)
					self.listaTrabalhoCompletoEmCongresso.append(iessimoItem)
					self.salvarItem = 0
					self.relevante = 0
					return

				if self.achouResumoExpandidoEmCongresso:
 					iessimoItem = ResumoExpandidoEmCongresso(self.idMembro, self.partesDoItem, self.doi, self.relevante)
					self.listaResumoExpandidoEmCongresso.append(iessimoItem)
					self.salvarItem = 0
					self.doi = ''
					self.relevante = 0
					return

				if self.achouResumoEmCongresso:
 					iessimoItem = ResumoEmCongresso(self.idMembro, self.partesDoItem, self.doi, self.relevante)
					self.listaResumoEmCongresso.append(iessimoItem)
					self.salvarItem = 0
					self.doi = ''
					self.relevante = 0
					return

				if self.achouArtigoAceito:
 					iessimoItem =  ArtigoAceito(self.idMembro, self.partesDoItem, self.doi, self.relevante)
					self.listaArtigoAceito.append(iessimoItem)
					self.salvarItem = 0
					self.doi = ''
					self.relevante = 0
					return

				if self.achouApresentacaoDeTrabalho:
 					iessimoItem =  ApresentacaoDeTrabalho(self.idMembro, self.partesDoItem, self.relevante)
					self.listaApresentacaoDeTrabalho.append(iessimoItem)
					self.salvarItem = 0
					return

				if self.achouOutroTipoDeProducaoBibliografica:
 					iessimoItem = OutroTipoDeProducaoBibliografica(self.idMembro, self.partesDoItem, self.relevante)
					self.listaOutroTipoDeProducaoBibliografica.append(iessimoItem)
					self.salvarItem = 0
					return

				# Produção técnica
				if self.achouSoftwareComPatente:
 					iessimoItem = SoftwareComPatente(self.idMembro, self.partesDoItem, self.relevante)
					self.listaSoftwareComPatente.append(iessimoItem)
					self.salvarItem = 0
					return

				if self.achouSoftwareSemPatente:
 					iessimoItem = SoftwareSemPatente(self.idMembro, self.partesDoItem, self.relevante)
					self.listaSoftwareSemPatente.append(iessimoItem)
					self.salvarItem = 0
					return

				if self.achouProdutoTecnologico:
 					iessimoItem = ProdutoTecnologico(self.idMembro, self.partesDoItem, self.relevante)
					self.listaProdutoTecnologico.append(iessimoItem)
					self.salvarItem = 0
					return

				if self.achouProcessoOuTecnica:
 					iessimoItem = ProcessoOuTecnica(self.idMembro, self.partesDoItem, self.relevante)
					self.listaProcessoOuTecnica.append(iessimoItem)
					self.salvarItem = 0
					return

				if self.achouTrabalhoTecnico:
 					iessimoItem = TrabalhoTecnico(self.idMembro, self.partesDoItem, self.relevante)
					self.listaTrabalhoTecnico.append(iessimoItem)
					self.salvarItem = 0
					return

				if self.achouOutroTipoDeProducaoTecnica:
 					iessimoItem = OutroTipoDeProducaoTecnica(self.idMembro, self.partesDoItem, self.relevante)
					self.listaOutroTipoDeProducaoTecnica.append(iessimoItem)
					self.salvarItem = 0
					return

				if self.achouProducaoArtistica:
 					iessimoItem = ProducaoArtistica(self.idMembro, self.partesDoItem, self.relevante)
					self.listaProducaoArtistica.append(iessimoItem)
					self.salvarItem = 0
					return

				# Orientações em andamento
				if self.achouOrientacoesEmAndamento:
					if self.achouSupervisaoDePosDoutorado:
						self.listaOASupervisaoDePosDoutorado.append( OrientacaoEmAndamento(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = 0
						return

					if self.achouTeseDeDoutorado:
						self.listaOATeseDeDoutorado.append( OrientacaoEmAndamento(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouDissertacaoDeMestrado:
						self.listaOADissertacaoDeMestrado.append( OrientacaoEmAndamento(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouMonografiaDeEspecializacao:
						self.listaOAMonografiaDeEspecializacao.append( OrientacaoEmAndamento(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouTCC:
						self.listaOATCC.append( OrientacaoEmAndamento(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouIniciacaoCientifica:
						self.listaOAIniciacaoCientifica.append( OrientacaoEmAndamento(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouOutroTipoDeOrientacao:
						self.listaOAOutroTipoDeOrientacao.append( OrientacaoEmAndamento(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

				# Orientações concluidas
				if self.achouOrientacoesConcluidas :
					if self.achouSupervisaoDePosDoutorado:
						self.listaOCSupervisaoDePosDoutorado.append( OrientacaoConcluida(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouTeseDeDoutorado:
						self.listaOCTeseDeDoutorado.append( OrientacaoConcluida(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouDissertacaoDeMestrado:
						self.listaOCDissertacaoDeMestrado.append( OrientacaoConcluida(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouMonografiaDeEspecializacao:
						self.listaOCMonografiaDeEspecializacao.append( OrientacaoConcluida(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouTCC:
						self.listaOCTCC.append( OrientacaoConcluida(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouIniciacaoCientifica:
						self.listaOCIniciacaoCientifica.append( OrientacaoConcluida(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return

					if self.achouOutroTipoDeOrientacao:
						self.listaOCOutroTipoDeOrientacao.append( OrientacaoConcluida(self.idMembro, self.partesDoItem, self.idOrientando) )
						self.salvarItem = 0
						self.idOrientando = ''
						return


		if tag=='tr': # para os items armazenados apenas em linhas <TR>
			if self.salvarAreaDeAtuacao:
				iessimaAreaDeAtucao = AreaDeAtuacao(self.partesDoItem) # criamos um objeto com a lista correspondentes às celulas da linha
				self.listaAreaDeAtuacao.append(iessimaAreaDeAtucao) # acrescentamos o objeto de AreaDeAtuacao
				self.salvarAreaDeAtuacao = 0
				return

			if self.salvarIdioma:
				iessimoIdioma = Idioma(self.partesDoItem) # criamos um objeto com a lista correspondentes às celulas da linha
				self.listaIdioma.append(iessimoIdioma) # acrescentamos o objeto de Idioma
				self.salvarIdioma = 0
				return

			if self.salvarPremioOuTitulo:
				iessimoPremio = PremioOuTitulo(self.idMembro, self.partesDoItem) # criamos um objeto com a lista correspondentes às celulas da linha
				self.listaPremioOuTitulo.append(iessimoPremio) # acrescentamos o objeto de PremioOuTitulo
				self.salvarPremioOuTitulo = 0
				return

		if tag=='td':

			if self.salvarEnderecoProfissional:
				self.enderecoProfissional = stripBlanks(self.item)
				self.enderecoProfissional = re.sub("\'", '', self.enderecoProfissional)
				self.enderecoProfissional = re.sub("\"", '', self.enderecoProfissional)

				self.salvarEnderecoProfissional = 0
				self.achouEnderecoProfissional = 0
				return

			if self.salvarSexo:
				self.sexo = stripBlanks(self.item)
				self.salvarSexo = 0
				self.achouSexo = 0
				return

			if self.salvarNomeEmCitacoes:
				self.nomeEmCitacoesBibliograficas = stripBlanks(self.item)
				self.salvarNomeEmCitacoes = 0
				self.achouNomeEmCitacoes = 0
				return

			if self.salvarFormacaoAcademica or self.salvarProjetoDePesquisa or self.salvarAreaDeAtuacao or self.salvarIdioma or self.salvarPremioOuTitulo or self.salvarParticipacaoEmEvento or self.salvarOrganizacaoDeEvento or self.salvarItem:
				self.partesDoItem.append(stripBlanks(self.item)) # acrescentamos cada celula da linha numa lista!
				return


		if tag=='em':
			self.procurarCabecalho = 0

		if tag=='html':
			if self.foto=='':
				self.foto = 'usuaria.png' if self.sexo.lower()=='feminino' else 'usuario.png'

	# ------------------------------------------------------------------------ #
	def handle_data(self, dado):
		self.item = self.item + htmlentitydecode(dado)

		if not self.salvarItem:
			dado = stripBlanks(dado)

			if u'Endereço profissional'==dado:
				self.achouEnderecoProfissional = 1

			if u'Sexo'==dado:
				self.achouSexo = 1

			if u'Nome em citações bibliográficas'==dado:
				self.achouNomeEmCitacoes = 1

			if self.salvarAtualizacaoCV:
				data = re.findall(u'Última atualização do currículo em (\d{2}/\d{2}/\d{4})', dado)

				if len(data)>0: # se a data de atualizacao do CV for identificada
					self.atualizacaoCV = stripBlanks(data[0])
					self.salvarAtualizacaoCV = 0

			if self.procurarCabecalho:
				if u'Formação acadêmica/Titulação'==dado:
					self.achouFormacaoAcademica = 1

				if u'Projetos de Pesquisa'==dado:
					self.achouProjetoDePesquisa = 1
	
				if u'Áreas de atuação'==dado:
					self.achouAreaDeAtuacao = 1
			
				if u'Idiomas'==dado:
					self.achouIdioma = 1

				if u'Prêmios e títulos'==dado:
					self.achouPremioOuTitulo = 1

				return


		if self.achouGrupo:
			dado = stripBlanks(dado)

			# Produção bibliográfica
			if  u'Artigos completos publicados em periódicos'==dado:
				self.achouArtigoEmPeriodico = 1
				return
			if u'Livros publicados/organizados ou edições'==dado:
				self.achouLivroPublicado = 1
				return
			if u'Capítulos de livros publicados'==dado:
				self.achouCapituloDeLivroPublicado = 1
				return
			if u'Textos em jornais de notícias/revistas'==dado:
				self.achouTextoEmJornalDeNoticia = 1
				return
			if u'Trabalhos completos publicados em anais de congressos'==dado:
				self.achouTrabalhoCompletoEmCongresso = 1
				return
			if u'Resumos expandidos publicados em anais de congressos'==dado:
				self.achouResumoExpandidoEmCongresso = 1
				return
			if u'Resumos publicados em anais de congressos' in dado:
				self.achouResumoEmCongresso = 1
				return
			if u'Artigos aceitos para publicação'==dado:
				self.achouArtigoAceito = 1
				return
			if u'Apresentações de Trabalho'==dado:
				self.achouApresentacaoDeTrabalho = 1
				return
			if u'Demais tipos de produção bibliográfica'==dado:
				self.achouOutroTipoDeProducaoBibliografica = 1
				return

			# Produção técnica
			if u'Softwares com registro de patente'==dado:
				self.achouSoftwareComPatente = 1
				return
			if u'Softwares sem registro de patente'==dado:
				self.achouSoftwareSemPatente = 1
				return
			if u'Produtos tecnológicos'==dado:
				self.achouProdutoTecnologico = 1
				return
			if u'Processos ou técnicas'==dado:
				self.achouProcessoOuTecnica = 1
				return
			if u'Trabalhos técnicos'==dado:
				self.achouTrabalhoTecnico = 1
				return
			if u'Demais tipos de produção técnica'==dado:
				self.achouOutroTipoDeProducaoTecnica = 1
				return

			# Tipos de orientações (em andamento ou concluídas)
			if u'Supervisão de pós-doutorado'==dado:
				self.achouSupervisaoDePosDoutorado = 1
				return
			if u'Tese de doutorado'==dado:
				self.achouTeseDeDoutorado = 1
				return
			if u'Dissertação de mestrado'==dado:
				self.achouDissertacaoDeMestrado = 1
				return
			if u'Monografia de conclusão de curso de aperfeiçoamento/especialização'==dado:
				self.achouMonografiaDeEspecializacao = 1
				return
			if u'Trabalho de conclusão de curso de graduação'==dado:
				self.achouTCC = 1
				return
			if u'Iniciação científica' in dado or u'Iniciação Científica'==dado:
				self.achouIniciacaoCientifica = 1
				return
			if u'Orientações de outra natureza'==dado:
				self.achouOutroTipoDeOrientacao = 1
				return


		dado = stripBlanks(dado)
		if u'Produção artística/cultural'==dado:
			self.achouProducaoArtistica = 1
			self.achouGrupo = 1
			
			self.achouArtigoEmPeriodico = 0
			self.achouLivroPublicado = 0
			self.achouCapituloDeLivroPublicado = 0
			self.achouTextoEmJornalDeNoticia = 0
			self.achouTrabalhoCompletoEmCongresso = 0
			self.achouResumoExpandidoEmCongresso = 0
			self.achouResumoEmCongresso = 0
			self.achouArtigoAceito = 0
			self.achouApresentacaoDeTrabalho = 0
			self.achouOutroTipoDeProducaoBibliografica = 0

			self.achouSoftwareComPatente = 0
			self.achouSoftwareSemPatente = 0
			self.achouProdutoTecnologico = 0
			self.achouProcessoOuTecnica = 0
			self.achouTrabalhoTecnico = 0
			self.achouOutroTipoDeProducaoTecnica = 0
			return

		if  u'Orientações em andamento'==dado:
			self.achouOrientacoesEmAndamento = 1
			self.achouOrientacoesConcluidas = 0
			return

		if u'Supervisões e orientações concluídas'==dado:
			self.achouOrientacoesEmAndamento = 0
			self.achouOrientacoesConcluidas = 1
			return

		if u'Participação em eventos'==dado:
			self.achouParticipacaoEmEvento  = 1
			self.achouOrganizacaoDeEvento = 0
			return

		if u'Organização de eventos'==dado:
			self.achouParticipacaoEmEvento  = 0
			self.achouOrganizacaoDeEvento = 1
			return

# ---------------------------------------------------------------------------- #
def stripBlanks(s):
	return re.sub('\s+', ' ', s).strip()

def htmlentitydecode(s):                                                                               
	return re.sub('&(%s);' % '|'.join(name2codepoint),                                                 
		lambda m: unichr(name2codepoint[m.group(1)]), s)   

